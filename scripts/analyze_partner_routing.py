"""Quantify partner-routed bookings and correct the published cohort figures.

Purpose
-------
Donald challenged the headline of `reports/customer-cohort-analysis.md` on
2026-11-17: CSI cannot have won 411 new funeral homes in a year, because when CSI
books for International Mortuary Shipping (IMS) or National Mortuary Shipping (NMS)
the shipment is recorded under the *originating* funeral home's name while the
invoice goes to the partner. Such a home is partner volume, not a CSI account.

Ethan confirmed the identifying mechanism on 2026-11-18: the invoice bill-to. A
booking is partner-routed when its bill-to is a partner account and its shipping
funeral home is not that partner.

This script does three things:

1. **Reports the measured bill-to figures** supplied by the production-database
   session (`config/partner-routing-measured-20261118.json`), and derives the
   corrected new-account counts under three candidate exclusion rules.
2. **Runs the two inference methods that were used before bill-to was available**
   -- the revenue-per-booking ratio and the never-invoiced-in-QuickBooks proxy --
   against the measured truth, so the error of each is on the record.
3. **Bounds the corrections that still need per-home data**, and writes the exact
   manifest request that would close them.

It deliberately does *not* silently overwrite the published numbers. Corrections
are emitted side by side with what was published, which is what `CLAUDE.md` §8
requires of a correction.

Inputs
------
`config/partner-routing-measured-20261118.json`      measured bill-to aggregates
`data/raw/shipments-since-2022-20261110.xlsx`        one row per booking
`data/raw/sales-by-customer-summary-20261110.xlsx`   QuickBooks revenue by customer
`data/raw/oms-funeral-homes-20261109.csv`            account dimension
`--manifest PATH` (optional)                          per-home bill-to split; when
    supplied, the estimated corrections are replaced by measured ones and the
    call-sheet exclusion lists are written.

Outputs (all to `data/derived/`, each with a companion `.meta.json`)
-------------------------------------------------------------------
partner-routing-corrections.csv      published vs corrected, figure by figure
partner-routing-method-error.csv     each inference method against measured truth
partner-routing-by-year.csv          partner-routed homes and bookings by year
partner-routing-callsheet-exposure.csv   written only with --manifest

Privacy (`CLAUDE.md` §7.2)
--------------------------
The shipment export carries four columns and no decedent or family data. From the
account dimension this script reads `funeral_home_id`, `name`, `state` and
`duplicate_group_id` only; `address`, `phone`, `email`, `zip`, `created_by` and
`updated_by` are never read into memory. Funeral-home *business* names are retained
deliberately (§7.2 permits them). No output is row-level shipment data.

Owner: data-analyst
Date: 2026-11-18
Version: 1.0.0
"""

from __future__ import annotations

import argparse
import csv
import json
import logging
import re
import subprocess
from collections import Counter, defaultdict
from datetime import UTC, date, datetime
from pathlib import Path
from typing import Any

import openpyxl

LOG = logging.getLogger("partner_routing")

REPO = Path(__file__).resolve().parent.parent
CONFIG_PATH = REPO / "config" / "partner-routing-measured-20261118.json"
SHIPMENTS = REPO / "data" / "raw" / "shipments-since-2022-20261110.xlsx"
QUICKBOOKS = REPO / "data" / "raw" / "sales-by-customer-summary-20261110.xlsx"
ACCOUNTS = REPO / "data" / "raw" / "oms-funeral-homes-20261109.csv"
DERIVED = REPO / "data" / "derived"

SCRIPT_VERSION = "1.0.0"

# Columns never read from the account dimension (CLAUDE.md §7.2).
ACCOUNT_COLUMNS_DROPPED_AT_LOAD = (
    "address",
    "city",
    "country",
    "country_code",
    "created_by",
    "created_date",
    "email",
    "phone",
    "updated_by",
    "zip",
)

# QuickBooks pseudo-customers that are not customers. `TOTAL` is the report's own
# grand total sitting inside the customer rows; including it doubles every annual
# figure exactly (reports/customer-cohort-analysis.md §5).
QB_PSEUDO_CUSTOMERS = frozenset({"TOTAL", "ALREADY PAID"})

# The same trap exists on the other axis: the sheet's last column is a `Total`
# formula (`=B6+C6+...`). Read with `data_only=True` it resolves to a number and
# doubles every sum; read without it, it is a string and is skipped by accident
# rather than by design. Only true four-digit year columns are summed.
QB_YEAR_HEADER = re.compile(r"^(19|20)\d{2}$")

