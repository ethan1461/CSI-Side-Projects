"""Build the IMS Army published-rate sheet from the IMS-billed leg export.

Purpose
    Ethan, 2026-11-22: show IMS the PUBLISHED rates for the shipments CSI billed
    to them out of Paul Prikos's ten origin funeral homes. CSI charged IMS the
    discount rate; IMS charged their own customers the published rate, so the
    published rate is what they need for the Army renewal.

    One row per booking: the lane actually flown, the carrier, the full routing,
    and the published rate. Where the rate card prices by weight ("var") and no
    weight is held, a RANGE is shown rather than a single invented figure
    (Ethan: "Put the range we show then").

Inputs
    data/raw/ims-army-lanes-ims-billed-20261122.tsv   500 legs / 286 bookings
    data/raw/rates-published-20261102.csv             6,919 published lanes
    data/raw/oms-funeral-homes-20261109.csv           business names only

Outputs
    data/derived/ims-army-published-rates-<asof>.xlsx
    data/derived/ims-army-published-rates-<asof>.meta.json

Guardrails
    s7.2 - business names, airports, dates, booking refs only. No decedent or
           family data is read or written; the deceased table was never joined.
    s7.3 - unmatched lanes are reported as unmatched, never estimated. The rate
           basis is printed on every row.
    s7.6 - reports published rates as they stand. Sets no rate.

Owner      pm-orchestrator
Created    2026-11-22
Re-runnable: yes.
"""

from __future__ import annotations

import csv
import json
from collections import defaultdict
from datetime import UTC, date, datetime
from pathlib import Path
from typing import Final, NamedTuple

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

SCRIPT_VERSION: Final[str] = "1.0.0"
RAW: Final[Path] = Path("data/raw")
DERIVED: Final[Path] = Path("data/derived")
LEGS: Final[Path] = RAW / "ims-army-lanes-ims-billed-20261122.tsv"
RATES: Final[Path] = RAW / "rates-published-20261102.csv"
HOMES: Final[Path] = RAW / "oms-funeral-homes-20261109.csv"

NAVY: Final[str] = "1F3864"
AMBER: Final[str] = "7F6000"
HEADER_FONT: Final[Font] = Font(bold=True, color="FFFFFF")
TITLE_FONT: Final[Font] = Font(bold=True, size=14, color=NAVY)

# Flight-number prefix is the reliable carrier field (Ethan's note); the airline
# text column has mixed case, trailing spaces and 8 blanks.
PREFIX_TO_AIRLINE: Final[dict[str, str]] = {
    "AA": "American Airlines",
    "DL": "Delta Airlines",
    "WN": "Southwest Airlines",
    "UA": "United Airlines",
    "HA": "Hawaiian Airlines",
    "AS": "Alaska Airlines",
    "TK": "Turkish Airlines",
}
TEXT_TO_AIRLINE: Final[dict[str, str]] = {
    "AMERICAN AIRLINES": "American Airlines",
    "DELTA AIRLINES": "Delta Airlines",
    "SOUTHWEST AIRLINES": "Southwest Airlines",
    "UNITED AIRLINES": "United Airlines",
    "HAWAIIAN AIRLINES": "Hawaiian Airlines",
    "ALASKA AIRLINES": "Alaska Airlines",
    "TURKISH AIRLINES": "Turkish Airlines",
}


class Leg(NamedTuple):
    """One flight leg."""

    booking_id: int
    reg_date: str
    home_id: str
    leg_type: str
    leg_seq: int
    airline_text: str
    flight: str
    origin: str
    destination: str


class RateHit(NamedTuple):
    """A published-rate lookup result."""

    basis: str
    lo: float | None
    hi: float | None
    rate_types: str
    rows: int


