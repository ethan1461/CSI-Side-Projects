"""Build the retention call sheets: one account, one named caller, no row on two sheets (v3).

Purpose: partition the accounts on data/derived/accounts-{at-risk-volume-decline,dormant,one-and-done}.csv
         across the six named callers, plus an Ortiz sheet (Cheryl / Vadim, to be assigned), a record-repair
         list and the partner-tier exclusions. Every source account lands in exactly one place; the script
         asserts it and writes a per-account reconciliation file.
Inputs:  the three cohort CSVs and data/derived/fy27-owner-plan.csv (HubSpot owner plan).
Outputs: data/derived/rep-call-sheet-{otto,stacy,ethan,abe,renee,susej}-2026-11.csv,
         call-sheet-ortiz-group-2026-11.csv, call-sheet-unrouted-2026-11.csv,
         call-sheet-reconciliation-2026-11.csv, call-sheet-summary-2026-11.json (+ .meta.json each).
Owner:   sales-lead. Date: 2026-11-12 (v3, after Ethan's second 2026-11-12 ruling). Idempotent.
         Business names only; no contacts, no phone. Allocation and outcome tracking only: no
         bonus, incentive, commission or compensation field of any kind (CLAUDE.md s7.7).
Callers: Ethan, Otto, Stacy confirmed. Susej, Renee, Abe PROVISIONAL (Ethan: "maybe"); their sheets stay
         unreleased until Vadim has seen the volume (recommendation, Ethan decides).
Routing: partner flag asserted (never name-filtered). Ortiz five -> Ortiz sheet. Other enterprise
         (Foundation Partners) -> Ethan. SCI -> stays on its v2 sheet, flagged HELD. Northstar released.
         Otto and Stacy keep every v2 account except the one-and-done tail beyond KEEP_TAIL rows
         (unreached before Dec 11); that tail goes round-robin to the provisional callers.
         Use --no-provisional to return the tail to Otto and Stacy (a rebuild, not a hand edit).
"""

from __future__ import annotations

import argparse
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
# The five Ortiz entities named for the cohort revenue grouping (scripts/analyze_customer_cohorts.py
# ORTIZ_GROUP_DONALD). Naming them was a grouping exercise; nobody named is a caller. Only IDs present on
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
# These two groups route to reps (Northstar = a funeral home group like SCI, confirmed by Ethan 2026-11-12).
# Any other enterprise group stays with Ethan.
REP_GROUPS = {"SCI", "Northstar"}
# group column says Independent, name says corporate sibling. Routed as SCI/Northstar; record defect stands.
NAME_SIBLING = ("Levitt-Weinstein", "(SCI)")
ENTERPRISE_NAME_HINTS = ("Foundation Partners", "Everstory", "Carriage", "Park Lawn")
SITUATION = {"at_risk": "A", "dormant": "B", "one_and_done": "C"}
KEEP_TAIL = 80  # one-and-done rows per sheet Otto/Stacy keep (about 40 a week, weeks of Nov 30 and Dec 7)
PROVISIONAL = (
    "Abe",
    "Renee",
    "Susej",
)  # alphabetical: neutral, no judgement about a person
CONFIRMED = {"Ethan", "Otto", "Stacy"}
HELD = "HELD \u2014 awaiting SCI corporate"
STATUS_CONFIRMED = "CONFIRMED"
STATUS_PROVISIONAL = "PROVISIONAL \u2014 not yet confirmed"
PALM_NOTE = (
    "PALM MORTUARY (Las Vegas): do not release with the other SCI rows when Pam replies. "
    "Check Stacy's separate conversation with Phoebe first (Ethan, 2026-11-12)"
)
STALE = (
    "call-sheet-unassigned-pool-2026-11",
    "call-sheet-ethan-held-2026-11",
)


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
            "Ortiz group (five entities named for the cohort revenue grouping): Ethan ruling 2026-11-12, Cheryl / Vadim to assign",
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