# CSI's 2026 realised yield, used only to invert revenue into implied bookings for
# the ratio method. CLAUDE.md §2.
YIELD_2026 = 1346.0


def normalize_name(raw: str) -> str:
    """Normalize an account name for joining across systems.

    Identical to `scripts.analyze_customer_cohorts.normalize_name`, duplicated here
    so this script does not import a 1,700-line module to use one function.
    Parentheticals are kept, because "(SCI Location #4356)" and "(SCI Location
    #7098)" are different homes and must not collapse.

    >>> normalize_name("Jorge Rivera Funeral Home, Inc.")
    'jorge rivera funeral home'
    >>> normalize_name("The Highlands Funeral Home")
    'highlands funeral home'
    """
    text = raw.lower().strip()
    text = re.sub(r"[^a-z0-9#() ]+", " ", text)
    text = re.sub(r"\b(inc|llc|ltd|corp|company|pa|p a)\b", " ", text)
    text = re.sub(r"^the\s+", "", text)
    text = re.sub(r"\s*\(\s*", " (", text)
    text = re.sub(r"\s*\)", ")", text)
    return re.sub(r"\s+", " ", text).strip()


def corrected_new_accounts(measured: dict[str, Any]) -> dict[str, int]:
    """New-account count under each candidate exclusion rule.

    Three rules are defensible and they do not agree, so all three are published
    and one is made canonical in `context/metric-definitions.md` rather than a
    single number being asserted.

        ever_billed_directly  a home counts if CSI has ever invoiced it itself
        first_booking_direct  a home counts if CSI invoiced its FIRST booking
        no_partner_booking    a home counts only if no booking of its was
                              partner-billed -- the strictest rule

    `first_booking_direct` is canonical for acquisition: "CSI won this account"
    means CSI billed the booking that opened the relationship.

    >>> corrected_new_accounts({"new_accounts_window": {
    ...     "homes": 418, "purely_partner_billed_homes": 121,
    ...     "first_booking_partner_billed_homes": 125,
    ...     "partner_billed_homes": 129}})
    {'ever_billed_directly': 297, 'first_booking_direct': 293, 'no_partner_booking': 289}
    """
    w = measured["new_accounts_window"]
    homes = int(w["homes"])
    return {
        "ever_billed_directly": homes - int(w["purely_partner_billed_homes"]),
        "first_booking_direct": homes - int(w["first_booking_partner_billed_homes"]),
        "no_partner_booking": homes - int(w["partner_billed_homes"]),
    }


def partner_rows_by_year(measured: dict[str, Any]) -> list[dict[str, object]]:
    """Partner-routed homes and bookings per calendar year, per partner and total.

    Home counts overlap across partners (38 homes used more than one partner), so
    the total row is an upper bound on distinct homes and is labelled as such.
    """
    block = measured["by_year_homes_bookings"]
    years = block["_columns"]
    partners = [k for k in block if not k.startswith("_")]
    rows: list[dict[str, object]] = []
    for idx, year in enumerate(years):
        total_homes = sum(int(block[p]["homes"][idx]) for p in partners)
        total_bookings = sum(int(block[p]["bookings"][idx]) for p in partners)
        row: dict[str, object] = {"year": year}
        for p in partners:
            row[f"{p}_homes"] = int(block[p]["homes"][idx])
            row[f"{p}_bookings"] = int(block[p]["bookings"][idx])
        row["homes_upper_bound"] = total_homes
        row["bookings_total"] = total_bookings
        rows.append(row)
    return rows


