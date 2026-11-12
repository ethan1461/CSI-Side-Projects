"""Build per-rep retention call sheets from the three cohort lists.

Purpose: turn data/derived/accounts-{at-risk-volume-decline,dormant,one-and-done}.csv into
         call sheets for Otto and Stacy, an unassigned pool, an Ortiz-group sheet (Cheryl / Vadim,
         to be assigned), a holding list for Ethan (Foundation Partners and other enterprise),
         and a record-repair list.
Inputs:  the three cohort CSVs and data/derived/fy27-owner-plan.csv (HubSpot owner plan).
Outputs: data/derived/rep-call-sheet-{otto,stacy}-2026-11.csv, call-sheet-unassigned-pool-2026-11.csv,
         call-sheet-ortiz-group-2026-11.csv, call-sheet-ethan-held-2026-11.csv,
         call-sheet-unrouted-2026-11.csv, call-sheet-summary-2026-11.json (+ .meta.json each).
Owner:   sales-lead. Date: 2026-11-12 (v2, after Ethan's 2026-11-12 rulings). Idempotent.
         Business names only; no contacts, no phone. Allocation and outcome tracking only: no
         bonus, incentive, commission or compensation field of any kind (CLAUDE.md s7.7).
Routing: partner flag asserted (never name-filtered). Donald's five Ortiz homes -> Ortiz sheet.
         group SCI or Northstar -> reps by territory; any other enterprise group -> Ethan.
         Territory per CLAUDE.md s5 authority 5 and fy27_owner_assignment.py.
"""

from __future__ import annotations

import csv
import json
from datetime import UTC, date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
D = ROOT / "data/derived"
AS_OF = date(2026, 11, 12)
YIELD = 1346  # 2026 average yield, CLAUDE.md s2. [ESTIMATE] wherever used.
MIDWEST = {"IL", "IN", "IA", "KS", "MI", "MN", "MO", "NE", "ND", "OH", "SD", "WI"}
WEST = {"CA", "OR", "WA", "AK", "HI", "AZ", "NV", "UT", "ID", "MT", "WY", "CO", "NM"}
US = {
    "AL",
    "AK",
    "AZ",
    "AR",
    "CA",
    "CO",
    "CT",
    "DE",
    "DC",
    "FL",
    "GA",
    "HI",
    "ID",
    "IL",
    "IN",
    "IA",
    "KS",
    "KY",
    "LA",
    "ME",
    "MD",
    "MA",
    "MI",
    "MN",
    "MS",
    "MO",
    "MT",
    "NE",
    "NV",
    "NH",
    "NJ",
    "NM",
    "NY",
    "NC",
    "ND",
    "OH",
    "OK",
    "OR",
    "PA",
    "RI",
    "SC",
    "SD",
    "TN",
    "TX",
    "UT",
    "VT",
    "VA",
    "WA",
    "WV",
    "WI",
    "WY",
    "PR",
}
OWNER_ORTIZ = "Cheryl / Vadim \u2014 to be assigned"  # Ethan 2026-11-12: not an individual, not Ethan
# Donald's five Ortiz homes (scripts/analyze_customer_cohorts.py ORTIZ_GROUP_DONALD). Only IDs present on
# the cohort lists can appear here: 7428 R.G. Ortiz (Bronx), 2706 Rivera (Janet), 2298 Ponce Funeral Home.
# Rivera (Celsa) and Ortiz (Delta Shipments Only) are in the group but on no cohort list.
ORTIZ_IDS = {"7428", "2706", "2298"}
ORTIZ_NAMES = (
    "R.G. Ortiz Funeral Home (Bronx)",
    "Rivera Funeral Home (Janet)",
    "Rivera Funeral Home (Celsa)",
    "Ponce Funeral Home",
    "Ortiz Funeral Homes (Delta Shipments Only)",
)
# Ruling 2: these two groups go to reps. Any other enterprise group stays with Ethan.
REP_GROUPS = {"SCI", "Northstar"}
# group column says Independent, name says corporate sibling. Routed as SCI/Northstar; record defect stands.
NAME_SIBLING = ("Levitt-Weinstein", "(SCI)")
ENTERPRISE_NAME_HINTS = ("Foundation Partners", "Everstory", "Carriage", "Park Lawn")
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
    """Return (bucket, reason). bucket in rep|ortiz|ethan|unrouted|partner."""
    if r["is_partner_tier"] == "True":
        return "partner", "is_partner_tier flag"
    if r["funeral_home_id"] in ORTIZ_IDS or r["funeral_home"] in ORTIZ_NAMES:
        return (
            "ortiz",
            "Ortiz group (Donald's five): Ethan ruling 2026-11-12, Cheryl / Vadim to assign",
        )
    if r["group"] in REP_GROUPS:
        return "rep", ""
    if r["group"] not in ("Independent", ""):
        return (
            "ethan",
            f"group = {r['group']} (enterprise stays with Ethan, ruling 2026-11-12)",
        )
    if any(k in r["funeral_home"] for k in ENTERPRISE_NAME_HINTS):
        return (
            "ethan",
            "group column says Independent but name indicates another enterprise group",
        )
    if r["funeral_home"].startswith("(not in account export)"):
        return (
            "unrouted",
            "ID absent from account master (likely merged/deleted record)",
        )
    if r["state"] not in US:
        return "unrouted", f"state '{r['state']}' not a US state: non-US or bad record"
    return "rep", ""


