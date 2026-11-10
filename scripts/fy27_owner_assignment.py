"""Build the FY27 company-owner assignment plan (Seg 1 and 2).

Purpose: apply Ethan's 2026-11-10 territory ruling. Midwest -> Otto, West -> Stacy,
unassigned Northeast/South split by alternating call_rank (rank-ordered, Otto first).
Inputs: data/derived/fy27-hubspot-members-seg{1,2}-*.csv (call_rank, tier, ids),
        data/derived/fy27-seg{1,2}-*.csv (terr, state, country_code, name),
        partner company ids passed via --partner-ids (from csi_partner_tier=true in HubSpot).
Outputs: data/derived/fy27-owner-plan.csv (+ .meta.json). Contains business names only.
Owner: revops-crm. Date: 2026-11-10. Idempotent: same input, same output.
"""
from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

D = Path("data/derived")
SEGS = {"1": "one-time", "2": "churned"}
OTTO, STACY = 102528265, 102528264


def load_seg(seg: str, name: str) -> list[dict[str, str]]:
    mem = {r["oms_funeral_home_id"]: r for r in csv.DictReader(open(D / f"fy27-hubspot-members-seg{seg}-{name}.csv"))}
    out = []
    for r in csv.DictReader(open(D / f"fy27-seg{seg}-{name}.csv")):
        m = mem[r["funeral_home_id"]]
        assert m["call_rank"] == r["call_rank"], (seg, r["funeral_home_id"])
        out.append({**r, "segment": seg, "hubspot_company_id": m["hubspot_company_id"]})
    return out


def build(partner_ids: set[str]) -> list[dict[str, str]]:
    plan: list[dict[str, str]] = []
    for seg, name in SEGS.items():
        rows = sorted(load_seg(seg, name), key=lambda r: int(r["call_rank"]))
        pool = 0
        for r in rows:
            owner, rule = "", ""
            if r["hubspot_company_id"] in partner_ids:
                rule = "SKIP partner tier"
            elif r["country_code"] != "us":
                rule = "SKIP non-US"
            elif r["terr"] == "Otto (Midwest)":
                owner, rule = "Otto", "Midwest rule"
            elif r["terr"] == "Stacy (West)":
                owner, rule = "Stacy", "West rule"
            elif r["terr"] == "Unassigned (Northeast/South)":
                owner = "Otto" if pool % 2 == 0 else "Stacy"
                pool += 1
                rule = f"NE/South alternation (pool position {pool})"
            else:
                rule = "SKIP no state"
            plan.append({"segment": seg, "call_rank": r["call_rank"], "tier": r["tier"],
                         "hubspot_company_id": r["hubspot_company_id"], "oms_funeral_home_id": r["funeral_home_id"],
                         "name": r["name"], "state": r["state"], "current_owner": "(none)",
                         "new_owner": owner, "rule": rule})
    return plan


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--partner-ids", default="")
    ap.add_argument("--owned-ids", default="")
    a = ap.parse_args()
    partners = {x for x in a.partner_ids.split(",") if x}
    plan = build(partners)
    out = D / "fy27-owner-plan.csv"
    with open(out, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(plan[0]))
        w.writeheader()
        w.writerows(plan)
    cnt = Counter((p["segment"], p["new_owner"] or p["rule"]) for p in plan)
    print(len(plan), dict(cnt))
    meta = {"script": "scripts/fy27_owner_assignment.py", "rows": len(plan), "run": datetime.now(timezone.utc).isoformat(),
            "sources": [str(p) for p in sorted(D.glob("fy27-hubspot-members-seg[12]-*.csv"))] + [str(p) for p in sorted(D.glob("fy27-seg[12]-*.csv"))],
            "dropped_columns": "none loaded beyond business name/city/state/ids", "counts": {f"{k[0]}|{k[1]}": v for k, v in cnt.items()}}
    (D / "fy27-owner-plan.meta.json").write_text(json.dumps(meta, indent=2))


if __name__ == "__main__":
    main()
