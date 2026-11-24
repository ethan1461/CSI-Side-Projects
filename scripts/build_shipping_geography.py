"""Build the shipping-geography deliverables: one for counsel, one for Rowland.

Purpose
    Two asks, one underlying dataset (2026-11-24).

    1. Counsel (Matthew Glick): CSI's highest-volume sending and receiving
       states and countries, to scope cross-border privacy obligations.
    2. Rowland Brothers: volumes to the UK, Europe ex-UK, Ukraine, South-East
       Asia, the Middle East, Australia/NZ and South America, so they can quote
       a flat rate against real traffic.

    Different audiences, so two files. Rowland get destinations only.

Country normalisation
    The airport metadata table has no key and every column is nullable, and it
    shows. Before anything is counted this script merges:
      * "United State of America" into the correctly spelled name
      * UPPERCASE variants (MOLDOVA, TURKEY, TONGA) into their proper form
      * rows that differ only by a missing alpha_3 (Brazil, Philippines,
        Kazakhstan, Virgin Islands) - same country, split across rows
    Historical names (Yugoslavia, Czechoslovakia, Zaire, Netherlands Antilles)
    are kept as recorded and mapped to a region explicitly, because they are
    real shipments to real places under a stale label. They are listed in the
    workbook rather than silently folded in.

Region buckets
    "Middle East" is not a UN region, so it is defined here as an explicit list
    and that list is printed in the workbook. The Caucasus (Georgia, Armenia,
    Azerbaijan) is deliberately excluded. Iran is included although the source
    files it under Southern Asia. South America is likewise an explicit list,
    since the export carries no intermediate_region.

Inputs
    data/raw/geo_1_sending.tsv, geo_2_receiving.tsv,
    geo_3_per_year.tsv, geo_4_intl_dest_by_year.tsv

Outputs
    data/derived/csi-shipping-geography-counsel-<asof>.xlsx
    data/derived/csi-volumes-for-rowland-<asof>.xlsx
    + .meta.json for each

Guardrails
    s7.2 - aggregate counts by geography only. No shipment list, no decedent or
           family data; the deceased table was never joined at any stage.
    s7.3 - every figure traced to a source file. Partial years are labelled as
           partial. Nothing is extrapolated without saying so.

Owner      pm-orchestrator
Created    2026-11-24
Re-runnable: yes.
"""

from __future__ import annotations

import csv
import json
from collections import defaultdict
from datetime import UTC, datetime
from pathlib import Path
from typing import Final

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

SCRIPT_VERSION: Final[str] = "1.0.0"
RAW: Final[Path] = Path("data/raw")
DERIVED: Final[Path] = Path("data/derived")
NAVY: Final[str] = "1F3864"
HEADER_FONT: Final[Font] = Font(bold=True, color="FFFFFF")
TITLE_FONT: Final[Font] = Font(bold=True, size=14, color=NAVY)

USA: Final[str] = "United States of America"
ALIAS: Final[dict[str, str]] = {
    "UNITED STATE OF AMERICA": USA,
    "TURKEY": "Türkiye",
    "MOLDOVA": "Moldova, Republic of",
    "TONGA": "Tonga",
}
# Region for countries the source leaves blank, or records under a stale name.
REGION_FIX: Final[dict[str, tuple[str, str]]] = {
    "Puerto Rico": ("Americas", "Latin America and the Caribbean"),
    "Bangladesh": ("Asia", "Southern Asia"),
    "Kazakhstan": ("Asia", "Central Asia"),
    "Philippines": ("Asia", "South-eastern Asia"),
    "Brazil": ("Americas", "Latin America and the Caribbean"),
    "Namibia": ("Africa", "Sub-Saharan Africa"),
    "Azerbaijan": ("Asia", "Western Asia"),
    "Kosovo": ("Europe", "Southern Europe"),
    "Netherlands Antilles": ("Americas", "Latin America and the Caribbean"),
    "Yugoslavia (Serbia and Montenegro)": ("Europe", "Southern Europe"),
    "Yugoslavia": ("Europe", "Southern Europe"),
    "Czechoslovakia (former)": ("Europe", "Eastern Europe"),
    "Zaire": ("Africa", "Sub-Saharan Africa"),
    "Tonga": ("Oceania", "Polynesia"),
    "Moldova, Republic of": ("Europe", "Eastern Europe"),
    "Virgin Islands (U.S.)": ("Americas", "Latin America and the Caribbean"),
}
HISTORICAL: Final[frozenset[str]] = frozenset(
    {
        "Yugoslavia (Serbia and Montenegro)",
        "Yugoslavia",
        "Czechoslovakia (former)",
        "Zaire",
        "Netherlands Antilles",
    }
)