def legacy_rep(r: dict[str, str]) -> bool:
    """True if the row was on a rep sheet in the 2026-11-12 morning build (v1)."""
    if r["is_partner_tier"] == "True" or r["group"] not in ("Independent", ""):
        return False
    if r["funeral_home_id"] in {"7428", "2706"} or any(
        k in r["funeral_home"] for k in NAME_SIBLING
    ):
        return False
    return not (
        r["funeral_home"].startswith("(not in account export)") or r["state"] not in US
    )


def caution(r: dict[str, str]) -> tuple[str, str]:
    """Return (enterprise_group, flag). Flag text is a recommendation for Ethan, not a rule."""
    g, n = r["group"], r["funeral_home"]
    sibling = g in ("Independent", "") and any(k in n for k in NAME_SIBLING)
    if sibling:
        label = "SCI" if "(SCI)" in n else "SCI/Northstar (unconfirmed)"
        return label, (
            "RECORD DEFECT: group column says Independent, name indicates corporate sibling. "
            "SCI hold recommended pending Pam reply; Ethan decides"
        )
    if g == "SCI":
        return "SCI", "SCI hold recommended pending Pam reply; Ethan decides"
    if g == "Northstar":
        return (
            "Northstar",
            "Enterprise group; check with Ethan whether the SCI hold recommendation applies",
        )
    return "", ""


def reason(r: dict[str, str], lst: str) -> tuple[str, str]:
    if lst == "one_and_done":
        return (
            "C",
            (
                f"Won {mon(r['first_and_only_booking'])}; booked once on {r['first_and_only_booking']}, "
                f"nothing since ({r['days_since']} days)"
            ),
        )
    b24, b25 = r["bookings_2024"], r["bookings_2025"]
    if lst == "dormant" or int(r["bookings_2026_to_cut"]) == 0:
        n = days(r["last_booking"])
        return (
            "B",
            (
                f"{b24} bookings in 2024, {b25} in 2025, none in 2026; last shipped "
                f"{r['last_booking']} ({n} days ago)"
            ),
        )
    return (
        "A",
        (
            f"{b24} bookings in 2024, {b25} in 2025, {r['bookings_2026_to_cut']} so far in 2026 "
            f"({r['bookings_2026_annualised']} annualised); last shipped {r['last_booking']}"
        ),
    )