def ratio_method_error(measured: dict[str, Any], trajectory_path: Path) -> list[dict[str, object]]:
    """The revenue-per-booking inference, scored against the measured bill-to count.

    Before bill-to was available the only available handle was that IMS showed
    $727,854 of 2025 revenue against 10 recorded bookings -- 52x CSI's yield. The
    implied booking count is revenue / yield. This records how close that got, so
    the next person knows what that class of inference is worth.
    """
    if not trajectory_path.exists():
        LOG.warning("%s absent; skipping ratio-method scoring", trajectory_path)
        return []
    with trajectory_path.open() as fh:
        traj = list(csv.DictReader(fh))

    by_year = measured["by_year_homes_bookings"]
    year_idx = by_year["_columns"].index("2025")
    actual = {
        "International Mortuary Shipping": int(by_year["IMS"]["bookings"][year_idx]),
        "National Mortuary Shipping": int(by_year["NMS"]["bookings"][year_idx]),
        "Bergen Funeral Service (group)": int(by_year["Bergen"]["bookings"][year_idx]),
    }

    rows: list[dict[str, object]] = []
    for entity, actual_routed in actual.items():
        match = [r for r in traj if r["entity"] == entity and r["year"] == "2025"]
        if not match:
            continue
        revenue = float(match[0]["revenue"] or 0.0)
        recorded = int(match[0]["bookings"]) if match[0]["bookings"] else 0
        implied_total = revenue / YIELD_2026
        implied_routed = implied_total - recorded
        rows.append(
            {
                "entity": entity,
                "year": 2025,
                "revenue": round(revenue, 2),
                "bookings_under_own_record": recorded,
                "ratio_method_implied_routed": round(implied_routed),
                "measured_routed": actual_routed,
                "error_bookings": round(implied_routed - actual_routed),
                "error_pct_of_measured": (
                    round((implied_routed - actual_routed) / actual_routed * 100, 1)
                    if actual_routed
                    else None
                ),
            }
        )
    return rows


def load_accounts() -> dict[str, dict[str, str]]:
    """Account dimension, identifier columns dropped at load (CLAUDE.md §7.2)."""
    keep = ("funeral_home_id", "name", "state", "duplicate_group_id")
    out: dict[str, dict[str, str]] = {}
    with ACCOUNTS.open(newline="") as fh:
        for row in csv.DictReader(fh):
            out[row["funeral_home_id"]] = {k: row[k] for k in keep}
    LOG.info(
        "accounts loaded: %d (columns dropped at load: %s)",
        len(out),
        ", ".join(ACCOUNT_COLUMNS_DROPPED_AT_LOAD),
    )
    return out


def billed_account_ids(accounts: dict[str, dict[str, str]]) -> tuple[set[str], int, float, float]:
    """Account ids CSI has ever invoiced, per the QuickBooks customer summary.

    This is the proxy that was available before bill-to: an account that ships but
    never appears as a billed QuickBooks customer is billed to somebody else. It is
    scored against measured truth and found to over-count badly -- see
    `partner-routing-method-error.csv`. Returned alongside the join-failure count
    and revenue, which is the proxy's error term.
    """
    index: dict[str, list[str]] = defaultdict(list)
    for acct_id, acct in accounts.items():
        index[normalize_name(acct["name"])].append(acct_id)

    workbook = openpyxl.load_workbook(QUICKBOOKS, read_only=True, data_only=True)
    rows = list(workbook["Sheet1"].iter_rows(values_only=True))
    workbook.close()
    header = rows[4]
    year_columns = [i for i, h in enumerate(header) if h and QB_YEAR_HEADER.match(str(h).strip())]
    dropped = [str(h) for i, h in enumerate(header) if h and i not in year_columns]
    LOG.info(
        "quickbooks year columns: %d (%s..%s); non-year columns dropped: %s",
        len(year_columns),
        str(header[year_columns[0]]),
        str(header[year_columns[-1]]),
        ", ".join(dropped) or "none",
    )

    billed: set[str] = set()
    unjoined = 0
    unjoined_revenue = 0.0
    total_revenue = 0.0
    customers = 0
    for raw in rows[5:]:
        name = (raw[0] or "").strip()
        if not name or name.upper() in QB_PSEUDO_CUSTOMERS:
            continue
        customers += 1
        revenue = sum(
            raw[i] for i in year_columns if i < len(raw) and isinstance(raw[i], (int, float))
        )
        total_revenue += revenue
        ids = index.get(normalize_name(name), [])
        if not ids:
            unjoined += 1
            unjoined_revenue += revenue
            continue
        if revenue:
            billed.update(ids)
    LOG.info(
        "quickbooks customers: %d, joined to accounts: %d ids, unjoined names: %d "
        "carrying $%.0f of $%.0f lifetime revenue (%.2f%%)",
        customers,
        len(billed),
        unjoined,
        unjoined_revenue,
        total_revenue,
        unjoined_revenue / total_revenue * 100 if total_revenue else 0.0,
    )
    return billed, unjoined, unjoined_revenue, total_revenue


