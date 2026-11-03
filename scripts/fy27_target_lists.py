"""Build the four FY27 target lists from OMS booking history and size them.

Purpose: TASK-0021. Segment the OMS funeral home table into one-time, churned,
enterprise and net-new lists; apply the exclusion waterfall; rank each list; draw a
stratified 20-call diagnostic sample; and emit the planning figures that the bottom-up
build in reports/fy27-target-lists.md uses. READ-ONLY on every input.
Inputs:  data/raw/oms-funeral-homes-20261103.csv
         data/derived/oms-company-plan.csv (revops-crm duplicate tiering)
Outputs: data/derived/fy27-seg1-one-time.csv, fy27-seg2-churned.csv,
         fy27-seg3-enterprise.csv, fy27-seg4-net-new.csv, fy27-sample20.csv,
         fy27-target-lists-summary.json (each with a .meta.json)
Owner:   sales-lead
Date:    2026-11-03
Privacy: email, phone and street address are dropped at load; only a has_phone flag
         survives. Business name, city, state, OMS id are written. No contact person.
"""

from __future__ import annotations

import csv
import hashlib
import json
import statistics
from collections import Counter
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
OMS = ROOT / "data/raw/oms-funeral-homes-20261103.csv"
PLAN = ROOT / "data/derived/oms-company-plan.csv"
OUT = ROOT / "data/derived"
VERSION = "1.0"
AS_OF = date(2026, 11, 3)
SEED = "fy27-sample-v1"

# Dropped at load. Only has_phone is kept, derived before the column is discarded.
DROP = ("email", "phone", "address", "zip", "created_by", "updated_by")

# Partners: customers AND allies (CLAUDE.md section 5). Confirmed by revops-crm by name.
PARTNER_IDS = {"2734", "1764", "2239", "2767"}

MIDWEST = {"IL", "IN", "IA", "KS", "MI", "MN", "MO", "NE", "ND", "OH", "SD", "WI"}
WEST = {"CA", "OR", "WA", "AK", "HI", "AZ", "NV", "UT", "ID", "MT", "WY", "CO", "NM"}

ENTERPRISE_PREFIX = ("SCI", "Northstar", "Foundation Partners", "Carriage Services")


def parse_date(s: str) -> date | None:
    try:
        return date.fromisoformat(s[:10])
    except (ValueError, TypeError):
        return None


def territory(state: str, country: str) -> str:
    """Proposed routing rule. Not in force: no territory rule exists (TASK-0020)."""
    if country != "us":
        return "non-US (not routed)"
    if not state:
        return "no state"
    if state in MIDWEST:
        return "Otto (Midwest)"
    if state in WEST:
        return "Stacy (West)"
    return "Unassigned (Northeast/South)"


def load() -> list[dict[str, Any]]:
    plan_tier: dict[str, str] = {}
    with PLAN.open(encoding="utf-8-sig") as fh:
        for row in csv.DictReader(fh):
            plan_tier[row["funeral_home_id"]] = row["create_tier"]
    rows: list[dict[str, Any]] = []
    with OMS.open(encoding="utf-8-sig") as fh:
        for r in csv.DictReader(fh):
            x: dict[str, Any] = {k: v for k, v in r.items() if k not in DROP}
            x["has_phone"] = bool((r.get("phone") or "").strip())
            x["b"] = int(r["booking_count"] or 0)
            x["first"] = parse_date(r["first_booking_date"])
            x["last"] = parse_date(r["last_booking_date"])
            x["shipper"] = r["is_shipper"] == "1"
            x["dup"] = (
                r["likely_duplicate"] == "yes"
                or plan_tier.get(r["funeral_home_id"]) == "hold_duplicate"
            )
            x["partner"] = r["funeral_home_id"] in PARTNER_IDS
            x["group"] = r["funeral_home_group"]
            x["terr"] = territory(r["state"], r["country_code"])
            rows.append(x)
    return rows