def normalise_airline(leg: Leg) -> tuple[str, str]:
    """Resolve the carrier. Returns (airline, how_resolved)."""
    flight = (leg.flight or "").strip().upper().replace("#", "")
    prefix = flight[:2]
    if prefix in PREFIX_TO_AIRLINE:
        name = PREFIX_TO_AIRLINE[prefix]
        text = TEXT_TO_AIRLINE.get((leg.airline_text or "").strip().upper())
        if text and text != name:
            return name, f"flight number ({prefix}) — CONFLICTS with airline field '{leg.airline_text.strip()}'"
        return name, "flight number"
    text = TEXT_TO_AIRLINE.get((leg.airline_text or "").strip().upper())
    if text:
        return text, "airline field"
    return "", "unresolved"


def chain_route(legs: list[Leg]) -> list[str]:
    """Order legs into a route by connectivity, not by leg id or leg type."""
    origins = [l.origin for l in legs]
    dests = [l.destination for l in legs]
    starts = [o for o in origins if o not in dests]
    by_origin: dict[str, Leg] = {}
    for leg in sorted(legs, key=lambda l: l.leg_seq):
        by_origin.setdefault(leg.origin, leg)
    if len(set(starts)) != 1:
        ordered = sorted(legs, key=lambda l: (l.leg_type != "domestic", l.leg_seq))
        route = [ordered[0].origin] + [l.destination for l in ordered]
        return route
    route = [starts[0]]
    seen: set[str] = set()
    while route[-1] in by_origin and route[-1] not in seen:
        seen.add(route[-1])
        route.append(by_origin[route[-1]].destination)
    return route


def load_rates() -> dict[tuple[str, str, str], list[dict[str, str]]]:
    """Index airport-to-airport published rates by (airline, origin, destination)."""
    index: dict[tuple[str, str, str], list[dict[str, str]]] = defaultdict(list)
    with RATES.open(newline="", encoding="utf-8", errors="replace") as fh:
        for row in csv.DictReader(fh):
            if row["origin_type"] != "airport" or row["destination_type"] != "airport":
                continue
            key = (row["airline"].strip(), row["origin"].strip().upper(),
                   row["destination"].strip().upper())
            index[key].append(row)
    return index


def lookup(index: dict[tuple[str, str, str], list[dict[str, str]]],
           airline: str, origin: str, dest: str) -> RateHit:
    """Look up a published rate; returns a range when several rows match."""
    rows = index.get((airline, origin, dest), [])
    if not rows:
        return RateHit("no published rate for this lane", None, None, "", 0)
    vals: list[float] = []
    for r in rows:
        try:
            vals.append(float(str(r["published_rate"]).replace("$", "").replace(",", "")))
        except (ValueError, TypeError):
            continue
    types = ",".join(sorted({r["rate_type"] for r in rows}))
    if not vals:
        return RateHit("matched, rate not numeric", None, None, types, len(rows))
    return RateHit("published rate card", min(vals), max(vals), types, len(rows))


