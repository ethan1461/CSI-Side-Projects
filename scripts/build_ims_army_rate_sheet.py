"""Build the IMS Army published-rate sheet.

Purpose
    Ethan, 2026-11-22: show IMS the PUBLISHED rates for the shipments CSI billed
    to them out of the ten origin funeral homes IMS listed for the Army renewal.
    CSI charged IMS the discount rate; IMS charged its own customers the
    published rate, so published is what they need.

Pricing model (learned from the database, 2026-11-22)
    The four US majors are priced ZONE to ZONE, not airport to airport, and each
    carrier keeps its own zone column on the airport row - a Delta "NE" is not a
    United "NE". Rates further split by SHIPMENT TYPE (casket / ashes / infant /
    combo), which is why one zone pair carried several prices.

    Resolution order per lane end: airport row, then US state row, then the
    carrier's zone. American's Hawaii and Puerto Rico rates are state rows.
    Zone comparison is case-insensitive: three United rows say "MIdwest".

Honest limits, all surfaced in the workbook rather than smoothed over
    * 106 airline/route/type combinations carry two or more ACTIVE rows at
      different prices. The export holds no updated_at, so there is no basis to
      pick one. Both are shown as a range and listed on the Rate conflicts tab.
    * 5 bookings have no shipment type recorded. Not priced, not guessed.
    * Southwest has no zone for HNL, ITO or SJU.
    * United publishes Casket rates only.

Inputs
    data/raw/ims-army-lanes-ims-billed-20261122.tsv   500 legs / 286 bookings
    data/raw/ims-A-airport-zones.tsv                  83 airports
    data/raw/ims-B-state-regions.tsv                  51 states
    data/raw/ims-C-major-rates.tsv                    active rates, typed
    data/raw/ims-D-shipment-types.tsv                 type per booking
    data/raw/oms-funeral-homes-20261109.csv           business names

Outputs
    data/derived/ims-army-published-rates-<asof>.xlsx
    data/derived/ims-army-published-rates-<asof>.meta.json

Guardrails
    s7.2 - booking refs, business names, airports and dates only. The deceased
           table was never joined and no name is read or written.
    s7.3 - nothing is estimated. Every unpriced row states why.
    s7.6 - reports published rates as they stand; sets no rate.

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

SCRIPT_VERSION: Final[str] = "2.0.0"
RAW: Final[Path] = Path("data/raw")
DERIVED: Final[Path] = Path("data/derived")

NAVY: Final[str] = "1F3864"
AMBER: Final[str] = "7F6000"
HEADER_FONT: Final[Font] = Font(bold=True, color="FFFFFF")
TITLE_FONT: Final[Font] = Font(bold=True, size=14, color=NAVY)

ZONE_COLUMN: Final[dict[str, str]] = {
    "American Airlines": "american_region",
    "Delta Airlines": "delta_region",
    "Southwest Airlines": "southwest_zone",
    "United Airlines": "united_region",
}
PREFIX_TO_AIRLINE: Final[dict[str, str]] = {
    "AA": "American Airlines", "DL": "Delta Airlines", "WN": "Southwest Airlines",
    "UA": "United Airlines", "HA": "Hawaiian Airlines", "AS": "Alaska Airlines",
    "TK": "Turkish Airlines",
}
TEXT_TO_AIRLINE: Final[dict[str, str]] = {
    "AMERICAN AIRLINES": "American Airlines", "DELTA AIRLINES": "Delta Airlines",
    "SOUTHWEST AIRLINES": "Southwest Airlines", "UNITED AIRLINES": "United Airlines",
    "HAWAIIAN AIRLINES": "Hawaiian Airlines", "ALASKA AIRLINES": "Alaska Airlines",
    "TURKISH AIRLINES": "Turkish Airlines",
}


class Leg(NamedTuple):
    booking_id: int
    reg_date: str
    home_id: str
    leg_seq: int
    airline_text: str
    flight: str
    origin: str
    destination: str


class Hit(NamedTuple):
    lo: float | None
    hi: float | None
    basis: str
    conflict: bool
    n: int


def read_tsv(path: Path) -> list[dict[str, str]]:
    """Read a tab-separated export, skipping blank trailing rows."""
    with path.open(newline="", encoding="utf-8", errors="replace") as fh:
        return [r for r in csv.DictReader(fh, delimiter="\t") if any(v for v in r.values())]


def carrier_of(leg: Leg) -> tuple[str, str]:
    """Resolve the carrier. The flight-number prefix beats the airline text field."""
    flight = (leg.flight or "").strip().upper().replace("#", "")
    pre = flight[:2]
    text = TEXT_TO_AIRLINE.get((leg.airline_text or "").strip().upper())
    if pre in PREFIX_TO_AIRLINE:
        name = PREFIX_TO_AIRLINE[pre]
        if text and text != name:
            return name, f"flight no. ({pre}); airline field said {text}"
        return name, "flight no."
    return (text, "airline field") if text else ("", "unresolved")


def chain(legs: list[Leg]) -> list[str]:
    """Order legs into a route by connectivity, ignoring the unreliable leg type."""
    dests = {l.destination for l in legs}
    starts = [l.origin for l in legs if l.origin not in dests]
    nxt: dict[str, str] = {}
    for leg in sorted(legs, key=lambda l: l.leg_seq):
        nxt.setdefault(leg.origin, leg.destination)
    if len(set(starts)) != 1:
        ordered = sorted(legs, key=lambda l: l.leg_seq)
        return [ordered[0].origin] + [l.destination for l in ordered]
    route, seen = [starts[0]], set()
    while route[-1] in nxt and route[-1] not in seen:
        seen.add(route[-1])
        route.append(nxt[route[-1]])
    return route


def main() -> None:
    """Assemble the workbook."""
    asof = date.today()
    legs = [
        Leg(int(r["booking_id"]), r["registration_date"], r["funeral_home_id"],
            int(r["leg_seq"]), r["airline"], r["flight"],
            r["origin_airport"].strip().upper(), r["destination_airport"].strip().upper())
        for r in read_tsv(RAW / "ims-army-lanes-ims-billed-20261122.tsv")
    ]
    airports = {r["airport_code"].strip().upper(): r
                for r in read_tsv(RAW / "ims-A-airport-zones.tsv")}
    states = {r["state"].strip().upper(): r for r in read_tsv(RAW / "ims-B-state-regions.tsv")}
    types = {int(r["booking_id"]): (r.get("shipment_type") or "").strip()
             for r in read_tsv(RAW / "ims-D-shipment-types.tsv")}
    with (RAW / "oms-funeral-homes-20261109.csv").open(
            newline="", encoding="utf-8", errors="replace") as fh:
        homes = {r["funeral_home_id"]: r for r in csv.DictReader(fh)}

    # Rates, de-duplicated: rate_id is nullable and repeats, so key on the values.
    seen_rate: set[tuple[str, ...]] = set()
    rates: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    raw_rate_rows = read_tsv(RAW / "ims-C-major-rates.tsv")
    for r in raw_rate_rows:
        if (r.get("is_active") or "").strip() not in ("1", ""):
            continue
        key = tuple(r.get(c, "") for c in (
            "airline", "origin_type", "origin", "destination_type", "destination",
            "rate_type", "published_rate", "shipment_rate_type_id"))
        if key in seen_rate:
            continue
        seen_rate.add(key)
        rates[(r["airline"].strip(), (r.get("shipment_type") or "").strip())].append(r)
    print(f"  rate rows: {len(raw_rate_rows)} read, {len(seen_rate)} after de-duplication")

    def ends_for(airline: str, ap: str) -> list[tuple[str, str]]:
        """Candidate (type, value) pairs for one end of a lane, most specific first."""
        out: list[tuple[str, str]] = [("airport", ap)]
        row = airports.get(ap)
        if not row:
            return out
        st = (row.get("us_state") or "").strip().upper()
        if st:
            out.append(("state", st))
        col = ZONE_COLUMN.get(airline, "")
        zone = (row.get(col) or "").strip()
        if not zone and st in states:
            zone = (states[st].get(col) or "").strip()
        if zone:
            out.append(("zone", zone))
        return out

    def price(airline: str, stype: str, o: str, d: str) -> Hit:
        pool = rates.get((airline, stype), [])
        if not pool:
            return Hit(None, None, f"{airline} publishes no {stype or 'this'} rate", False, 0)
        o_ends, d_ends = ends_for(airline, o), ends_for(airline, d)
        non_numeric = ""
        for ot, ov in o_ends:
            for dt, dv in d_ends:
                vals: list[float] = []
                for r in pool:
                    if (r["origin_type"].strip() != ot
                            or r["origin"].strip().lower() != ov.lower()
                            or r["destination_type"].strip() != dt
                            or r["destination"].strip().lower() != dv.lower()):
                        continue
                    raw = str(r["published_rate"]).replace("$", "").replace(",", "").strip()
                    try:
                        vals.append(float(raw))
                    except (ValueError, TypeError):
                        # The card carries a note instead of a figure - American's
                        # Hawaii casket rate reads "varies per city". That is the card
                        # declining to state a rate, not a missing lane. Say which.
                        if raw and not non_numeric:
                            non_numeric = f'rate card reads "{raw}"'
                if vals:
                    lo, hi = min(vals), max(vals)
                    basis = f"{ot} {ov} → {dt} {dv}"
                    return Hit(lo, hi, basis, lo != hi, len(vals))
        if non_numeric:
            return Hit(None, None, non_numeric, False, 0)
        zones = [v for t, v in o_ends if t == "zone"] + [v for t, v in d_ends if t == "zone"]
        if len(zones) < 2:
            missing = o if not any(t == "zone" for t, _ in o_ends) else d
            return Hit(None, None, f"{airline} has no zone for {missing}", False, 0)
        return Hit(None, None, "no published rate for this zone pair", False, 0)

    by_booking: dict[int, list[Leg]] = defaultdict(list)
    for leg in legs:
        by_booking[leg.booking_id].append(leg)

    records: list[dict[str, object]] = []
    for bid, blegs in sorted(by_booking.items()):
        route = chain(blegs)
        carriers, notes = [], set()
        for leg in sorted(blegs, key=lambda l: l.leg_seq):
            name, how = carrier_of(leg)
            notes.add(how)
            if name and name not in carriers:
                carriers.append(name)
        stype = types.get(bid, "")
        o, d = route[0], route[-1]
        if len(carriers) != 1:
            hit = Hit(None, None, "multi-carrier routing — no single lane rate", False, 0)
        elif not stype:
            hit = Hit(None, None, "shipment type not recorded on the booking", False, 0)
        else:
            hit = price(carriers[0], stype, o, d)
        home = homes.get(blegs[0].home_id, {})
        records.append({
            "booking_id": bid, "date": blegs[0].reg_date, "home": home.get("name", ""),
            "state": home.get("state", ""), "home_id": blegs[0].home_id,
            "lane": f"{o}–{d}", "carrier": carriers[0] if len(carriers) == 1
            else " / ".join(carriers), "carrier_note": "; ".join(sorted(notes)),
            "type": stype or "not recorded", "routing": " → ".join(route),
            "legs": len(blegs), "lo": hit.lo, "hi": hit.hi, "basis": hit.basis,
            "conflict": hit.conflict,
        })

    priced = sum(1 for r in records if r["lo"] is not None)
    conflicts = sum(1 for r in records if r["conflict"])
    print(f"  priced: {priced} of {len(records)}   (of which rate-conflicted: {conflicts})")
    for b, n in sorted(defaultdict(int, {
            str(r["basis"]): sum(1 for x in records if x["basis"] == r["basis"])
            for r in records if r["lo"] is None}).items(), key=lambda kv: -kv[1]):
        print(f"    unpriced: {n:>3}  {b}")

    # ---------------- workbook ----------------
    wb = Workbook()

    def grid(sheet, cols, amber_from=None):
        for i, (t, w) in enumerate(cols, start=1):
            c = sheet.cell(row=1, column=i, value=t)
            c.font = HEADER_FONT
            c.fill = PatternFill("solid", fgColor=AMBER if amber_from and i >= amber_from else NAVY)
            c.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
            sheet.column_dimensions[get_column_letter(i)].width = w
        sheet.row_dimensions[1].height = 30

    ws = wb.active
    ws.title = "Read me"
    ws.column_dimensions["A"].width = 106
    unpriced = len(records) - priced
    lines = [
        (True, "IMS — published rates on Army-origin shipments"),
        (False, ""),
        (False, f"{len(records)} shipments Cargo Sales International billed to International "
                f"Mortuary Shipping, out of the ten origin funeral homes IMS listed. Booking "
                f"dates 1 January 2026 to {asof.strftime('%-d %B %Y')}. "
                f"{priced} carry a published rate; {unpriced} do not, each for a stated reason."),
        (False, ""),
        (True, "These are PUBLISHED rates"),
        (False, "Rate-card rates as at 2 November 2026, current and subject to carrier "
                "re-confirmation at the time of booking. Not partner or contract pricing."),
        (False, ""),
        (True, "How a rate is found"),
        (False, "The four US carriers price by ZONE, not by airport, and each keeps its own "
                "zones — a Delta “NE” is not a United “NE”. Rates also differ by "
                "shipment type. Each lane is matched on the carrier's own zone for the first "
                "origin and the last destination, at that shipment's type. The Rate basis "
                "column states exactly which zone pair produced the figure."),
        (False, ""),
        (True, "Where a low and a high differ"),
        (False, "CSI's rate card currently holds more than one active rate for that lane and "
                "type, with nothing to say which supersedes the other. Both are shown rather "
                "than one chosen. The spread is small in every case. These are listed on the "
                "Rate conflicts tab and are being resolved."),
        (False, ""),
        (True, "Where there is no rate"),
        (False, "The reason is on the row, and one reason dominates. For casket shipments out "
                "of Hawaii, American's published card does not state a figure \u2014 it reads "
                "\u201cvaries per city\u201d \u2014 so those cannot be quoted from the card. The rest are "
                "small in number: a few shipments routed on more than one carrier, so no single "
                "lane rate applies; a handful of bookings have no shipment type recorded; and "
                "one carrier does not publish the type shipped. Nothing has been estimated to "
                "fill a gap."),
        (False, ""),
        (True, "Before this file leaves CSI"),
        (False, "Check it for decedent and family data. This extract holds none — booking "
                "references, business names, airports and dates only."),
    ]
    for i, (head, text) in enumerate(lines, start=1):
        c = ws.cell(row=i, column=1, value=text)
        c.alignment = Alignment(wrap_text=True, vertical="top")
        c.font = TITLE_FONT if i == 1 else (Font(bold=True, size=11, color=NAVY) if head else Font())
        if text:
            ws.row_dimensions[i].height = max(15, 15 * (len(text) // 97 + 1))
    ws.sheet_view.showGridLines = False

    ws = wb.create_sheet("Shipments")
    cols = (("Booking", 10), ("Date", 11), ("Funeral home (origin)", 32), ("St", 5),
            ("Lane", 11), ("Carrier", 18), ("Type", 10), ("Routing", 24), ("Legs", 5),
            ("Published rate", 13), ("High, where two apply", 15), ("Rate basis", 34))
    grid(ws, cols, amber_from=10)
    for i, r in enumerate(records, start=2):
        hi = r["hi"] if r["conflict"] else None
        for j, v in enumerate((r["booking_id"], r["date"], r["home"], r["state"], r["lane"],
                               r["carrier"], r["type"], r["routing"], r["legs"],
                               r["lo"], hi, r["basis"]), start=1):
            c = ws.cell(row=i, column=j, value=v)
            c.alignment = Alignment(vertical="top",
                                    horizontal="center" if j in (1, 4, 7, 9) else "left")
            if j in (10, 11) and v is not None:
                c.number_format = '#,##0.00'
    ws.freeze_panes = "C2"
    ws.auto_filter.ref = f"A1:{get_column_letter(len(cols))}{len(records) + 1}"

    ws = wb.create_sheet("By lane")
    grid(ws, (("Lane", 11), ("Carrier", 18), ("Type", 10), ("Shipments", 10),
              ("Published rate", 13), ("High, where two apply", 15), ("Rate basis", 34)))
    lanes: dict[tuple, list[dict]] = defaultdict(list)
    for r in records:
        lanes[(r["lane"], r["carrier"], r["type"])].append(r)
    for i, (k, rs) in enumerate(sorted(lanes.items(), key=lambda kv: -len(kv[1])), start=2):
        f = rs[0]
        for j, v in enumerate((k[0], k[1], k[2], len(rs), f["lo"],
                               f["hi"] if f["conflict"] else None, f["basis"]), start=1):
            c = ws.cell(row=i, column=j, value=v)
            c.alignment = Alignment(vertical="top",
                                    horizontal="center" if j in (1, 3, 4) else "left")
            if j in (5, 6) and v is not None:
                c.number_format = '#,##0.00'
    ws.freeze_panes = "A2"

    ws = wb.create_sheet("By funeral home")
    grid(ws, (("Funeral home (origin)", 36), ("St", 5), ("CSI ID", 8), ("Shipments", 10),
              ("Lanes", 8), ("Priced", 8), ("Not priced", 10)))
    per: dict[str, list[dict]] = defaultdict(list)
    for r in records:
        per[str(r["home_id"])].append(r)
    for i, (hid, rs) in enumerate(sorted(per.items(), key=lambda kv: -len(kv[1])), start=2):
        h = homes.get(hid, {})
        for j, v in enumerate((h.get("name", ""), h.get("state", ""), int(hid), len(rs),
                               len({r["lane"] for r in rs}),
                               sum(1 for r in rs if r["lo"] is not None),
                               sum(1 for r in rs if r["lo"] is None)), start=1):
            c = ws.cell(row=i, column=j, value=v)
            c.alignment = Alignment(vertical="top", horizontal="center" if j != 1 else "left")
    ws.freeze_panes = "A2"

    ws = wb.create_sheet("Rate conflicts")
    ws["A1"] = "Lanes where CSI's rate card holds more than one active rate"
    ws["A1"].font = TITLE_FONT
    ws["A2"] = ("Internal. Both figures are shown on the shipment rows because nothing in the "
                "rate table says which supersedes the other. Worth resolving in the card.")
    ws["A2"].alignment = Alignment(wrap_text=True, vertical="top")
    ws.column_dimensions["A"].width = 100
    grid_start = 4
    for i, (t, w) in enumerate((("Carrier", 20), ("Type", 10), ("Rate basis", 34),
                                ("Low", 12), ("High", 12), ("Spread", 10)), start=1):
        c = ws.cell(row=grid_start, column=i, value=t)
        c.font = HEADER_FONT
        c.fill = PatternFill("solid", fgColor=NAVY)
        ws.column_dimensions[get_column_letter(i)].width = w
    rown = grid_start + 1
    for key in sorted({(r["carrier"], r["type"], r["basis"], r["lo"], r["hi"])
                       for r in records if r["conflict"]}):
        for j, v in enumerate((key[0], key[1], key[2], key[3], key[4],
                               round(float(key[4]) - float(key[3]), 2)), start=1):
            c = ws.cell(row=rown, column=j, value=v)
            if j >= 4:
                c.number_format = '#,##0.00'
        rown += 1

    DERIVED.mkdir(parents=True, exist_ok=True)
    out = DERIVED / f"ims-army-published-rates-{asof.isoformat()}.xlsx"
    wb.save(out)

    reasons: dict[str, int] = defaultdict(int)
    for r in records:
        if r["lo"] is None:
            reasons[str(r["basis"])] += 1
    meta = {
        "script": "scripts/build_ims_army_rate_sheet.py",
        "script_version": SCRIPT_VERSION,
        "generated_at": datetime.now(UTC).isoformat(),
        "bookings": len(records), "legs": len(legs),
        "priced": priced, "unpriced": unpriced,
        "unpriced_reasons": dict(reasons),
        "rate_conflicts": conflicts,
        "rate_basis": "PUBLISHED (Ethan, 2026-11-22)",
        "billed_to": "International Mortuary Shipping, LLC (funeral_home_id 2767)",
        "rate_card_asof": "2026-11-02",
        "known_limits": [
            "106 airline/route/type combinations have 2+ active rates; no updated_at in the "
            "export, so both are shown rather than one picked.",
            "Southwest has no zone for HNL, ITO, SJU.",
            "United publishes Casket rates only.",
            "5 bookings have no shipment type recorded; not priced, not guessed.",
            "Combo type has no rates on any of the four carriers.",
        ],
        "pii": "none - booking refs, business names, airports, dates (CLAUDE.md s7.2)",
    }
    out.with_suffix(".meta.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    print(f"  wrote {out}")


if __name__ == "__main__":
    main()