def never_invoiced_proxy(accounts: dict[str, dict[str, str]], billed: set[str]) -> dict[str, int]:
    """Score the never-invoiced proxy on the shipment export's trailing window.

    Counts homes and bookings in the 365 days to the 2026-11-10 data cut that never
    appear as a billed QuickBooks customer.
    """
    workbook = openpyxl.load_workbook(SHIPMENTS, read_only=True, data_only=True)
    sheet = workbook["Shipments"]
    rows = sheet.iter_rows(values_only=True)
    next(rows)
    window_opens = date(2025, 11, 10)
    window_closes = date(2026, 11, 10)
    volume: Counter[str] = Counter()
    total = 0
    skipped = 0
    for _booking_id, home_id, flight_date, _status in rows:
        total += 1
        if home_id is None or flight_date is None:
            skipped += 1
            continue
        day = (
            flight_date.date()
            if hasattr(flight_date, "date")
            else date.fromisoformat(str(flight_date)[:10])
        )
        if window_opens < day <= window_closes:
            volume[str(home_id)] += 1
    workbook.close()
    LOG.info("shipment rows read: %d, skipped (no home or no flight date): %d", total, skipped)

    active = list(volume)
    unbilled = [h for h in active if h not in billed]
    result = {
        "active_homes": len(active),
        "active_bookings": sum(volume.values()),
        "unbilled_homes": len(unbilled),
        "unbilled_bookings": sum(volume[h] for h in unbilled),
    }
    LOG.info(
        "trailing window: %d homes / %d bookings; never-invoiced: %d homes / %d bookings",
        result["active_homes"],
        result["active_bookings"],
        result["unbilled_homes"],
        result["unbilled_bookings"],
    )
    return result


def write_csv(path: Path, rows: list[dict[str, object]], sort_key: tuple[str, ...]) -> None:
    """Write rows sorted deterministically, so diffs between runs are meaningful."""
    if not rows:
        LOG.warning("no rows for %s; not written", path.name)
        return
    ordered = sorted(rows, key=lambda r: tuple(str(r.get(k, "")) for k in sort_key))
    with path.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(ordered)
    LOG.info("wrote %s (%d rows)", path.name, len(ordered))


def git_sha() -> str | None:
    """Current commit, or None outside a git checkout."""
    try:
        return subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=REPO, capture_output=True, text=True, check=True
        ).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def write_meta(path: Path, sources: list[str], rows_in: int, rows_out: int, note: str) -> None:
    """Companion `.meta.json` for a derived output (CLAUDE.md §8)."""
    meta = {
        "script": "scripts/analyze_partner_routing.py",
        "script_version": SCRIPT_VERSION,
        "source_files": sources,
        "rows_in": rows_in,
        "rows_out": rows_out,
        "run_timestamp_utc": datetime.now(UTC).isoformat(),
        "git_sha": git_sha(),
        "note": note,
        "privacy_note": (
            "Shipment export carries no decedent or family data (four columns). From the "
            "OMS account export only funeral_home_id, name, state and duplicate_group_id "
            "are read; identifier columns are never loaded, per CLAUDE.md §7.2. No "
            "row-level shipment data is written."
        ),
        "columns_never_read": list(ACCOUNT_COLUMNS_DROPPED_AT_LOAD),
    }
    path.write_text(json.dumps(meta, indent=2, sort_keys=True) + "\n")


