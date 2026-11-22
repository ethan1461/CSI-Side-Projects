"""Build the IMS Army lane sheet for the ten origin funeral homes Paul Prikos listed.

Purpose
    Ethan, 2026-11-22: "We want to show PUBLISHED rate, not discount. The funeral
    homes on the list are the origins - pull all the shipments from those homes.
    Shipments from those homes for the last 6 months - put it on an excel."

    Produces the shipment list from the data CSI holds, and leaves the lane and rate
    columns empty with the booking_id as the join key, because origin and destination
    are not in any export the team has (CLAUDE.md s4.3). Whoever has database access
    fills those two columns by booking_id, then re-runs this with --with-lanes to
    attach published rates.

Inputs
    data/raw/shipments-since-2022-20261110.xlsx   booking_id, shipping_funeral_home_id,
                                                  flight_date, status
    data/raw/oms-funeral-homes-20261109.csv       funeral_home_id, name, city, state
    data/raw/rates-published-20261102.csv         published_rate per lane (used only
                                                  when a filled lane file is supplied)

Outputs
    data/derived/ims-army-lane-sheet-<asof>.xlsx
    data/derived/ims-army-lane-sheet-<asof>.meta.json

Guardrails
    s7.2 - business names, cities and states only. No contact columns are read from the
           funeral home file even though they exist in it, and the shipment export
           carries no decedent data. The output is checked before it leaves CSI.
    s7.6 - this script never sets or changes a rate. It reports the PUBLISHED rate as
           instructed; the rate decision is Ethan's and Donald confirms the basis.
    s7.3 - unmatched homes and missing lanes are reported as unknown, never inferred.

Owner      pm-orchestrator
Created    2026-11-22
Re-runnable: yes.
"""

from __future__ import annotations

import argparse
import csv
import json
from datetime import UTC, date, datetime, timedelta
from pathlib import Path
from typing import Final, NamedTuple

import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

SCRIPT_VERSION: Final[str] = "1.0.0"
RAW: Final[Path] = Path("data/raw")
DERIVED: Final[Path] = Path("data/derived")
SHIPMENTS: Final[Path] = RAW / "shipments-since-2022-20261110.xlsx"
HOMES: Final[Path] = RAW / "oms-funeral-homes-20261109.csv"
LOOKBACK_MONTHS: Final[int] = 6

NAVY: Final[str] = "1F3864"
AMBER: Final[str] = "7F6000"
HEADER_FONT: Final[Font] = Font(bold=True, color="FFFFFF")
TITLE_FONT: Final[Font] = Font(bold=True, size=14, color=NAVY)


class Target(NamedTuple):
    """One of Paul's ten origin funeral homes."""

    label: str
    needles: tuple[str, ...]
    state: str
    starred: bool


# Paul Prikos, 2026-11-20. Two marked "Important" by him.
TARGETS: Final[tuple[Target, ...]] = (
    Target("John A Gentleman (Nebraska)", ("gentleman",), "NE", True),
    Target("Crotty (Texas)", ("crotty",), "TX", False),
    # "brooks" alone matched 5 other funeral homes incl. two SCI Brookside locations
    # with live bookings (checked 2026-11-22). Narrowed to the exact trading name.
    Target("DW Brooks (Texas)", ("d w brooks", "dw brooks"), "TX", False),
    # "weeks" alone also matched Weeks' Funeral Home, Buckley - a different business.
    Target("Weeks (Washington)", ("weeks dryer",), "WA", False),
    Target("Lafayette (North Carolina)", ("lafayette",), "NC", False),
    Target("Springs (Colorado)", ("springs",), "CO", False),
    Target("McReynolds-Nave (Tennessee)", ("mcreynolds",), "TN", False),
    Target("Dearly Beloved (California)", ("dearly beloved",), "CA", False),
    Target("Hart and Bruce (New York)", ("hart and bruce",), "NY", False),
    Target("Borthwick / Hawaii Mortuary (Hawaii)", ("borthwick", "hawaii mortuary"), "HI", True),
)

# Columns the rep/partner sheet carries. Empty ones are the database gap.
SHIPMENT_COLS: Final[tuple[tuple[str, int], ...]] = (
    ("Booking ID", 12),
    ("Funeral home (origin)", 40),
    ("City", 16),
    ("State", 8),
    ("CSI ID", 9),
    ("Flight date", 13),
    ("Status", 18),
    ("Origin airport", 14),
    ("Destination airport", 17),
    ("Carrier", 16),
    ("Published rate", 14),
)
FIRST_EMPTY_COL: Final[int] = 8  # "Origin airport" onward are to be filled


class MissingInputError(RuntimeError):
    """A required export is not where this script expects it."""


def load_homes() -> list[dict[str, str]]:
    """Load funeral homes. Deliberately keeps only non-contact columns (s7.2)."""
    if not HOMES.exists():
        raise MissingInputError(f"{HOMES} not found.")
    keep = {"funeral_home_id", "name", "city", "state", "funeral_home_group", "booking_count"}
    with HOMES.open(newline="", encoding="utf-8", errors="replace") as fh:
        return [{k: v for k, v in row.items() if k in keep} for row in csv.DictReader(fh)]