def caution(r: dict[str, str]) -> tuple[str, str, bool]:
    """Return (enterprise_group, flag, held). SCI rows are held; Northstar is released by Ethan."""
    g, n = r["group"], r["funeral_home"]
    sibling = g in ("Independent", "") and any(k in n for k in NAME_SIBLING)
    if sibling:
        label = "SCI" if "(SCI)" in n else "SCI/Northstar (unconfirmed)"
        return (
            label,
            (
                "RECORD DEFECT: group column says Independent, name indicates corporate sibling. "
                "Held by default while the parent is unconfirmed; revops to resolve from the record"
            ),
            True,
        )
    if g == "SCI":
        return "SCI", "SCI location. Do not call until the hold is released", True
    if g == "Northstar":
        return "Northstar", "Northstar location. Released by Ethan 2026-11-12", False
    return "", "", False


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


def build_rows(
    lists: list[tuple[str, list[dict[str, str]]]], plan: dict[str, tuple[str, str]]
) -> list[dict]:
    """Route every source row once. Otto/Stacy owners reproduce v2 exactly (no reshuffle)."""
    rows: list[dict] = []
    for lst, data in lists:
        pool = 0  # v1 alternation counter: keeps every v1 owner unchanged
        pool_new = (
            0  # alternation for rows routable only since ruling 2 (SCI / Northstar)
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
            if was_v1 and needs_alt:
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
            grp, flag, held = caution(r)
            if bucket == "ortiz":
                owner, rule = OWNER_ORTIZ, "Ethan ruling 2026-11-12"
            if bucket == "ethan":
                owner, rule = "Ethan", "enterprise stays with Ethan (ruling 2026-11-12)"
            palm = "Palm Mortuary & Cemetery (SCI" in r["funeral_home"]
            if palm:
                flag = f"{flag}. {PALM_NOTE}"
            rows.append(
                {
                    "list": lst,
                    "list_rank": rank,
                    "situation": sit,
                    "bucket": bucket,
                    "hold_reason": note,
                    "rep": owner,
                    "territory_rep": owner,
                    "owner_rule": rule,
                    "caller_status": "",
                    "call_status": HELD if (held and bucket == "rep") else "",
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
    return rows


ORDER = {"at_risk": 0, "dormant": 1, "one_and_done": 2}


def sort_key(r: dict) -> tuple[int, int]:
    return (ORDER[r["list"]], r["list_rank"])


def carve_tail(rows: list[dict]) -> list[dict]:
    """Move the unreached one-and-done tail off Otto/Stacy to the provisional callers.

    Rule (mechanical): per territory sheet in call order, the first KEEP_TAIL one-and-done rows stay;
    later released rows go round-robin to Abe, Renee, Susej (one counter across both sheets, Otto's
    carved rows first). Held SCI rows never move. Returns the carved rows.
    """
    carved: list[dict] = []
    for rep in ("Otto", "Stacy"):
        mine = sorted(
            (r for r in rows if r["bucket"] == "rep" and r["rep"] == rep), key=sort_key
        )
        tail = [r for r in mine if r["list"] == "one_and_done"]
        carved += [r for r in tail[KEEP_TAIL:] if not r["call_status"]]
    for i, r in enumerate(carved):
        r["rep"] = PROVISIONAL[i % len(PROVISIONAL)]
        r["owner_rule"] = (
            f"round-robin from {r['territory_rep']}'s one-and-done tail (position {i + 1})"
        )
    return carved


def counts(sub: list[dict]) -> dict:
    d = {k: sum(1 for r in sub if r["list"] == k) for k in ORDER}
    d["at_risk_bookings_per_year"] = sum(
        r["bookings_per_year_at_stake"] for r in sub if r["list"] == "at_risk"
    )
    d["dormant_lost_bookings_per_year"] = sum(
        r["bookings_per_year_at_stake"] for r in sub if r["list"] == "dormant"
    )
    d["held_sci"] = sum(1 for r in sub if r["call_status"])
    d["northstar_released"] = sum(
        1 for r in sub if r["enterprise_group"] == "Northstar"
    )
    d["callable_now"] = len(sub) - d["held_sci"]
    d["total"] = len(sub)
    return d


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument(
        "--no-provisional",
        action="store_true",
        help="keep the one-and-done tail with Otto and Stacy; provisional sheets are written empty",
    )
    args = ap.parse_args()
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
    rows = build_rows(
        [("at_risk", atr), ("dormant", dor_deduped), ("one_and_done", one)], plan
    )
    ids = [r["funeral_home_id"] for r in rows]
    if len(ids) != len(set(ids)):
        dupes = sorted({i for i in ids if ids.count(i) > 1})
        raise SystemExit(f"account appears on two source lists after dedupe: {dupes}")
    palm = [r for r in rows if "Palm Mortuary & Cemetery (SCI" in r["funeral_home"]]
    if len(palm) != 1 or palm[0]["state"] != "NV" or not palm[0]["call_status"]:
        raise SystemExit(
            "Palm Mortuary & Cemetery (Las Vegas) must match exactly one held row"
        )
    carved = [] if args.no_provisional else carve_tail(rows)

    # Assign sheet, status and call order. A row's sheet is its single destination.
    for r in rows:
        if r["bucket"] == "rep":
            r["sheet"] = r["rep"]
        elif r["bucket"] == "ethan":
            r["sheet"] = "Ethan"
        elif r["bucket"] == "ortiz":
            r["sheet"] = "Ortiz group"
        elif r["bucket"] == "unrouted":
            r["sheet"] = "Record repair"
        else:
            r["sheet"] = "Partner tier (excluded)"
        r["caller_status"] = (
            STATUS_PROVISIONAL
            if r["sheet"] in PROVISIONAL
            else STATUS_CONFIRMED if r["sheet"] in CONFIRMED else ""
        )
    capture = [
        "called_on",
        "outcome",
        "reason_code",
        "competitor_or_detail",
        "what_they_said",
        "next_action_and_date",
    ]
    base = [
        "list",
        "list_rank",
        "situation",
        "bucket",
        "hold_reason",
        "rep",
        "territory_rep",
        "owner_rule",
        "caller_status",
        "call_status",
        "funeral_home_id",
        "funeral_home",
        "state",
        "enterprise_group",
        "flag",
        "bookings_2024",
        "bookings_2025",
        "bookings_2026_to_10nov",
        "last_booking",
        "bookings_per_year_at_stake",
        "reason_to_call",
    ]
    cap = ["call_order", *base, *capture]
    summary: dict = {"script_version": "3.0", "provisional_released": False}
    sheets = {}
    for name in ("Otto", "Stacy", "Ethan", *PROVISIONAL):
        # Released rows first (in list order), held rows last, so a rep never starts on a held row.
        sub = sorted(
            (r for r in rows if r["sheet"] == name),
            key=lambda r: (bool(r["call_status"]), *sort_key(r)),
        )
        for i, r in enumerate(sub, 1):
            r["call_order"] = i
        sheets[name] = sub
        write(D / f"rep-call-sheet-{name.lower()}-2026-11.csv", cap, sub)
        summary[name] = counts(sub)
        summary[name]["caller_status"] = (
            STATUS_PROVISIONAL if name in PROVISIONAL else STATUS_CONFIRMED
        )
    for name, sheet in (("ortiz-group", "Ortiz group"), ("unrouted", "Record repair")):
        sub = sorted((r for r in rows if r["sheet"] == sheet), key=sort_key)
        for i, r in enumerate(sub, 1):
            r["call_order"] = i
        write(D / f"call-sheet-{name}-2026-11.csv", cap[: cap.index("called_on")], sub)
        summary[name] = counts(sub)
    partner = [r for r in rows if r["bucket"] == "partner"]
    summary["partner_excluded"] = [r["funeral_home_id"] for r in partner]

    # Partition reconciliation: every source account lands in exactly one place.
    src = {"at_risk": len(atr), "dormant": len(dor_deduped), "one_and_done": len(one)}
    placed: dict[str, dict[str, int]] = {k: {} for k in src}
    for r in rows:
        placed[r["list"]][r["sheet"]] = placed[r["list"]].get(r["sheet"], 0) + 1
    for k, n_in in src.items():
        if sum(placed[k].values()) != n_in:
            raise SystemExit(
                f"row loss in {k}: {n_in} in, {sum(placed[k].values())} placed"
            )
    recon_cols = ["funeral_home_id", "funeral_home", "list", "sheet", "call_status"]
    write(
        D / "call-sheet-reconciliation-2026-11.csv",
        recon_cols,
        sorted(rows, key=sort_key),
    )
    summary["reconciliation"] = {
        "dormant_rows_also_on_at_risk_removed": len(dor) - len(dor_deduped),
        "source_accounts": sum(src.values()),
        "placed_by_source_list": placed,
        "sheet_totals": {
            s: sum(p.get(s, 0) for p in placed.values())
            for s in sorted({r["sheet"] for r in rows})
        },
        "carved_to_provisional": len(carved),
    }
    summary["checks"] = verify_on_disk(sum(src.values()))
    top10 = {}
    for name in ("Otto", "Stacy"):
        top10[name] = [
            (
                r["call_order"],
                r["funeral_home"],
                r["state"],
                r["reason_to_call"],
                r["enterprise_group"],
            )
            for r in sheets[name]
            if not r["call_status"]
        ][:10]
    summary["top10_callable"] = top10
    summary["yield_estimate"] = YIELD
    (D / "call-sheet-summary-2026-11.json").write_text(json.dumps(summary, indent=2))
    for s in STALE:
        for ext in (".csv", ".meta.json"):
            f = D / f"{s}{ext}"
            if f.exists():
                f.unlink()
                print(f"removed superseded {f.name}")
    print(
        json.dumps(
            {k: v for k, v in summary.items() if k != "top10_callable"}, indent=1
        )
    )


def verify_on_disk(expected: int) -> dict:
    """Re-read the written sheets: no account id on two sheets, none missing."""
    seen: dict[str, str] = {}
    files = sorted(D.glob("rep-call-sheet-*-2026-11.csv")) + [
        D / "call-sheet-ortiz-group-2026-11.csv",
        D / "call-sheet-unrouted-2026-11.csv",
    ]
    for f in files:
        with f.open(encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                fid = row["funeral_home_id"]
                if fid in seen:
                    raise SystemExit(
                        f"account {fid} on two sheets: {seen[fid]} and {f.name}"
                    )
                seen[fid] = f.name
    with (D / "call-sheet-reconciliation-2026-11.csv").open(encoding="utf-8") as fh:
        recon = list(csv.DictReader(fh))
    partner = {r["funeral_home_id"] for r in recon if r["sheet"].startswith("Partner")}
    if len(seen) + len(partner) != expected:
        raise SystemExit(
            f"{len(seen)} on sheets + {len(partner)} partner != {expected} source"
        )
    return {
        "accounts_on_sheets": len(seen),
        "partner_excluded": len(partner),
        "duplicates_across_sheets": 0,
        "source_accounts": expected,
    }


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
        "script_version": "3.0",
        "run_timestamp": datetime.now(UTC).isoformat(),
        "privacy": "business names only; no contacts, phone, or shipment-level data",
        "scope": "account allocation and outcome capture only; no compensation fields",
    }
    path.with_suffix(".meta.json").write_text(json.dumps(meta, indent=2))
    print(f"wrote {path.name}: {len(data)} rows")


if __name__ == "__main__":
    main()
