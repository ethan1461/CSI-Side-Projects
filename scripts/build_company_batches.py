"""Build HubSpot Company create/update batches from the OMS funeral home table.

Purpose: turn the 'create' tier of oms-company-plan.csv into batch payloads and a
record-level change log (log-before-write, CLAUDE.md 7.1). Never writes to HubSpot.
Inputs:  data/raw/oms-funeral-homes-20261103.csv, data/derived/oms-company-plan.csv
Outputs: data/derived/company-batches.jsonl (+ .meta.json), reports/account-layer-bulk-log.csv
Owner:   revops-crm (TASK-0020). Date: 2026-11-09.
Usage:   build_company_batches.py            writes the log and jsonl
         build_company_batches.py --batch N  prints batch N (10 records) as compact JSON
         build_company_batches.py --pilot    prints the 10 pilot updates
"""

from __future__ import annotations

import csv
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data/raw/oms-funeral-homes-20261103.csv"
PLAN = ROOT / "data/derived/oms-company-plan.csv"
OUT = ROOT / "data/derived/company-batches.jsonl"
LOG = ROOT / "reports/account-layer-bulk-log.csv"

# HubSpot Company IDs created in the 2026-11-03 pilot (reports/account-layer-pilot-log.md)
PILOT = {
    "2734": 60398025037, "1764": 60367230846, "2239": 60383235449, "2767": 60397415491,
    "3273": 60397908828, "6888": 60383698494, "21473": 60498692279, "1686": 60496410905,
    "1685": 60495014149, "1681": 60509877547,
}
CONFIRMED_PARTNERS = {"2734", "1764", "2239", "2767"}
# Judgement calls recorded in the task log: Las Rosas = exact-name Brooklyn record;
# Dunn & Sons = same entity as Karen C (19411, discount eligible), per Ethan.
EXTRA_PARTNERS = {"2143", "5176"}
BATCH = 10


def b(v: str) -> str:
    return "true" if v.strip() == "1" else "false"


def build() -> list[dict]:
    raw = {r["funeral_home_id"]: r for r in csv.DictReader(RAW.open(encoding="utf-8"))}
    plan = [r for r in csv.DictReader(PLAN.open()) if r["create_tier"] == "create"]
    out = []
    for p in plan:
        fid = p["funeral_home_id"]
        r = raw[fid]
        n = int(r["booking_count"] or 0)
        partner = fid in CONFIRMED_PARTNERS or fid in EXTRA_PARTNERS or r["is_discount_eligible"] == "1"
        cls = "partner" if partner else ("enterprise" if r["funeral_home_group"].strip() else "standard")
        country = r["country"].strip()
        if country == "United States of America":
            country = "United States"
        props = {
            "name": r["name"].strip(),
            "country": country,
            "lifecyclestage": "customer" if n > 0 else "lead",
            "hubspot_owner_id": "",
            "oms_funeral_home_id": fid,
            "oms_booking_count": str(n),
            "oms_is_shipper": b(r["is_shipper"]),
            "oms_is_discount_eligible": b(r["is_discount_eligible"]),
            "csi_partner_tier": "true" if partner else "false",
            "csi_account_class": cls,
        }
        today = datetime.now(timezone.utc).date().isoformat()
        zipc = r["zip"].strip()
        if set(zipc) == {"0"}:
            zipc = ""  # placeholder zip, not real
        last = r["last_booking_date"].strip()
        first = r["first_booking_date"].strip()
        if last > today or first > today:
            # impossible future date in the OMS: do not carry into the CRM, flag in the log
            last, first = ("" if last > today else last), ("" if first > today else first)
            props["_flag"] = "future_date"
        for k, v in (("state", r["state"]), ("city", r["city"]), ("zip", zipc),
                     ("oms_first_booking_date", first),
                     ("oms_last_booking_date", last),
                     ("oms_funeral_home_group", r["funeral_home_group"])):
            if v.strip():
                props[k] = v.strip()
        flag = props.pop("_flag", "")
        out.append({"id": fid, "pilot": fid in PILOT, "props": props, "flag": flag})
    return out


def main() -> None:
    recs = build()
    new = [r for r in recs if not r["pilot"]]
    if "--batch" in sys.argv:
        i = int(sys.argv[sys.argv.index("--batch") + 1])
        chunk = new[i * BATCH:(i + 1) * BATCH]
        print(json.dumps([{"objectType": "companies", "properties": r["props"]} for r in chunk],
                         separators=(",", ":"), ensure_ascii=False))
        return
    if "--pilot" in sys.argv:
        print(json.dumps([{"objectType": "companies", "objectId": PILOT[r["id"]], "properties": r["props"]}
                          for r in recs if r["pilot"]], separators=(",", ":"), ensure_ascii=False))
        return
    with OUT.open("w", encoding="utf-8") as f:
        for r in recs:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    with LOG.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["oms_funeral_home_id", "action", "hubspot_id", "current_value", "lifecycle",
                    "booking_count", "account_class", "partner_tier", "confidence", "batch", "flag"])
        ni = 0
        for r in recs:
            p = r["props"]
            if r["pilot"]:
                w.writerow([r["id"], "update", PILOT[r["id"]], "exists (pilot: name/state/country/lifecycle)",
                            p["lifecyclestage"], p["oms_booking_count"], p["csi_account_class"],
                            p["csi_partner_tier"], "high", "pilot", r["flag"]])
            else:
                w.writerow([r["id"], "create", "", "does not exist", p["lifecyclestage"],
                            p["oms_booking_count"], p["csi_account_class"], p["csi_partner_tier"],
                            "high", ni // BATCH, r["flag"]])
                ni += 1
    meta = {"source": [str(RAW.name), str(PLAN.name)], "rows_in_plan_create": len(recs),
            "rows_new": len(new), "rows_pilot_update": len(recs) - len(new),
            "batches": -(-len(new) // BATCH), "script": "build_company_batches.py v1",
            "run": datetime.now(timezone.utc).isoformat(),
            "dropped_columns": ["address", "email", "created_by", "updated_by", "shipper_account_number"]}
    OUT.with_suffix(".meta.json").write_text(json.dumps(meta, indent=2))
    cnt: dict[str, int] = {}
    for r in recs:
        k = r["props"]["csi_account_class"]
        cnt[k] = cnt.get(k, 0) + 1
    print(len(recs), len(new), meta["batches"], cnt)


if __name__ == "__main__":
    main()