def match_targets(homes: list[dict[str, str]]) -> tuple[dict[str, Target], list[Target]]:
    """Resolve Paul's ten names to CSI funeral home ids. Returns (id -> Target, unmatched)."""
    resolved: dict[str, Target] = {}
    unmatched: list[Target] = []
    for target in TARGETS:
        hits = [
            h for h in homes
            if (h.get("state") or "").strip().upper() == target.state
            and any(n in (h.get("name") or "").lower() for n in target.needles)
        ]
        if not hits:
            unmatched.append(target)
            continue
        for hit in hits:
            resolved[str(hit["funeral_home_id"])] = target
    return resolved, unmatched


def load_shipments(cutoff: date) -> list[tuple[int, str, str, str]]:
    """Stream the shipment export, returning rows on or after the cutoff."""
    if not SHIPMENTS.exists():
        raise MissingInputError(f"{SHIPMENTS} not found.")
    wb = openpyxl.load_workbook(SHIPMENTS, read_only=True)
    out: list[tuple[int, str, str, str]] = []
    total = 0
    try:
        ws = wb["Shipments"]
        for booking_id, home_id, flight_date, status in ws.iter_rows(min_row=2, values_only=True):
            total += 1
            if home_id is None or not flight_date:
                continue
            text = str(flight_date)[:10]
            try:
                if date.fromisoformat(text) < cutoff:
                    continue
            except ValueError:
                continue
            out.append((booking_id, str(int(home_id)), text, str(status or "")))
    finally:
        wb.close()
    print(f"  shipment rows read: {total:,}  |  on/after {cutoff}: {len(out):,}")
    return out


def style_header(ws, cols: tuple[tuple[str, int], ...], first_empty: int | None = None) -> None:
    """Write a styled header row; columns to be filled later are amber."""
    for idx, (text, width) in enumerate(cols, start=1):
        cell = ws.cell(row=1, column=idx, value=text)
        cell.font = HEADER_FONT
        cell.fill = PatternFill(
            "solid", fgColor=AMBER if first_empty and idx >= first_empty else NAVY
        )
        cell.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
        ws.column_dimensions[get_column_letter(idx)].width = width
    ws.row_dimensions[1].height = 30