def main() -> None:
    plan = plan_owners()
    atr, dor, one = (
        read("accounts-at-risk-volume-decline"),
        read("accounts-dormant"),
        read("accounts-one-and-done"),
    )
    atr_ids = {r["funeral_home_id"] for r in atr}
    dor_deduped = [r for r in dor if r["funeral_home_id"] not in atr_ids]
    print(
        f"rows in: at_risk {len(atr)} dormant {len(dor)} (dup with at-risk {len(dor)-len(dor_deduped)}) one_and_done {len(one)}"
    )
    lists = [("at_risk", atr), ("dormant", dor_deduped), ("one_and_done", one)]
    rows: list[dict] = []
    for lst, data in lists:
        pool = 0  # v1 alternation counter: keeps every v1 owner unchanged (Ponce keeps its slot, then leaves)
        pool_new = (
            0  # alternation for rows newly routable under ruling 2 (SCI / Northstar)
        )
        for rank, r in enumerate(data, 1):
            sit, why = reason(r, lst)
            if lst == "at_risk":
                stake = int(r["bookings_at_stake_vs_prior"])
            elif lst == "dormant":
                stake = round(float(r["bookings_lost_per_year"]))
            else:
                stake = 0
            bucket, note = route(r, lst)
            was_v1 = legacy_rep(r)
            fid = r["funeral_home_id"]
            needs_alt = (
                fid not in plan and r["state"] not in MIDWEST and r["state"] not in WEST
            )
            slot = ""
            if (
                was_v1 and needs_alt
            ):  # consume the v1 slot even if the row has since moved (Ponce)
                slot = "Otto" if pool % 2 == 0 else "Stacy"
                pool += 1
            owner, rule = "", ""
            if bucket == "rep":
                if fid in plan and plan[fid][0]:
                    owner, rule = plan[fid][0], "matches HubSpot owner plan"
                elif fid in plan:
                    bucket, note = "unrouted", f"owner plan skipped it: {plan[fid][1]}"
                elif r["state"] in MIDWEST:
                    owner, rule = "Otto", "Midwest rule"
                elif r["state"] in WEST:
                    owner, rule = "Stacy", "West rule"
                elif was_v1:
                    owner, rule = (
                        slot,
                        f"NE/South alternation (list pool position {pool})",
                    )
                else:
                    owner = "Otto" if pool_new % 2 == 0 else "Stacy"
                    pool_new += 1
                    rule = (
                        f"NE/South alternation, enterprise rows (position {pool_new})"
                    )
            grp, flag = caution(r)
            if bucket == "ortiz":
                owner, rule = OWNER_ORTIZ, "Ethan ruling 2026-11-12"
            rows.append(
                {
                    "list": lst,
                    "list_rank": rank,
                    "situation": sit,
                    "bucket": bucket,
                    "hold_reason": note,
                    "rep": owner,
                    "owner_rule": rule,
                    "funeral_home_id": fid,
                    "funeral_home": r["funeral_home"],
                    "state": r["state"],
                    "enterprise_group": grp,
                    "flag": flag,
                    "bookings_2024": r.get("bookings_2024", ""),
                    "bookings_2025": r.get("bookings_2025", ""),
                    "bookings_2026_to_10nov": r.get("bookings_2026_to_cut", ""),
                    "last_booking": r.get("last_booking")
                    or r.get("first_and_only_booking", ""),
                    "bookings_per_year_at_stake": stake,
                    "reason_to_call": why,
                }
            )
    order = {"at_risk": 0, "dormant": 1, "one_and_done": 2}
    capture = [
        "called_on",
        "outcome",
        "reason_code",
        "competitor_or_detail",
        "what_they_said",
        "next_action_and_date",
    ]
    cap = ["call_order", *rows[0].keys(), *capture]

    def counts(sub: list[dict], key: str = "stake") -> dict:
        d = {k: sum(1 for r in sub if r["list"] == k) for k in order}
        d["at_risk_bookings_per_year"] = sum(
            r["bookings_per_year_at_stake"] for r in sub if r["list"] == "at_risk"
        )
        d["dormant_lost_bookings_per_year"] = sum(
            r["bookings_per_year_at_stake"] for r in sub if r["list"] == "dormant"
        )
        d["enterprise_rows"] = sum(1 for r in sub if r["enterprise_group"])
        d["total"] = len(sub)
        return d

    def ranked(sub: list[dict]) -> list[dict]:
        sub = sorted(sub, key=lambda r: (order[r["list"]], r["list_rank"]))
        for i, r in enumerate(sub, 1):
            r["call_order"] = i
        return sub

    summary: dict = {}
    rep_rows = [r for r in rows if r["bucket"] == "rep"]
    for rep in ("Otto", "Stacy"):
        mine = ranked([r for r in rep_rows if r["rep"] == rep])
        write(D / f"rep-call-sheet-{rep.lower()}-2026-11.csv", cap, mine)
        summary[rep] = counts(mine)
    # Unassigned pool: every rep-routable row, rep-agnostic. The rep column is blank on purpose; the
    # territory default is kept for reference and claimed_by is the one-caller-per-account ledger.
    pool_rows = ranked(
        [
            dict(
                r, rep="", default_territory_rep=r["rep"], claimed_by="", claimed_on=""
            )
            for r in rep_rows
        ]
    )
    pool_cap = [
        "call_order",
        *[c for c in rows[0] if c != "owner_rule"],
        "default_territory_rep",
        "claimed_by",
        "claimed_on",
        *capture,
    ]
    write(D / "call-sheet-unassigned-pool-2026-11.csv", pool_cap, pool_rows)
    summary["unassigned_pool"] = counts(pool_rows)
    for name, b in (
        ("ortiz-group", "ortiz"),
        ("ethan-held", "ethan"),
        ("unrouted", "unrouted"),
    ):
        sub = ranked([r for r in rows if r["bucket"] == b])
        write(D / f"call-sheet-{name}-2026-11.csv", cap[: cap.index("called_on")], sub)
        summary[name] = counts(sub)
    summary["partner_excluded"] = [
        r["funeral_home_id"] for r in rows if r["bucket"] == "partner"
    ]
    summary["enterprise_on_rep_sheets"] = {
        g: counts([r for r in rep_rows if r["enterprise_group"].startswith(g)])
        for g in ("SCI", "Northstar")
    }
    summary["yield_estimate"] = YIELD
    total = sum(
        summary[k]["total"]
        for k in ("Otto", "Stacy", "ortiz-group", "ethan-held", "unrouted")
    )
    summary["reconciliation"] = {
        "rows_on_routed_sheets": total + len(summary["partner_excluded"]),
        "rows_in_after_dedupe": len(atr) + len(dor_deduped) + len(one),
    }
    (D / "call-sheet-summary-2026-11.json").write_text(json.dumps(summary, indent=2))
    print(json.dumps(summary, indent=1))


def write(path: Path, cols: list[str], data: list[dict]) -> None:
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(data)
    meta = {
        "source_files": [
            "accounts-at-risk-volume-decline.csv",
            "accounts-dormant.csv",
            "accounts-one-and-done.csv",
            "fy27-owner-plan.csv",
        ],
        "row_count": len(data),
        "script": "scripts/build_rep_call_sheets.py",
        "script_version": "2.0",
        "run_timestamp": datetime.now(UTC).isoformat(),
        "privacy": "business names only; no contacts, phone, or shipment-level data",
        "scope": "account allocation and outcome capture only; no compensation fields",
    }
    path.with_suffix(".meta.json").write_text(json.dumps(meta, indent=2))
    print(f"wrote {path.name}: {len(data)} rows")


if __name__ == "__main__":
    main()
