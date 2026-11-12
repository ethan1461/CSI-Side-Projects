"""Build per-rep retention call sheets from the three cohort lists.

Purpose: turn data/derived/accounts-{at-risk-volume-decline,dormant,one-and-done}.csv into
         call sheets for Otto and Stacy, plus holding lists for Ethan and for record repair.
Inputs:  the three cohort CSVs and data/derived/fy27-owner-plan.csv (HubSpot owner plan).
Outputs: data/derived/rep-call-sheet-{otto,stacy}-2026-11.csv, call-sheet-ethan-held-2026-11.csv,
         call-sheet-unrouted-2026-11.csv, call-sheet-summary-2026-11.json (+ .meta.json each).
Owner:   sales-lead. Date: 2026-11-12. Idempotent. Business names only; no contacts, no phone.
Routing: partner flag asserted (never name-filtered); group != Independent -> Ethan;
         territory per CLAUDE.md s5 authority 5 and fy27_owner_assignment.py.
"""
from __future__ import annotations

import csv
import json
from datetime import date, datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
D = ROOT / "data/derived"
AS_OF = date(2026, 11, 12)
YIELD = 1346  # 2026 average yield, CLAUDE.md s2. [ESTIMATE] wherever used.
MIDWEST = {"IL", "IN", "IA", "KS", "MI", "MN", "MO", "NE", "ND", "OH", "SD", "WI"}
WEST = {"CA", "OR", "WA", "AK", "HI", "AZ", "NV", "UT", "ID", "MT", "WY", "CO", "NM"}
US = set("AL AK AZ AR CA CO CT DE DC FL GA HI ID IL IN IA KS KY LA ME MD MA MI MN MS MO MT NE NV NH NJ NM NY NC ND OH OK OR PA RI SC SD TN TX UT VT VA WA WV WI WY PR".split())
# Ethan holds, beyond the group column. Reasons recorded per row.
ORTIZ_IDS = {"7428", "2706"}  # Ortiz group: largest decline account; Rivera (Janet)->(Celsa) shift
NAME_HOLD = ("Levitt-Weinstein", "(SCI)")  # group says Independent, name says corporate sibling
SITUATION = {"at_risk": "A", "dormant": "B", "one_and_done": "C"}


def read(name: str) -> list[dict[str, str]]:
    with (D / f"{name}.csv").open(encoding="utf-8-sig") as fh:
        return list(csv.DictReader(fh))


def days(s: str) -> int:
    return (AS_OF - date.fromisoformat(s)).days


def mon(s: str) -> str:
    return date.fromisoformat(s).strftime("%b %Y")


def plan_owners() -> dict[str, tuple[str, str]]:
    out = {}
    for r in read("fy27-owner-plan"):
        out[r["oms_funeral_home_id"]] = (r["new_owner"], r["rule"])
    return out


def route(r: dict[str, str], lst: str) -> tuple[str, str]:
    """Return (bucket, reason). bucket in rep|ethan|unrouted|partner."""
    if r["is_partner_tier"] == "True":
        return "partner", "is_partner_tier flag"
    if r["group"] not in ("Independent", ""):
        return "ethan", f"group = {r['group']} (enterprise gate)"
    if r["funeral_home_id"] in ORTIZ_IDS:
        return "ethan", "Ortiz group: largest account in decline, executive-owned"
    if any(k in r["funeral_home"] for k in NAME_HOLD):
        return "ethan", "group column says Independent but name indicates SCI/Northstar sibling"
    if r["funeral_home"].startswith("(not in account export)"):
        return "unrouted", "ID absent from account master (likely merged/deleted record)"
    if r["state"] not in US:
        return "unrouted", f"state '{r['state']}' not a US state: non-US or bad record"
    return "rep", ""


def reason(r: dict[str, str], lst: str) -> tuple[str, str]:
    if lst == "one_and_done":
        return ("C", f"Won {mon(r['first_and_only_booking'])}; booked once on {r['first_and_only_booking']}, "
                     f"nothing since ({r['days_since']} days)")
    b24, b25 = r["bookings_2024"], r["bookings_2025"]
    if lst == "dormant" or int(r["bookings_2026_to_cut"]) == 0:
        n = days(r["last_booking"])
        return ("B", f"{b24} bookings in 2024, {b25} in 2025, none in 2026; last shipped "
                     f"{r['last_booking']} ({n} days ago)")
    return ("A", f"{b24} bookings in 2024, {b25} in 2025, {r['bookings_2026_to_cut']} so far in 2026 "
                 f"({r['bookings_2026_annualised']} annualised); last shipped {r['last_booking']}")