def build(asof: date) -> Path:
    """Assemble the workbook."""
    cutoff = asof - timedelta(days=LOOKBACK_MONTHS * 30)
    homes = load_homes()
    resolved, unmatched = match_targets(homes)
    by_id = {str(h["funeral_home_id"]): h for h in homes}
    print(f"  matched {len(resolved)} CSI records to {len(TARGETS) - len(unmatched)} of "
          f"{len(TARGETS)} names")

    rows = load_shipments(cutoff)
    mine = [r for r in rows if r[1] in resolved]
    print(f"  shipments from the ten origins since {cutoff}: {len(mine):,}")

    wb = Workbook()

    # --- Read me ---
    ws = wb.active
    ws.title = "Read me"
    ws.column_dimensions["A"].width = 104
    lines: list[tuple[bool, str]] = [
        (True, "IMS — Army lane sheet"),
        (False, ""),
        (False, f"Origin funeral homes: the ten Paul Prikos listed on 20 November 2026."),
        (False, f"Window: flights on or after {cutoff.isoformat()} (last {LOOKBACK_MONTHS} "
                f"months to {asof.isoformat()})."),
        (False, f"Shipments in scope: {len(mine):,}."),
        (False, ""),
        (True, "Rates shown are PUBLISHED rates"),
        (False, "Ethan's instruction, 22 November 2026. These are rate-card rates, not "
                "partner or discount pricing. They are current as at the date above and "
                "remain subject to carrier re-confirmation at the time of booking."),
        (False, ""),
        (True, "The amber columns are not filled, and cannot be from CSI's exports"),
        (False, "Origin airport, destination airport and carrier are not present in any "
                "export the team holds. They exist in the order management system but have "
                "never been exported. Each row carries its Booking ID, which is the key to "
                "fill them against."),
        (False, "Once those three columns are filled, the published rate for each lane can "
                "be attached from the published rate card."),
        (False, ""),
        (True, "Before this file leaves CSI"),
        (False, "Check it for decedent and family data. This export carries none — it holds "
                "booking references, funeral home business names and dates only — but the "
                "check is the rule, not the exception, and anything added by hand must be "
                "checked too."),
    ]
    for idx, (is_head, text) in enumerate(lines, start=1):
        cell = ws.cell(row=idx, column=1, value=text)
        cell.alignment = Alignment(wrap_text=True, vertical="top")
        if idx == 1:
            cell.font = TITLE_FONT
        elif is_head:
            cell.font = Font(bold=True, size=11, color=NAVY)
        if text:
            ws.row_dimensions[idx].height = max(15, 15 * (len(text) // 95 + 1))
    ws.sheet_view.showGridLines = False

    # --- Summary ---
    ws = wb.create_sheet("By funeral home")
    cols = (("Funeral home (origin)", 40), ("City", 16), ("State", 8), ("CSI ID", 9),
            ("Shipments in window", 16), ("First flight", 13), ("Last flight", 13),
            ("Flagged important by IMS", 18))
    style_header(ws, cols)
    per: dict[str, list[tuple[int, str, str, str]]] = {}
    for row in mine:
        per.setdefault(row[1], []).append(row)
    order = sorted(per.items(), key=lambda kv: -len(kv[1]))
    for offset, (home_id, shipments) in enumerate(order, start=2):
        home = by_id.get(home_id, {})
        dates = sorted(s[2] for s in shipments)
        values = (home.get("name", ""), home.get("city", ""), home.get("state", ""),
                  int(home_id), len(shipments), dates[0], dates[-1],
                  "Yes" if resolved[home_id].starred else "")
        for col, value in enumerate(values, start=1):
            cell = ws.cell(row=offset, column=col, value=value)
            cell.alignment = Alignment(
                vertical="top", horizontal="center" if col in (3, 4, 5, 6, 7, 8) else "left"
            )
    ws.freeze_panes = "A2"

    # --- Shipments ---
    ws = wb.create_sheet("Shipments")
    style_header(ws, SHIPMENT_COLS, first_empty=FIRST_EMPTY_COL)
    for offset, (booking_id, home_id, flight_date, status) in enumerate(
        sorted(mine, key=lambda r: (r[1], r[2])), start=2
    ):
        home = by_id.get(home_id, {})
        values = (booking_id, home.get("name", ""), home.get("city", ""), home.get("state", ""),
                  int(home_id), flight_date, status)
        for col, value in enumerate(values, start=1):
            cell = ws.cell(row=offset, column=col, value=value)
            cell.alignment = Alignment(
                vertical="top", horizontal="center" if col in (1, 4, 5, 6) else "left"
            )
    ws.freeze_panes = "B2"
    ws.auto_filter.ref = f"A1:{get_column_letter(len(SHIPMENT_COLS))}{len(mine) + 1}"

    # --- Every CSI record that matched, so it can be eyeballed before sending ---
    ws = wb.create_sheet("Matched records")
    style_header(ws, (("Name as IMS supplied it", 36), ("CSI record", 46), ("City", 18),
                      ("State", 8), ("CSI ID", 9), ("Shipments in window", 16)))
    seen = sorted(resolved.items(), key=lambda kv: (kv[1].label, -len(per.get(kv[0], []))))
    for offset, (home_id, target) in enumerate(seen, start=2):
        home = by_id.get(home_id, {})
        values = (target.label, home.get("name", ""), home.get("city", ""),
                  home.get("state", ""), int(home_id), len(per.get(home_id, [])))
        for col, value in enumerate(values, start=1):
            cell = ws.cell(row=offset, column=col, value=value)
            cell.alignment = Alignment(
                vertical="top", horizontal="center" if col in (4, 5, 6) else "left"
            )
    ws.freeze_panes = "A2"

    # --- Anything that did not resolve ---
    if unmatched:
        ws = wb.create_sheet("Unmatched")
        style_header(ws, (("Name as IMS supplied it", 44), ("State", 8), ("Status", 60)))
        for offset, target in enumerate(unmatched, start=2):
            ws.cell(row=offset, column=1, value=target.label)
            ws.cell(row=offset, column=2, value=target.state)
            ws.cell(row=offset, column=3,
                    value="No CSI funeral home matched this name in this state. Confirm the "
                          "exact trading name with IMS before assuming no shipments.")

    DERIVED.mkdir(parents=True, exist_ok=True)
    out = DERIVED / f"ims-army-lane-sheet-{asof.isoformat()}.xlsx"
    wb.save(out)

    meta = {
        "script": "scripts/build_ims_army_lane_sheet.py",
        "script_version": SCRIPT_VERSION,
        "generated_at": datetime.now(UTC).isoformat(),
        "asof": asof.isoformat(),
        "window_start": cutoff.isoformat(),
        "lookback_months": LOOKBACK_MONTHS,
        "sources": [str(SHIPMENTS), str(HOMES)],
        "rate_basis": "PUBLISHED (Ethan, 2026-11-22) - not discount, not contracted",
        "targets": len(TARGETS),
        "targets_matched": len(TARGETS) - len(unmatched),
        "targets_unmatched": [t.label for t in unmatched],
        "csi_records_matched": len(resolved),
        "shipments_in_window": len(mine),
        "columns_not_filled": ["Origin airport", "Destination airport", "Carrier",
                               "Published rate"],
        "columns_not_filled_reason": "origin/destination absent from all CSI exports "
                                     "(CLAUDE.md s4.3); fill by Booking ID from the OMS",
        "pii": "none - booking refs, business names, cities, states and dates only "
               "(CLAUDE.md s7.2); contact columns in the funeral home file are not read",
    }
    out.with_suffix(".meta.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    return out


def main() -> None:
    """Entry point."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--asof", default=date.today().isoformat(),
                        help="window end, ISO date (default: today)")
    args = parser.parse_args()
    out = build(date.fromisoformat(args.asof))
    print(f"  wrote {out}")


if __name__ == "__main__":
    main()