def main() -> None:
    """Assemble the workbook."""
    asof = date.today()
    with LEGS.open(newline="", encoding="utf-8") as fh:
        legs = [
            Leg(int(r["booking_id"]), r["registration_date"], r["funeral_home_id"],
                r["leg_type"], int(r["leg_seq"]), r["airline"], r["flight"],
                (r["origin_airport"] or "").strip().upper(),
                (r["destination_airport"] or "").strip().upper())
            for r in csv.DictReader(fh, delimiter="\t") if r.get("booking_id")
        ]
    print(f"  legs read: {len(legs)}")

    with HOMES.open(newline="", encoding="utf-8", errors="replace") as fh:
        homes = {r["funeral_home_id"]: r for r in csv.DictReader(fh)}

    index = load_rates()
    by_booking: dict[int, list[Leg]] = defaultdict(list)
    for leg in legs:
        by_booking[leg.booking_id].append(leg)
    print(f"  bookings: {len(by_booking)}")

    records: list[dict[str, object]] = []
    for bid, blegs in sorted(by_booking.items()):
        route = chain_route(blegs)
        carriers: list[str] = []
        hows: set[str] = set()
        for leg in sorted(blegs, key=lambda l: l.leg_seq):
            name, how = normalise_airline(leg)
            hows.add(how)
            if name and name not in carriers:
                carriers.append(name)
        lane_o, lane_d = route[0], route[-1]
        carrier = carriers[0] if len(carriers) == 1 else ""
        hit = lookup(index, carrier, lane_o, lane_d) if carrier else RateHit(
            "multi-carrier routing — no single lane rate", None, None, "", 0)
        home = homes.get(blegs[0].home_id, {})
        records.append({
            "booking_id": bid,
            "date": blegs[0].reg_date,
            "home": home.get("name", ""),
            "state": home.get("state", ""),
            "home_id": blegs[0].home_id,
            "lane": f"{lane_o}–{lane_d}",
            "origin": lane_o,
            "dest": lane_d,
            "carrier": carrier or " / ".join(carriers),
            "carrier_src": "; ".join(sorted(hows)),
            "routing": " → ".join(route),
            "legs": len(blegs),
            "basis": hit.basis,
            "lo": hit.lo,
            "hi": hit.hi,
            "rate_types": hit.rate_types,
            "rate_rows": hit.rows,
        })

    matched = sum(1 for r in records if r["lo"] is not None)
    print(f"  matched to a published lane rate: {matched} of {len(records)}")

    wb = Workbook()

    ws = wb.active
    ws.title = "Read me"
    ws.column_dimensions["A"].width = 106
    lines: list[tuple[bool, str]] = [
        (True, "IMS — published rates on Army-origin shipments"),
        (False, ""),
        (False, f"{len(records)} shipments CSI billed to International Mortuary Shipping, "
                f"out of the ten origin funeral homes IMS listed. "
                f"Booking dates 2026-01-01 to {asof.isoformat()}."),
        (False, ""),
        (True, "Rates shown are PUBLISHED rates"),
        (False, "Rate-card rates as at 2026-11-02, current and subject to carrier "
                "re-confirmation at time of booking. Not partner or contract pricing."),
        (False, ""),
        (True, "Why some rates are a range"),
        (False, "Most published lanes are priced by weight (rate type 'var'). The rate card "
                "holds no included weight, and chargeable weight is not in this extract, so "
                "where the card carries more than one rate for a lane the low and high are "
                "both shown. A single figure has not been invented."),
        (False, ""),
        (True, "Why some rows have no rate"),
        (False, "Three reasons, each named in the Rate basis column: the lane is not on the "
                "published card; the shipment routed on more than one carrier so no single "
                "lane rate applies; or the carrier is not one CSI publishes rates for — the "
                "card covers American, Southwest, Delta and United only."),
        (False, ""),
        (True, "Lane definition"),
        (False, "First leg's origin to last leg's destination, assembled by connectivity. "
                "The full routing is shown so a multi-stop shipment is not mistaken for a "
                "direct one."),
        (False, ""),
        (True, "Before this file leaves CSI"),
        (False, "Check it for decedent and family data. This extract holds none — booking "
                "references, business names, airports and dates only — but the check is the "
                "rule, not the exception."),
    ]
    for i, (head, text) in enumerate(lines, start=1):
        c = ws.cell(row=i, column=1, value=text)
        c.alignment = Alignment(wrap_text=True, vertical="top")
        if i == 1:
            c.font = TITLE_FONT
        elif head:
            c.font = Font(bold=True, size=11, color=NAVY)
        if text:
            ws.row_dimensions[i].height = max(15, 15 * (len(text) // 97 + 1))
    ws.sheet_view.showGridLines = False

    def grid(sheet, cols: tuple[tuple[str, int], ...], amber_from: int | None = None) -> None:
        for i, (t, w) in enumerate(cols, start=1):
            c = sheet.cell(row=1, column=i, value=t)
            c.font = HEADER_FONT
            c.fill = PatternFill("solid", fgColor=AMBER if amber_from and i >= amber_from else NAVY)
            c.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
            sheet.column_dimensions[get_column_letter(i)].width = w
        sheet.row_dimensions[1].height = 30

    # --- Shipments ---
    ws = wb.create_sheet("Shipments")
    cols = (("Booking", 10), ("Date", 11), ("Funeral home (origin)", 34), ("State", 7),
            ("Lane", 12), ("Carrier", 19), ("Routing", 26), ("Legs", 6),
            ("Published rate (low)", 14), ("Published rate (high)", 14),
            ("Rate type", 10), ("Rate basis", 36))
    grid(ws, cols, amber_from=9)
    for i, r in enumerate(records, start=2):
        for j, v in enumerate((r["booking_id"], r["date"], r["home"], r["state"], r["lane"],
                               r["carrier"], r["routing"], r["legs"], r["lo"], r["hi"],
                               r["rate_types"], r["basis"]), start=1):
            c = ws.cell(row=i, column=j, value=v)
            c.alignment = Alignment(vertical="top",
                                    horizontal="center" if j in (1, 4, 8, 11) else "left")
            if j in (9, 10) and v is not None:
                c.number_format = '#,##0.00'
    ws.freeze_panes = "C2"
    ws.auto_filter.ref = f"A1:{get_column_letter(len(cols))}{len(records) + 1}"

    # --- By lane ---
    ws = wb.create_sheet("By lane")
    grid(ws, (("Lane", 12), ("Carrier", 19), ("Shipments", 11),
              ("Published rate (low)", 15), ("Published rate (high)", 15),
              ("Rate type", 10), ("Rate basis", 36)))
    lanes: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for r in records:
        lanes[(str(r["lane"]), str(r["carrier"]))].append(r)
    for i, ((lane, carrier), rs) in enumerate(
            sorted(lanes.items(), key=lambda kv: -len(kv[1])), start=2):
        f = rs[0]
        for j, v in enumerate((lane, carrier, len(rs), f["lo"], f["hi"],
                               f["rate_types"], f["basis"]), start=1):
            c = ws.cell(row=i, column=j, value=v)
            c.alignment = Alignment(vertical="top",
                                    horizontal="center" if j in (1, 3, 6) else "left")
            if j in (4, 5) and v is not None:
                c.number_format = '#,##0.00'
    ws.freeze_panes = "A2"

    # --- By funeral home ---
    ws = wb.create_sheet("By funeral home")
    grid(ws, (("Funeral home (origin)", 38), ("State", 7), ("CSI ID", 9),
              ("Shipments", 11), ("Distinct lanes", 13), ("With a published rate", 18)))
    per: dict[str, list[dict[str, object]]] = defaultdict(list)
    for r in records:
        per[str(r["home_id"])].append(r)
    for i, (hid, rs) in enumerate(sorted(per.items(), key=lambda kv: -len(kv[1])), start=2):
        h = homes.get(hid, {})
        for j, v in enumerate((h.get("name", ""), h.get("state", ""), int(hid), len(rs),
                               len({r["lane"] for r in rs}),
                               sum(1 for r in rs if r["lo"] is not None)), start=1):
            c = ws.cell(row=i, column=j, value=v)
            c.alignment = Alignment(vertical="top",
                                    horizontal="center" if j != 1 else "left")
    ws.freeze_panes = "A2"

    DERIVED.mkdir(parents=True, exist_ok=True)
    out = DERIVED / f"ims-army-published-rates-{asof.isoformat()}.xlsx"
    wb.save(out)

    unmatched: dict[str, int] = defaultdict(int)
    for r in records:
        if r["lo"] is None:
            unmatched[str(r["basis"])] += 1
    meta = {
        "script": "scripts/build_ims_army_rate_sheet.py",
        "script_version": SCRIPT_VERSION,
        "generated_at": datetime.now(UTC).isoformat(),
        "sources": [str(LEGS), str(RATES), str(HOMES)],
        "legs": len(legs),
        "bookings": len(records),
        "matched_to_published_rate": matched,
        "unmatched_reasons": dict(unmatched),
        "rate_basis": "PUBLISHED (Ethan, 2026-11-22)",
        "billed_to": "International Mortuary Shipping, LLC (funeral_home_id 2767)",
        "pii": "none - booking refs, business names, airports, dates (CLAUDE.md s7.2)",
    }
    out.with_suffix(".meta.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    print(f"  unmatched: {dict(unmatched)}")
    print(f"  wrote {out}")


if __name__ == "__main__":
    main()