def main() -> None:
    plan = plan_owners()
    atr, dor, one = read("accounts-at-risk-volume-decline"), read("accounts-dormant"), read("accounts-one-and-done")
    atr_ids = {r["funeral_home_id"] for r in atr}
    dor_deduped = [r for r in dor if r["funeral_home_id"] not in atr_ids]
    print(f"rows in: at_risk {len(atr)} dormant {len(dor)} (dup with at-risk {len(dor)-len(dor_deduped)}) one_and_done {len(one)}")
    lists = [("at_risk", atr), ("dormant", dor_deduped), ("one_and_done", one)]
    rows: list[dict] = []
    for lst, data in lists:
        pool = 0
        for rank, r in enumerate(data, 1):
            sit, why = reason(r, lst)
            if lst == "at_risk":
                stake = int(r["bookings_at_stake_vs_prior"])
            elif lst == "dormant":
                stake = round(float(r["bookings_lost_per_year"]))
            else:
                stake = 0
            bucket, note = route(r, lst)
            owner, rule = "", ""
            if bucket == "rep":
                if r["funeral_home_id"] in plan and plan[r["funeral_home_id"]][0]:
                    owner, rule = plan[r["funeral_home_id"]][0], "matches HubSpot owner plan"
                elif r["funeral_home_id"] in plan:
                    bucket, note = "unrouted", f"owner plan skipped it: {plan[r['funeral_home_id']][1]}"
                elif r["state"] in MIDWEST:
                    owner, rule = "Otto", "Midwest rule"
                elif r["state"] in WEST:
                    owner, rule = "Stacy", "West rule"
                else:
                    owner = "Otto" if pool % 2 == 0 else "Stacy"
                    pool += 1
                    rule = f"NE/South alternation (list pool position {pool})"
            rows.append({
                "list": lst, "list_rank": rank, "situation": sit, "bucket": bucket, "hold_reason": note,
                "rep": owner, "owner_rule": rule, "funeral_home_id": r["funeral_home_id"],
                "funeral_home": r["funeral_home"], "state": r["state"],
                "bookings_2024": r.get("bookings_2024", ""), "bookings_2025": r.get("bookings_2025", ""),
                "bookings_2026_to_10nov": r.get("bookings_2026_to_cut", ""),
                "last_booking": r.get("last_booking") or r.get("first_and_only_booking", ""),
                "bookings_per_year_at_stake": stake, "reason_to_call": why,
            })
    # call order per rep: at-risk first, then dormant, then one-and-done (most recent first)
    order = {"at_risk": 0, "dormant": 1, "one_and_done": 2}
    cap = ["call_order", *rows[0].keys(), "called_on", "outcome", "reason_code", "competitor_or_detail",
           "what_they_said", "next_action_and_date"]
    summary: dict = {}
    for rep in ("Otto", "Stacy"):
        mine = [r for r in rows if r["bucket"] == "rep" and r["rep"] == rep]
        mine.sort(key=lambda r: (order[r["list"]], r["list_rank"]))
        for i, r in enumerate(mine, 1):
            r["call_order"] = i
        write(D / f"rep-call-sheet-{rep.lower()}-2026-11.csv", cap, mine)
        summary[rep] = {k: sum(1 for r in mine if r["list"] == k) for k in order}
        summary[rep]["stake_bookings_yr"] = sum(r["bookings_per_year_at_stake"] for r in mine if r["list"] == "at_risk")
        summary[rep]["dormant_lost_bookings_yr"] = sum(r["bookings_per_year_at_stake"] for r in mine if r["list"] == "dormant")
        summary[rep]["total"] = len(mine)
    for name, b in (("ethan-held", "ethan"), ("unrouted", "unrouted")):
        sub = [r for r in rows if r["bucket"] == b]
        for i, r in enumerate(sub, 1):
            r["call_order"] = i
        write(D / f"call-sheet-{name}-2026-11.csv", cap[:cap.index("called_on")], sub)
        summary[name] = {k: sum(1 for r in sub if r["list"] == k) for k in order}
        summary[name]["stake_at_risk"] = sum(r["bookings_per_year_at_stake"] for r in sub if r["list"] == "at_risk")
        summary[name]["dormant_lost"] = sum(r["bookings_per_year_at_stake"] for r in sub if r["list"] == "dormant")
        summary[name]["total"] = len(sub)
    summary["partner_excluded"] = [r["funeral_home_id"] for r in rows if r["bucket"] == "partner"]
    summary["yield_estimate"] = YIELD
    (D / "call-sheet-summary-2026-11.json").write_text(json.dumps(summary, indent=2))
    print(json.dumps(summary, indent=1))


def write(path: Path, cols: list[str], data: list[dict]) -> None:
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(data)
    meta = {"source_files": ["accounts-at-risk-volume-decline.csv", "accounts-dormant.csv",
                             "accounts-one-and-done.csv", "fy27-owner-plan.csv"],
            "row_count": len(data), "script": "scripts/build_rep_call_sheets.py", "script_version": "1.0",
            "run_timestamp": datetime.now(timezone.utc).isoformat(),
            "privacy": "business names only; no contacts, phone, or shipment-level data"}
    path.with_suffix(".meta.json").write_text(json.dumps(meta, indent=2))
    print(f"wrote {path.name}: {len(data)} rows")


if __name__ == "__main__":
    main()