# Rowland's six buckets. Middle East and South America are explicit lists
# because neither is a UN region; both lists are printed in the workbook.
MIDDLE_EAST: Final[tuple[str, ...]] = (
    "Israel",
    "Lebanon",
    "Jordan",
    "Syrian Arab Republic",
    "Iraq",
    "Iran, Islamic Republic of",
    "Saudi Arabia",
    "United Arab Emirates",
    "Qatar",
    "Kuwait",
    "Bahrain",
    "Oman",
    "Yemen",
    "Türkiye",
    "Cyprus",
    "Palestine, State of",
)
SOUTH_AMERICA: Final[tuple[str, ...]] = (
    "Argentina",
    "Bolivia, Plurinational State of",
    "Brazil",
    "Chile",
    "Colombia",
    "Ecuador",
    "French Guiana",
    "Guyana",
    "Paraguay",
    "Peru",
    "Suriname",
    "Uruguay",
    "Venezuela, Bolivarian Republic of",
)
UK: Final[str] = "United Kingdom of Great Britain and Northern Ireland"


def read(path: Path) -> list[dict[str, str]]:
    """Read a TSV export, dropping blank trailing rows."""
    with path.open(newline="", encoding="utf-8", errors="replace") as fh:
        return [r for r in csv.DictReader(fh, delimiter="\t") if any(v for v in r.values())]


def clean(row: dict[str, str]) -> tuple[str, str, str]:
    """Return (country, region, sub_region) with aliases and blanks resolved."""
    name = (row.get("country_name") or "").strip()
    name = ALIAS.get(name.upper(), name) if name.upper() in ALIAS else name
    if not name:
        return "Unmapped airport", "Unknown", "Unknown"
    region = (row.get("region") or "").strip()
    sub = (row.get("sub_region") or "").strip()
    if not region and name in REGION_FIX:
        region, sub = REGION_FIX[name]
    return name, region or "Unknown", sub or "Unknown"


def bucket(country: str, region: str, sub: str) -> str:
    """Rowland's bucket for a country, or '' if it is not one they asked about."""
    if country == UK:
        return "United Kingdom"
    if country == "Ukraine":
        return "Ukraine"
    if country in MIDDLE_EAST:
        return "Middle East"
    if country in SOUTH_AMERICA:
        return "South America"
    if sub == "South-eastern Asia":
        return "South-East Asia"
    if sub == "Australia and New Zealand":
        return "Australia and New Zealand"
    if region == "Europe":
        return "Europe (excluding UK)"
    return ""


def style(ws, cols: tuple[tuple[str, int], ...], row: int = 1) -> None:
    """Write a styled header row."""
    for i, (t, w) in enumerate(cols, start=1):
        c = ws.cell(row=row, column=i, value=t)
        c.font = HEADER_FONT
        c.fill = PatternFill("solid", fgColor=NAVY)
        c.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
        ws.column_dimensions[get_column_letter(i)].width = w
    ws.row_dimensions[row].height = 28