def callsheet_exposure(manifest_path: Path) -> list[dict[str, object]]:
    """Which rows of each sales list are partner-routed, from a per-home manifest.

    The manifest is one row per funeral home with `funeral_home_id`,
    `self_billed_bookings` and `partner_billed_bookings`. A home is excluded from a
    rep list when it has no self-billed booking at all: CSI has no direct billing
    relationship with it, so a rep calling it is calling a partner's customer.
    """
    with manifest_path.open(newline="") as fh:
        manifest = {r["funeral_home_id"]: r for r in csv.DictReader(fh)}
    LOG.info("manifest loaded: %d homes", len(manifest))

    def purely_partner(home_id: str) -> bool:
        row = manifest.get(home_id)
        if row is None:
            return False
        return (
            int(row["partner_billed_bookings"] or 0) > 0
            and int(row["self_billed_bookings"] or 0) == 0
        )

    lists = [
        "accounts-one-and-done",
        "accounts-at-risk-volume-decline",
        "accounts-dormant",
        "rep-call-sheet-otto-2026-11",
        "rep-call-sheet-stacy-2026-11",
        "rep-call-sheet-abe-2026-11",
        "rep-call-sheet-renee-2026-11",
        "rep-call-sheet-susej-2026-11",
        "rep-call-sheet-ethan-2026-11",
    ]
    rows: list[dict[str, object]] = []
    for name in lists:
        path = DERIVED / f"{name}.csv"
        if not path.exists():
            LOG.warning("%s absent; skipped", path.name)
            continue
        with path.open(newline="") as fh:
            entries = list(csv.DictReader(fh))
        excluded = [e for e in entries if purely_partner(e["funeral_home_id"])]
        rows.append(
            {
                "list": name,
                "rows": len(entries),
                "partner_routed_rows": len(excluded),
                "partner_routed_pct": (
                    round(len(excluded) / len(entries) * 100, 1) if entries else None
                ),
                "excluded_funeral_home_ids": " ".join(
                    sorted(e["funeral_home_id"] for e in excluded)
                ),
            }
        )
        LOG.info("%s: %d of %d rows partner-routed", name, len(excluded), len(entries))
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--manifest",
        type=Path,
        default=None,
        help="per-home bill-to manifest CSV; enables the call-sheet exposure output",
    )
    parser.add_argument("--log-level", default="INFO")
    args = parser.parse_args()
    logging.basicConfig(level=args.log_level, format="%(levelname)s %(name)s: %(message)s")

    measured = json.loads(CONFIG_PATH.read_text())
    published = measured["published_figures_being_corrected"]
    window = measured["new_accounts_window"]
    DERIVED.mkdir(parents=True, exist_ok=True)

    # --- 1. corrected new-account counts, measured -------------------------------
    rules = corrected_new_accounts(measured)
    LOG.info(
        "measured new-account basis: %d homes, %d partner-billed (%.1f%%)",
        window["homes"],
        window["partner_billed_homes"],
        window["partner_billed_homes"] / window["homes"] * 100,
    )
    for rule, value in rules.items():
        LOG.info("  rule %-22s -> %d genuine new accounts", rule, value)

    corrections: list[dict[str, object]] = [
        {
            "figure": "New accounts, trailing 365 days (M-13)",
            "published": published["new_accounts"],
            "corrected": rules["first_booking_direct"],
            "basis": "MEASURED",
            "rule": "first_booking_direct",
            "note": (
                f"Measured basis is {window['homes']} homes first shipping on/after "
                f"2025-11-17 against the published {published['new_accounts']} on a window "
                "opening 2025-11-10; the 7-home difference is the window-open date, not an "
                f"error. {window['first_booking_partner_billed_homes']} had their first "
                "booking billed to a partner. Range across the three rules: "
                f"{rules['no_partner_booking']}-{rules['ever_billed_directly']}."
            ),
        },
        {
            "figure": "Bookings from new accounts, trailing 365 days",
            "published": 702,
            "corrected": int(window["bookings"]) - int(window["partner_billed_bookings"]),
            "basis": "MEASURED",
            "rule": "partner-billed bookings removed",
            "note": (
                f"{window['bookings']} bookings on the measured basis, of which "
                f"{window['partner_billed_bookings']} partner-billed. Published figure is "
                "the 411-home window."
            ),
        },
        {
            "figure": "Partner-routed share of new accounts",
            "published": 0,
            "corrected": round(int(window["partner_billed_homes"]) / int(window["homes"]) * 100, 1),
            "basis": "MEASURED",
            "rule": "percent",
            "note": (
                "Donald's estimate was 80%+. The mechanism he identified is real and "
                "measured; the magnitude is roughly a third of his estimate."
            ),
        },
    ]

    # --- 2. the inference methods, scored ----------------------------------------
    accounts = load_accounts()
    billed, unjoined, unjoined_revenue, total_revenue = billed_account_ids(accounts)
    proxy = never_invoiced_proxy(accounts, billed)

    by_year = measured["by_year_homes_bookings"]
    idx_2026 = by_year["_columns"].index("2026")
    measured_2026_bookings = sum(
        int(by_year[p]["bookings"][idx_2026]) for p in by_year if not p.startswith("_")
    )
    measured_2026_homes_ub = sum(
        int(by_year[p]["homes"][idx_2026]) for p in by_year if not p.startswith("_")
    )

    method_rows: list[dict[str, object]] = ratio_method_error(
        measured, DERIVED / "named-account-trajectory.csv"
    )
    method_rows.append(
        {
            "entity": "ALL PARTNERS (never-invoiced-in-QuickBooks proxy)",
            "year": 2026,
            "revenue": None,
            "bookings_under_own_record": None,
            "ratio_method_implied_routed": proxy["unbilled_bookings"],
            "measured_routed": measured_2026_bookings,
            "error_bookings": proxy["unbilled_bookings"] - measured_2026_bookings,
            "error_pct_of_measured": round(
                (proxy["unbilled_bookings"] - measured_2026_bookings)
                / measured_2026_bookings
                * 100,
                1,
            ),
        }
    )
    method_rows.append(
        {
            "entity": "ALL PARTNERS (never-invoiced proxy, HOMES not bookings)",
            "year": 2026,
            "revenue": None,
            "bookings_under_own_record": None,
            "ratio_method_implied_routed": proxy["unbilled_homes"],
            "measured_routed": measured_2026_homes_ub,
            "error_bookings": proxy["unbilled_homes"] - measured_2026_homes_ub,
            "error_pct_of_measured": round(
                (proxy["unbilled_homes"] - measured_2026_homes_ub) / measured_2026_homes_ub * 100,
                1,
            ),
        }
    )

    # --- 3. outputs ---------------------------------------------------------------
    year_rows = partner_rows_by_year(measured)

    write_csv(DERIVED / "partner-routing-corrections.csv", corrections, ("figure",))
    write_meta(
        DERIVED / "partner-routing-corrections.meta.json",
        [str(CONFIG_PATH.relative_to(REPO))],
        rows_in=len(published),
        rows_out=len(corrections),
        note=(
            "Published versus corrected cohort figures. Only rows marked basis=MEASURED "
            "rest on the bill-to join; everything else in the report that depends on "
            "per-home bill-to is labelled [ESTIMATE] and needs the manifest."
        ),
    )

    write_csv(DERIVED / "partner-routing-method-error.csv", method_rows, ("entity",))
    write_meta(
        DERIVED / "partner-routing-method-error.meta.json",
        [
            str(CONFIG_PATH.relative_to(REPO)),
            "data/derived/named-account-trajectory.csv",
            "data/raw/sales-by-customer-summary-20261110.xlsx",
            "data/raw/shipments-since-2022-20261110.xlsx",
            "data/raw/oms-funeral-homes-20261109.csv",
        ],
        rows_in=proxy["active_homes"],
        rows_out=len(method_rows),
        note=(
            "Each pre-bill-to inference method scored against the measured bill-to count. "
            f"The never-invoiced proxy's error term is {unjoined} QuickBooks customer names "
            f"that do not join to any account record, carrying ${unjoined_revenue:,.0f} of "
            f"${total_revenue:,.0f} lifetime revenue."
        ),
    )

    write_csv(DERIVED / "partner-routing-by-year.csv", year_rows, ("year",))
    write_meta(
        DERIVED / "partner-routing-by-year.meta.json",
        [str(CONFIG_PATH.relative_to(REPO))],
        rows_in=int(measured["all_partner_billed_2022_2026"]["bookings"]),
        rows_out=len(year_rows),
        note=(
            "Partner-routed homes and bookings by calendar year. homes_upper_bound sums "
            "per-partner home counts, which overlap: 38 homes used more than one partner "
            "across the full history, so distinct homes per year is lower."
        ),
    )

    if args.manifest:
        exposure = callsheet_exposure(args.manifest)
        write_csv(DERIVED / "partner-routing-callsheet-exposure.csv", exposure, ("list",))
        write_meta(
            DERIVED / "partner-routing-callsheet-exposure.meta.json",
            [str(args.manifest), "data/derived/*.csv (sales lists)"],
            rows_in=sum(int(r["rows"]) for r in exposure),
            rows_out=len(exposure),
            note=(
                "Rows on each sales list whose funeral home has no self-billed booking. "
                "These must come off the rep sheets: a rep calling one is calling a "
                "partner's customer."
            ),
        )
    else:
        LOG.warning(
            "no --manifest supplied: call-sheet exposure NOT computed. The 302 one-and-done "
            "and 48 at-risk rows cannot be cleared for calling until it is. See the "
            "manifest request in reports/customer-cohort-analysis.md."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