def write_csv(path: Path, rows: list[dict[str, Any]], cols: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    meta = {
        "script": "scripts/fy27_target_lists.py",
        "version": VERSION,
        "run_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "as_of": AS_OF.isoformat(),
        "source": OMS.name,
        "rows_out": len(rows),
        "columns_dropped_at_load": list(DROP),
        "note": "has_phone flag only; no email, phone, address or contact person written.",
    }
    path.with_suffix(".meta.json").write_text(json.dumps(meta, indent=2) + "\n")


def h(rid: str) -> str:
    return hashlib.sha1(f"{SEED}{rid}".encode()).hexdigest()


def pct(a: int, b: int) -> float:
    return round(100 * a / b, 1) if b else 0.0


def build_model(summ: dict[str, Any]) -> dict[str, Any]:
    """Bottom-up FY27 incremental-bookings build. Every rate is an [ASSUMPTION]."""
    s1s = summ["seg1_callable_shipper_split"]["shipper"]
    s1n = summ["seg1_callable_shipper_split"]["non-shipper"]
    s2w = summ["seg2_waterfall"]
    s2_multi = s2w["of_which_lifetime_bookings_ge_2"]
    s2_single = s2w["minus_non_us"] - s2_multi
    s4a = summ["seg4_tiers"]["4A shipper account, never booked"]
    A = {  # low, base, high
        "s1_lift_shipper": (0.03, 0.08, 0.15),
        "s1_lift_nonshipper": (0.0, 0.03, 0.08),
        "s1_bookings_per_account": (1.0, 1.5, 2.0),
        "s2_react_multi": (0.03, 0.06, 0.10),
        "s2_react_single": (0.0, 0.01, 0.02),
        "s2_bookings_per_account": (1.0, 1.5, 2.0),
        "s3_sci_locations_live": (25, 100, 300),
        "s3_bookings_per_location_year": (1.0, 2.0, 2.0),
        "s3_live_fraction_of_year": (0.5, 0.5, 0.5),
        "s4a_conversion": (0.05, 0.10, 0.20),
        "s4b_worked": (1000, 2000, 3000),
        "s4b_conversion": (0.005, 0.01, 0.02),
        "s4_bookings_per_account": (1.0, 1.5, 2.0),
    }
    out: dict[str, Any] = {"assumptions": A, "scenarios": {}}
    for i, name in enumerate(("low", "base", "high")):
        a = {k: v[i] for k, v in A.items()}
        s1 = s1s * a["s1_lift_shipper"] + s1n * a["s1_lift_nonshipper"]
        s2 = s2_multi * a["s2_react_multi"] + s2_single * a["s2_react_single"]
        s3 = (
            a["s3_sci_locations_live"]
            * a["s3_bookings_per_location_year"]
            * a["s3_live_fraction_of_year"]
        )
        s4 = s4a * a["s4a_conversion"] + a["s4b_worked"] * a["s4b_conversion"]
        r = {
            "seg1_accounts": round(s1, 1),
            "seg1_bookings": round(s1 * a["s1_bookings_per_account"], 1),
            "seg2_accounts": round(s2, 1),
            "seg2_bookings": round(s2 * a["s2_bookings_per_account"], 1),
            "seg3_bookings": round(s3, 1),
            "seg4_accounts": round(s4, 1),
            "seg4_bookings": round(s4 * a["s4_bookings_per_account"], 1),
        }
        r["total_bookings"] = round(
            r["seg1_bookings"]
            + r["seg2_bookings"]
            + r["seg3_bookings"]
            + r["seg4_bookings"],
            1,
        )
        r["gap_to_556"] = round(556 - r["total_bookings"], 1)
        non_s3 = r["total_bookings"] - r["seg3_bookings"]
        per_loc = a["s3_bookings_per_location_year"] * a["s3_live_fraction_of_year"]
        r["sci_locations_live_needed_to_reach_556"] = round((556 - non_s3) / per_loc)
        r["dial_attempts_needed"] = round(
            3 * (s1s + s1n)
            + 2 * summ["seg2_waterfall"]["minus_non_us"]
            + 3 * (s4a + a["s4b_worked"])
        )
        out["scenarios"][name] = r
    out["capacity_assumption"] = {
        "dials_per_rep_per_day": 30,
        "reps": 2,
        "selling_days": 200,
        "dial_attempts_per_year": 30 * 2 * 200,
    }
    return out


def main() -> None:
    rows = load()
    print(f"rows in: {len(rows)}")
    summ: dict[str, Any] = {"as_of": AS_OF.isoformat(), "rows_in": len(rows)}
    recent_cut = AS_OF - timedelta(days=365)
    churn_cut = AS_OF - timedelta(days=730)
    fresh_cut = AS_OF - timedelta(days=14)

    # ---- data defects ----
    summ["defects"] = {
        "last_booking_after_asof": sum(
            1 for x in rows if x["last"] and x["last"] > AS_OF
        ),
        "last_booking_year_2060": [
            x["funeral_home_id"] for x in rows if x["last"] and x["last"].year >= 2030
        ],
        "first_booking_after_asof": sum(
            1 for x in rows if x["first"] and x["first"] > AS_OF
        ),
        "booked_but_no_first_date": [
            x["funeral_home_id"] for x in rows if x["b"] > 0 and not x["first"]
        ],
    }

    # ---- first-booking monthly series and shipper mix (step-change check) ----
    mon: Counter[str] = Counter()
    mon_s: Counter[str] = Counter()
    for x in rows:
        if x["b"] > 0 and x["first"] and date(2025, 1, 1) <= x["first"] <= AS_OF:
            k = x["first"].strftime("%Y-%m")
            mon[k] += 1
            mon_s[k] += x["shipper"]
    summ["first_booking_by_month"] = {
        k: {"n": mon[k], "shipper_pct": pct(mon_s[k], mon[k])} for k in sorted(mon)
    }

    # ---- Segment 1 ----
    s1_all = [
        x
        for x in rows
        if x["b"] == 1
        and x["first"]
        and x["first"] > recent_cut
        and x["first"].year < 2030
    ]
    s1_all += [x for x in rows if x["b"] == 1 and not x["first"]]
    wf1: dict[str, int] = {"segment_1_as_defined": len(s1_all)}
    s1 = [x for x in s1_all if not x["partner"]]
    wf1["minus_partners"] = len(s1)
    s1 = [x for x in s1 if not x["group"]]
    wf1["minus_enterprise_group_to_seg3"] = len(s1)
    s1 = [x for x in s1 if not x["dup"]]
    wf1["minus_likely_duplicates_held"] = len(s1)
    s1_nonus = [x for x in s1 if x["country_code"] != "us"]
    s1 = [x for x in s1 if x["country_code"] == "us"]
    wf1["minus_non_us_not_routed"] = len(s1)
    s1 = [x for x in s1 if x["first"] and x["first"] <= fresh_cut]
    wf1["minus_booked_within_14_days_or_future_dated"] = len(s1)
    s1_nophone = [x for x in s1 if not x["has_phone"]]
    wf1["of_which_no_phone_in_oms"] = len(s1_nophone)
    summ["seg1_waterfall"] = wf1
    summ["seg1_all_shipper_split"] = dict(
        Counter("shipper" if x["shipper"] else "non-shipper" for x in s1_all)
    )
    summ["seg1_all_cohort_split"] = {
        "first_booked_before_2026-06-01": sum(
            1 for x in s1_all if x["first"] and x["first"] < date(2026, 6, 1)
        ),
        "first_booked_2026-06-01_on": sum(
            1 for x in s1_all if x["first"] and x["first"] >= date(2026, 6, 1)
        ),
    }
    summ["seg1_all_cohort_shipper_split"] = {
        f"{c}|{'shipper' if s else 'non-shipper'}": sum(
            1
            for x in s1_all
            if x["first"]
            and (x["first"] < date(2026, 6, 1)) == (c == "pre-June")
            and x["shipper"] == s
        )
        for c in ("pre-June", "June-on")
        for s in (True, False)
    }
    summ["seg1_all_territory"] = dict(Counter(x["terr"] for x in s1_all))
    summ["seg1_callable_territory"] = dict(Counter(x["terr"] for x in s1))
    summ["seg1_callable_shipper_split"] = dict(
        Counter("shipper" if x["shipper"] else "non-shipper" for x in s1)
    )
    summ["seg1_callable_shipper_by_territory"] = dict(
        Counter(x["terr"] for x in s1 if x["shipper"])
    )
    summ["seg1_nonus_countries"] = dict(
        Counter(x["country_code"] for x in s1_nonus).most_common(8)
    )

    # rank: shipper-flagged first, then most recent first booking
    s1.sort(key=lambda x: (not x["shipper"], -(x["first"].toordinal())))
    for i, x in enumerate(s1, 1):
        x["call_rank"] = i
        x["cohort"] = "pre-June" if x["first"] < date(2026, 6, 1) else "June-on"
        x["tier"] = (
            "1A shipper-flagged"
            if x["shipper"]
            else "1B not shipper-flagged (hold pending sample)"
        )

    # ---- 20-call diagnostic sample ----
    def pick(pool: list[dict[str, Any]], n: int) -> list[dict[str, Any]]:
        pool = [x for x in pool if x["has_phone"]]
        return sorted(pool, key=lambda x: h(x["funeral_home_id"]))[:n]

    strata = {
        "A shipper-flagged, first booked before 2026-06-01": pick(
            [x for x in s1 if x["shipper"] and x["cohort"] == "pre-June"], 4
        ),
        "B shipper-flagged, first booked 2026-06-01 on": pick(
            [x for x in s1 if x["shipper"] and x["cohort"] == "June-on"], 8
        ),
        "C not shipper-flagged": pick([x for x in s1 if not x["shipper"]], 8),
    }
    sample: list[dict[str, Any]] = []
    for label, grp in strata.items():
        for x in grp:
            x["stratum"] = label
            sample.append(x)
    sample.sort(key=lambda x: h(x["funeral_home_id"]))
    for i, x in enumerate(sample):
        x["caller"] = "Otto" if i % 2 == 0 else "Stacy"
        x["sample20"] = "yes"
    ids = {x["funeral_home_id"] for x in sample}
    for x in s1:
        x["sample20"] = "yes" if x["funeral_home_id"] in ids else ""
    summ["sample20"] = {
        "n": len(sample),
        "by_stratum": dict(Counter(x["stratum"] for x in sample)),
        "by_caller": dict(Counter(x["caller"] for x in sample)),
        "by_territory": dict(Counter(x["terr"] for x in sample)),
    }

    # ---- repeat-rate by first-booking cohort (base-rate evidence) ----
    coh: dict[str, list[int]] = {}
    for x in rows:
        if (
            x["b"] > 0
            and x["first"]
            and 2022 <= x["first"].year <= 2026
            and x["first"] <= AS_OF
        ):
            if x["partner"] or x["group"]:
                continue
            k = (
                str(x["first"].year)
                if x["first"].year < 2026
                else f"2026-Q{(x['first'].month - 1)//3 + 1}"
            )
            coh.setdefault(k, [0, 0, 0, 0])
            coh[k][0] += 1
            coh[k][1] += x["b"] >= 2
            if x["shipper"]:
                coh[k][2] += 1
                coh[k][3] += x["b"] >= 2
    summ["repeat_rate_by_first_booking_cohort"] = {
        k: {
            "homes": v[0],
            "repeat_pct": pct(v[1], v[0]),
            "shipper_flagged_homes": v[2],
            "shipper_repeat_pct": pct(v[3], v[2]),
        }
        for k, v in sorted(coh.items())
    }

    # ---- value per returning home: bookings per year, low-volume repeat homes ----
    rates: list[float] = []
    for x in rows:
        if (
            2 <= x["b"] <= 9
            and x["first"]
            and not x["partner"]
            and not x["group"]
            and date(2022, 1, 1) <= x["first"] <= AS_OF - timedelta(days=365)
            and x["country_code"] == "us"
        ):
            yrs = max((AS_OF - x["first"]).days / 365, 1.0)
            rates.append(x["b"] / yrs)
    rates.sort()
    summ["bookings_per_year_low_volume_repeat_homes"] = {
        "n": len(rates),
        "median": round(statistics.median(rates), 2),
        "mean": round(statistics.mean(rates), 2),
        "p25": round(rates[len(rates) // 4], 2),
        "p75": round(rates[3 * len(rates) // 4], 2),
    }

    # ---- Segment 2 churned ----
    s2_all = [x for x in rows if x["b"] > 0 and x["last"] and x["last"] <= churn_cut]
    wf2: dict[str, int] = {"segment_2_as_defined": len(s2_all)}
    s2 = [x for x in s2_all if not x["partner"] and not x["group"]]
    wf2["minus_partners_and_enterprise_groups"] = len(s2)
    s2 = [x for x in s2 if not x["dup"]]
    wf2["minus_likely_duplicates"] = len(s2)
    s2 = [x for x in s2 if x["country_code"] == "us"]
    wf2["minus_non_us"] = len(s2)
    wf2["of_which_lifetime_bookings_ge_2"] = sum(1 for x in s2 if x["b"] >= 2)
    wf2["of_which_lifetime_bookings_ge_5"] = sum(1 for x in s2 if x["b"] >= 5)
    wf2["of_which_no_phone"] = sum(1 for x in s2 if not x["has_phone"])
    summ["seg2_waterfall"] = wf2
    bs = [x["b"] for x in s2_all]
    summ["seg2_stats_all"] = {
        "mean_lifetime": round(statistics.mean(bs), 2),
        "median": statistics.median(bs),
        "sum_lifetime_bookings": sum(bs),
        "max": max(bs),
    }
    summ["seg2_last_booking_year"] = dict(
        sorted(Counter(x["last"].year for x in s2_all).items())
    )
    summ["seg2_territory"] = dict(Counter(x["terr"] for x in s2))
    s2.sort(key=lambda x: (-x["b"], -x["last"].toordinal()))
    for i, x in enumerate(s2, 1):
        x["call_rank"] = i
        x["tier"] = (
            "2A 5+ bookings"
            if x["b"] >= 5
            else "2B 2-4 bookings" if x["b"] >= 2 else "2C single booking (verify-only)"
        )
    summ["seg2_tiers"] = dict(Counter(x["tier"] for x in s2))

    # ---- Segment 3 enterprise ----
    s3 = [x for x in rows if x["group"]]
    ent: dict[str, Any] = {}
    for g in sorted({x["group"] for x in s3}):
        gr = [x for x in s3 if x["group"] == g]
        bk = [x for x in gr if x["b"] > 0]
        yrs_rates = [
            x["b"] / max((AS_OF - x["first"]).days / 365, 1.0)
            for x in bk
            if x["first"] and x["first"].year < 2030
        ]
        ent[g] = {
            "mapped": len(gr),
            "ever_booked": len(bk),
            "never_booked": len(gr) - len(bk),
            "lifetime_bookings": sum(x["b"] for x in gr),
            "booked_in_last_12mo": sum(
                1 for x in bk if x["last"] and x["last"] > recent_cut
            ),
            "median_bookings_per_year_booked_locations": (
                round(statistics.median(yrs_rates), 2) if yrs_rates else None
            ),
            "duplicates_flagged": sum(x["dup"] for x in gr),
            "territory": dict(Counter(x["terr"] for x in gr)),
        }
    summ["seg3_enterprise"] = ent
    for x in s3:
        x["tier"] = f"3 {x['group']} (Ethan-gated)"
    s3.sort(key=lambda x: (x["group"], -x["b"]))
    for i, x in enumerate(s3, 1):
        x["call_rank"] = i

    # ---- Segment 4 net-new ----
    s4_all = [x for x in rows if x["b"] == 0]
    wf4: dict[str, int] = {"segment_4_as_defined": len(s4_all)}
    s4 = [x for x in s4_all if not x["group"]]
    wf4["minus_enterprise_group_records"] = len(s4)
    s4 = [x for x in s4 if not x["dup"]]
    wf4["minus_likely_duplicates"] = len(s4)
    s4_nonus = [x for x in s4 if x["country_code"] != "us"]
    s4 = [x for x in s4 if x["country_code"] == "us"]
    wf4["minus_non_us_not_routed"] = len(s4)
    wf4["of_which_no_phone"] = sum(1 for x in s4 if not x["has_phone"])
    s4 = [x for x in s4 if x["has_phone"]]
    wf4["us_callable_with_phone"] = len(s4)
    summ["seg4_waterfall"] = wf4
    summ["seg4_nonus_countries"] = dict(
        Counter(x["country_code"] for x in s4_nonus).most_common(8)
    )
    dens = Counter(
        x["state"]
        for x in rows
        if x["b"] > 0 and x["shipper"] and x["country_code"] == "us" and not x["dup"]
    )
    for x in s4:
        x["tier"] = (
            "4A shipper account, never booked"
            if x["shipper"]
            else "4B no shipper account"
        )
        x["state_customer_density"] = dens.get(x["state"], 0)
    s4.sort(
        key=lambda x: (
            not x["shipper"],
            -x["state_customer_density"],
            h(x["funeral_home_id"]),
        )
    )
    for i, x in enumerate(s4, 1):
        x["call_rank"] = i
    summ["seg4_tiers"] = dict(Counter(x["tier"] for x in s4))
    summ["seg4_territory"] = dict(Counter(x["terr"] for x in s4))
    summ["seg4_tier_by_territory"] = {
        t: dict(Counter(x["terr"] for x in s4 if x["tier"] == t))
        for t in sorted({x["tier"] for x in s4})
    }

    summ["model"] = build_model(summ)

    # ---- outputs ----
    base = [
        "call_rank",
        "tier",
        "funeral_home_id",
        "name",
        "city",
        "state",
        "country_code",
        "terr",
        "has_phone",
    ]
    write_csv(
        OUT / "fy27-seg1-one-time.csv",
        s1,
        base + ["first_booking_date", "is_shipper", "cohort", "sample20"],
    )
    write_csv(
        OUT / "fy27-seg2-churned.csv", s2, base + ["booking_count", "last_booking_date"]
    )
    write_csv(
        OUT / "fy27-seg3-enterprise.csv",
        s3,
        base + ["funeral_home_group", "booking_count", "last_booking_date"],
    )
    write_csv(
        OUT / "fy27-seg4-net-new.csv",
        s4,
        base + ["is_shipper", "state_customer_density"],
    )
    write_csv(
        OUT / "fy27-sample20.csv",
        sample,
        [
            "caller",
            "stratum",
            "funeral_home_id",
            "name",
            "city",
            "state",
            "terr",
            "first_booking_date",
            "is_shipper",
        ],
    )
    (OUT / "fy27-target-lists-summary.json").write_text(
        json.dumps(summ, indent=2, default=str) + "\n"
    )
    (OUT / "fy27-target-lists-summary.meta.json").write_text(
        json.dumps(
            {
                "script": "scripts/fy27_target_lists.py",
                "version": VERSION,
                "run_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                "source": OMS.name,
                "rows_in": len(rows),
                "columns_dropped_at_load": list(DROP),
            },
            indent=2,
        )
        + "\n"
    )
    print(json.dumps(summ, indent=1, default=str))


if __name__ == "__main__":
    main()