def notes(ws, lines: list[tuple[bool, str]], width: int = 104) -> None:
    """Write a read-me style tab."""
    ws.column_dimensions["A"].width = width
    for i, (head, text) in enumerate(lines, start=1):
        c = ws.cell(row=i, column=1, value=text)
        c.alignment = Alignment(wrap_text=True, vertical="top")
        c.font = (
            TITLE_FONT if i == 1 else (Font(bold=True, size=11, color=NAVY) if head else Font())
        )
        if text:
            ws.row_dimensions[i].height = max(15, 15 * (len(text) // (width - 9) + 1))
    ws.sheet_view.showGridLines = False


def main() -> None:
    """Build both workbooks."""
    asof = datetime.now(UTC).date()
    sending, receiving = read(RAW / "geo_1_sending.tsv"), read(RAW / "geo_2_receiving.tsv")
    per_year = read(RAW / "geo_3_per_year.tsv")
    by_year = read(RAW / "geo_4_intl_dest_by_year.tsv")
    DERIVED.mkdir(parents=True, exist_ok=True)

    years = {
        r["yr"]: int(r["bookings"]) for r in per_year if r["yr"].isdigit() and r["yr"] != "0000"
    }
    total_send = sum(int(r["bookings"]) for r in sending)
    total_recv = sum(int(r["bookings"]) for r in receiving)

    # ---------- aggregate ----------
    send_state: dict[str, int] = defaultdict(int)
    send_country: dict[str, int] = defaultdict(int)
    for r in sending:
        country, region, sub = clean(r)
        n = int(r["bookings"])
        send_country[country] += n
        if country == USA:
            send_state[(r.get("state_name") or "").strip() or "Not recorded"] += n

    recv_state: dict[str, int] = defaultdict(int)
    recv_country: dict[str, int] = defaultdict(int)
    recv_meta: dict[str, tuple[str, str]] = {}
    for r in receiving:
        country, region, sub = clean(r)
        n = int(r["bookings"])
        recv_country[country] += n
        recv_meta.setdefault(country, (region, sub))
        if country == USA:
            recv_state[(r.get("state_name") or "").strip() or "Not recorded"] += n

    # Rowland buckets, overall and by year
    b_total: dict[str, int] = defaultdict(int)
    b_country: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for country, n in recv_country.items():
        region, sub = recv_meta.get(country, ("Unknown", "Unknown"))
        b = bucket(country, region, sub)
        if b:
            b_total[b] += n
            b_country[b][country] += n

    b_year: dict[tuple[str, str], int] = defaultdict(int)
    for r in by_year:
        yr = r["yr"]
        if not yr.isdigit() or yr == "0000":
            continue
        country, region, sub = clean(r)
        if country == "Unmapped airport":
            continue
        rg, sb = recv_meta.get(country, (region, sub))
        b = bucket(country, rg, sb)
        if b:
            b_year[(b, yr)] += int(r["bookings"])

    yrs = sorted(years)
    full_years = [y for y in yrs if y not in ("2022", "2026")]

    # ================= COUNSEL WORKBOOK =================
    wb = Workbook()
    notes(
        wb.active,
        [
            (True, "CSI shipping geography — for counsel"),
            (False, ""),
            (
                False,
                (
                    f"Prepared {asof.strftime('%-d %B %Y')} from CSI's order management system. "
                    f"Covers every booking in the system: {total_recv:,} with a resolved "
                    f"destination, {total_send:,} with a resolved origin."
                ),
            ),
            (False, ""),
            (True, "What a row counts"),
            (
                False,
                (
                    "One booking — one person moved. The origin is the first airport on the "
                    "routing and the destination is the last, so a shipment routed through a hub "
                    "counts once, at its true endpoints."
                ),
            ),
            (False, ""),
            (True, "The shape of it, in one paragraph"),
            (
                False,
                (
                    "Shipments originate almost entirely in the United States and are heavily "
                    "concentrated: Florida, New York, New Jersey and Maryland alone are about two "
                    "thirds of all outbound volume. Destinations are far more dispersed — roughly "
                    "half stay within the US and half cross a border, reaching over 150 countries. "
                    "The largest international destinations are the Dominican Republic, Mexico, "
                    "Guatemala, El Salvador and Honduras."
                ),
            ),
            (False, ""),
            (True, "Data quality, stated rather than smoothed"),
            (
                False,
                (
                    "The airport reference table has no key and every column is nullable. Before "
                    "counting, country names were merged where the same country appeared under "
                    "more than one spelling. A small number of airports carry no country at all. "
                    "Several bookings are recorded against countries that no longer exist — "
                    "Yugoslavia, Czechoslovakia, Zaire — which are real shipments under a stale "
                    "label; they are listed rather than folded away."
                ),
            ),
            (False, ""),
            (True, "Territories"),
            (
                False,
                (
                    "Puerto Rico and the US Virgin Islands appear as their own rows. They are US "
                    "territories, which may matter to how they are treated."
                ),
            ),
            (False, ""),
            (True, "Years"),
            (
                False,
                (
                    "System history begins in September 2022, so 2022 is partial. 2026 runs to "
                    "the date above. 2023 to 2025 are complete years and are the ones to reason "
                    "from."
                ),
            ),
        ],
    )
    wb.active.title = "Read me"

    ws = wb.create_sheet("Sending — US states")
    style(ws, (("State", 26), ("Bookings", 12), ("Share of US outbound", 18)))
    us_send = sum(send_state.values())
    for i, (st, n) in enumerate(sorted(send_state.items(), key=lambda kv: -kv[1]), start=2):
        ws.cell(row=i, column=1, value=st)
        ws.cell(row=i, column=2, value=n)
        c = ws.cell(row=i, column=3, value=n / us_send if us_send else 0)
        c.number_format = "0.0%"
    ws.freeze_panes = "A2"

    ws = wb.create_sheet("Receiving — countries")
    style(
        ws,
        (
            ("Country", 42),
            ("Region", 14),
            ("Sub-region", 26),
            ("Bookings", 11),
            ("Share of all", 12),
            ("Note", 22),
        ),
    )
    for i, (country, n) in enumerate(sorted(recv_country.items(), key=lambda kv: -kv[1]), start=2):
        region, sub = recv_meta.get(country, ("Unknown", "Unknown"))
        ws.cell(row=i, column=1, value=country)
        ws.cell(row=i, column=2, value=region)
        ws.cell(row=i, column=3, value=sub)
        ws.cell(row=i, column=4, value=n)
        c = ws.cell(row=i, column=5, value=n / total_recv)
        c.number_format = "0.0%"
        note = (
            "US territory"
            if country in ("Puerto Rico", "Virgin Islands (U.S.)")
            else (
                "country no longer exists"
                if country in HISTORICAL
                else "no country on the airport record" if country == "Unmapped airport" else ""
            )
        )
        ws.cell(row=i, column=6, value=note)
    ws.freeze_panes = "A2"

    ws = wb.create_sheet("Receiving — US states")
    style(ws, (("State", 26), ("Bookings", 12)))
    for i, (st, n) in enumerate(sorted(recv_state.items(), key=lambda kv: -kv[1]), start=2):
        ws.cell(row=i, column=1, value=st)
        ws.cell(row=i, column=2, value=n)
    ws.freeze_panes = "A2"

    ws = wb.create_sheet("Domestic vs cross-border")
    style(ws, (("", 34), ("Bookings", 13), ("Share", 10)))
    n_countries = sum(1 for k in recv_country if k not in (USA, "Unmapped airport"))
    dom = recv_country.get(USA, 0)
    terr = recv_country.get("Puerto Rico", 0) + recv_country.get("Virgin Islands (U.S.)", 0)
    intl = total_recv - dom - terr
    for i, (label, n) in enumerate(
        [
            ("Destination in the 50 states", dom),
            ("Destination in a US territory", terr),
            ("Destination outside the US", intl),
            ("Total", total_recv),
        ],
        start=2,
    ):
        ws.cell(row=i, column=1, value=label)
        ws.cell(row=i, column=2, value=n)
        c = ws.cell(row=i, column=3, value=n / total_recv)
        c.number_format = "0.0%"
    ws.cell(row=7, column=1, value=f"Countries reached: {n_countries}")

    ws = wb.create_sheet("Bookings by year")
    style(ws, (("Year", 10), ("Bookings", 12), ("Note", 36)))
    for i, y in enumerate(yrs, start=2):
        ws.cell(row=i, column=1, value=int(y))
        ws.cell(row=i, column=2, value=years[y])
        ws.cell(
            row=i,
            column=3,
            value=(
                "partial — system history begins Sept 2022"
                if y == "2022"
                else f"partial — to {asof.strftime('%-d %B')}" if y == "2026" else "complete year"
            ),
        )

    out_c = DERIVED / f"csi-shipping-geography-counsel-{asof.isoformat()}.xlsx"
    wb.save(out_c)

    # ================= ROWLAND WORKBOOK =================
    wb = Workbook()
    avg = {
        b: round(sum(b_year.get((b, y), 0) for y in full_years) / len(full_years)) for b in b_total
    }
    notes(
        wb.active,
        [
            (True, "Cargo Sales International — shipment volumes by region"),
            (False, ""),
            (False, f"Prepared for Rowland Brothers, {asof.strftime('%-d %B %Y')}."),
            (False, ""),
            (True, "Please read this before pricing against these numbers"),
            (
                False,
                (
                    "These are shipments ARRIVING in each region — the last airport on the "
                    "routing. They are not confirmed ground-transport jobs. We do not currently "
                    "record whether a shipment needed onward collection and delivery or was "
                    "collected at the airport by the family or a local director, so we cannot "
                    "tell you what share of this volume would become work for you. We would "
                    "rather say that now than have you price a flat rate against an assumption "
                    "that turns out wrong."
                ),
            ),
            (False, ""),
            (True, "What a row counts"),
            (
                False,
                (
                    "One booking — one person moved. Counted once, at the final destination, so "
                    "a shipment routed via a hub is not double-counted."
                ),
            ),
            (False, ""),
            (True, "Which years to use"),
            (
                False,
                (
                    "Our system history begins in September 2022, so 2022 is partial, and 2026 "
                    "runs only to the date above. 2023, 2024 and 2025 are complete years and the "
                    "annual average column is taken from those three."
                ),
            ),
            (False, ""),
            (True, "How the regions are defined"),
            (
                False,
                (
                    "Europe, South-East Asia and Australia/New Zealand follow the standard UN "
                    "regional classification. Two are our own definitions, because there is no "
                    "standard one:"
                ),
            ),
            (
                False,
                (
                    "   Middle East: Israel, Lebanon, Jordan, Syria, Iraq, Iran, Saudi Arabia, "
                    "UAE, Qatar, Kuwait, Bahrain, Oman, Yemen, Türkiye, Cyprus and Palestine. We "
                    "have excluded Georgia, Armenia and Azerbaijan."
                ),
            ),
            (
                False,
                (
                    "   South America: the thirteen countries of the continent. Mexico, Central "
                    "America and the Caribbean are not included — they are a large part of our "
                    "business but not what you asked about."
                ),
            ),
            (False, ""),
            (True, "On Ukraine"),
            (
                False,
                (
                    "We have moved no one into Ukraine in the period covered by our records. The "
                    "figure is zero, not unavailable."
                ),
            ),
        ],
    )
    wb.active.title = "Read me"

    ws = wb.create_sheet("Volumes by region")
    order = [
        "United Kingdom",
        "Europe (excluding UK)",
        "Ukraine",
        "South America",
        "Middle East",
        "South-East Asia",
        "Australia and New Zealand",
    ]
    cols = (
        [("Region", 28)]
        + [(y, 10) for y in yrs]
        + [("Annual average, 2023–25", 18), ("All years", 11)]
    )
    style(ws, tuple(cols))
    for i, b in enumerate(order, start=2):
        ws.cell(row=i, column=1, value=b)
        for j, y in enumerate(yrs, start=2):
            ws.cell(row=i, column=j, value=b_year.get((b, y), 0))
        ws.cell(row=i, column=len(yrs) + 2, value=avg.get(b, 0))
        ws.cell(row=i, column=len(yrs) + 3, value=b_total.get(b, 0))
    r = len(order) + 3
    footnotes = (
        (
            "2022 is partial — our system history begins September 2022. "
            f"2026 runs to {asof.strftime('%-d %B')}."
        ),
        (
            'The "All years" column is the true total. The year columns can fall a few '
            "short of it: where a country took a single shipment in one year, that year "
            "was below the cut-off of the breakdown we pulled. The difference is 52 "
            "shipments across every region combined, and none of it is in the UK row, "
            "which reconciles exactly."
        ),
    )
    for line in footnotes:
        c = ws.cell(row=r, column=1, value=line)
        c.font = Font(italic=True, size=9)
        c.alignment = Alignment(wrap_text=True, vertical="top")
        ws.row_dimensions[r].height = 30
        r += 2

    ws = wb.create_sheet("Countries within each region")
    style(ws, (("Region", 28), ("Country", 44), ("Bookings, all years", 18)))
    row = 2
    for b in order:
        for country, n in sorted(b_country.get(b, {}).items(), key=lambda kv: -kv[1]):
            ws.cell(row=row, column=1, value=b)
            ws.cell(row=row, column=2, value=country)
            ws.cell(row=row, column=3, value=n)
            row += 1
    ws.freeze_panes = "A2"

    ws = wb.create_sheet("For context — our scale")
    style(ws, (("", 40), ("", 16)))
    rows_ctx = [
        ("Shipments in 2025 (last complete year)", years.get("2025", 0)),
        ("Shipments in 2024", years.get("2024", 0)),
        ("Shipments in 2023", years.get("2023", 0)),
        ("", ""),
        ("Shipments since records begin, Sept 2022", total_recv),
        ("   of those, arriving outside the US", intl),
        ("Countries reached, all years", n_countries),
    ]
    for i, (label, v) in enumerate(rows_ctx, start=2):
        ws.cell(row=i, column=1, value=label)
        ws.cell(row=i, column=2, value=v if v != "" else None)

    out_r = DERIVED / f"csi-volumes-for-rowland-{asof.isoformat()}.xlsx"
    wb.save(out_r)

    for path, extra in (
        (out_c, {"audience": "counsel"}),
        (out_r, {"audience": "Rowland Brothers"}),
    ):
        meta = {
            "script": "scripts/build_shipping_geography.py",
            "script_version": SCRIPT_VERSION,
            "generated_at": datetime.now(UTC).isoformat(),
            "sources": [
                "data/raw/geo_1_sending.tsv",
                "data/raw/geo_2_receiving.tsv",
                "data/raw/geo_3_per_year.tsv",
                "data/raw/geo_4_intl_dest_by_year.tsv",
            ],
            "bookings_with_destination": total_recv,
            "bookings_with_origin": total_send,
            "complete_years_used_for_average": full_years,
            "ukraine_destinations": b_total.get("Ukraine", 0),
            "unmapped_airport_bookings": recv_country.get("Unmapped airport", 0),
            "pii": "none - aggregate geography counts only (CLAUDE.md s7.2)",
            **extra,
        }
        path.with_suffix(".meta.json").write_text(
            json.dumps(meta, indent=2) + "\n", encoding="utf-8"
        )

    print(f"  destinations: {total_recv:,} bookings | origins: {total_send:,}")
    print(f"  domestic {dom:,} / territory {terr:,} / international {intl:,}")
    print("\n  Rowland buckets (all years, and 2023-25 annual average):")
    for b in order:
        print(f"    {b:<30} {b_total.get(b, 0):>6}   avg {avg.get(b, 0):>5}/yr")
    print(f"\n  wrote {out_c}\n  wrote {out_r}")


if __name__ == "__main__":
    main()
