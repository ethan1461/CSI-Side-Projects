"""Customer cohort, churn, acquisition and concentration analysis.

Purpose
-------
Answer the question CSI has never been able to answer: **is flat volume a retention
problem or a new-client problem?** Produces the yearly account cohort decomposition
(acquisition / reactivation / same-account frequency / churn), first-to-second-booking
conversion, revenue concentration 2016-2026, and the named-account trajectories
(Bergen, Ortiz group, partner tier, corporate groups) needed to test Donald's
hypothesis.

Also reconciles the two independent sources for the first time (`CLAUDE.md` §6).

Inputs
------
`data/raw/shipments-since-2022-20261110.xlsx`        sheet `Shipments`, one row per booking
`data/raw/sales-by-customer-summary-20261110.xlsx`   QuickBooks accrued revenue by customer by year
`data/raw/oms-funeral-homes-20261109.csv`            account dimension: id -> business name, group

Outputs (all to `data/derived/`, each with a companion `.meta.json`)
------------------------------------------------------------------
cohort-shipment-data-quality.csv     attribution and field completeness by year
cohort-yearly-accounts.csv           the four-term volume decomposition, full-year and like-for-like
cohort-retention-matrix.csv          accounts and bookings retained by cohort year x year offset
cohort-first-to-second.csv           first-to-second booking conversion by cohort year
revenue-concentration-by-year.csv    top-N revenue share and HHI, 2016-2026
revenue-customer-churn-by-year.csv   revenue-based acquisition and churn, 2017-2026
partner-tier-revenue-share.csv       partner tier and family-group share of revenue by year
named-account-trajectory.csv         Bergen / Ortiz / partner tier / corporate groups by year
base-decay-by-size-band.csv          how the 2023 customer base has decayed, by account size
qb-oms-revenue-reconciliation.csv    QuickBooks vs OMS analytics revenue by year
cohort-join-quality.csv              name-join coverage diagnostics

Sales-actionable lists (business names only, no individual contacts)
-------------------------------------------------------------------
accounts-at-risk-volume-decline.csv  established accounts whose volume has collapsed
accounts-dormant.csv                 accounts with real volume in 2024-25 and none in 2026
accounts-one-and-done.csv            accounts won since 2025 that never placed a second booking

Privacy (`CLAUDE.md` §7.2)
--------------------------
The shipment export carries four columns and no decedent or family data. The OMS
account export carries contact PII: `address`, `phone`, `email`, `created_by` and
`updated_by` are dropped **at load** and never held in memory. Funeral-home
*business* names are retained deliberately (§7.2 permits them). Dropped columns are
recorded in every `.meta.json`. No output is ever row-level shipment data.

Known limits
------------
* The shipment export begins 2022-01-02 but the legacy system was still being
  adopted through mid-2022 (9 bookings in January 2022, 896 in December). Any
  "first-ever booking" before ~2022-08 is left-censored, so the 2023 new-account
  cohort is inflated and 2022 cannot show churn at all. 2024 is the first year in
  which "new account" is trustworthy.
* 2026 is complete only to 2026-11-10. Full-year columns for 2026 are therefore
  partial; use the like-for-like (Jan-Oct) columns for any 2026 comparison.
* QuickBooks is accrued revenue by invoice date; the shipment file is counted on
  flight date. Annual totals agree to within 1% but a given booking may fall in a
  different year in each source.

Owner: data-analyst
Date: 2026-11-12
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
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path

import openpyxl

VERSION = "1.0.0"
SCRIPT_PATH = "scripts/analyze_customer_cohorts.py"

LOG = logging.getLogger("cohorts")

# --- source configuration ---------------------------------------------------

DEFAULT_SHIPMENTS = Path("data/raw/shipments-since-2022-20261110.xlsx")
DEFAULT_REVENUE = Path("data/raw/sales-by-customer-summary-20261110.xlsx")
DEFAULT_ACCOUNTS = Path("data/raw/oms-funeral-homes-20261109.csv")
DEFAULT_OUT = Path("data/derived")

# QuickBooks header is on row 5 (1-indexed); rows 1-4 are report title rows.
QB_HEADER_ROW = 5

# Pseudo-customers in the QuickBooks export that are not customers.
# "TOTAL" is the report's own grand-total row, sitting inside the customer list.
# Including it doubles every annual figure -- this is the entire reason the two
# systems appeared not to reconcile.
QB_NON_CUSTOMERS: frozenset[str] = frozenset({"TOTAL", "ALREADY PAID"})

# Columns kept from the OMS account export. Everything else is dropped at load.
ACCOUNT_KEEP: frozenset[str] = frozenset(
    {
        "funeral_home_id",
        "name",
        "state",
        "country_code",
        "funeral_home_group",
        "duplicate_group_id",
    }
)

# The data cut: last date the sources can be trusted to be complete.
DATA_CUT = date(2026, 11, 10)

# Like-for-like window. 2026 is complete only to 2026-11-10, so every year is
# compared on 1 January - 31 October.
LLF_LAST_MONTH = 10

# Plausible flight-date range. Anything outside is a data-entry defect.
MIN_YEAR, MAX_YEAR = 2022, 2026

# --- Donald's groupings (his explicit instruction, 2026-11-10) --------------

BERGEN_GROUP: tuple[str, ...] = (
    "Bergen Funeral Service (Florida)",
    "Bergen Funeral Service (New Jersey)",
)

# The five Donald named. Primary grouping.
ORTIZ_GROUP_DONALD: tuple[str, ...] = (
    "Ortiz Funeral Homes (Delta Shipments Only)",
    "R.G. Ortiz Funeral Home (Bronx)",
    "Rivera Funeral Home (Janet)",
    "Rivera Funeral Home (Celsa)",
    "Ponce Funeral Home",
)

# Names that look like the same family of homes but which Donald did not name.
# Reported as a sensitivity, never folded into the primary figure.
ORTIZ_GROUP_EXTENDED_EXTRA: tuple[str, ...] = (
    "Ortiz Funeral Homes (Viva Shipments Only)",
    "R.G. Ortiz Funeral Home",
    "Magano Funeral Home (Ortiz)",
    "Rivera Funeral Home (Bathgate)",
)

# Partner tier, `CLAUDE.md` §5 and §7.1 standing authority 1. Customers *and*
# partners: their trajectory is a relationship outcome, not only a sales one.
PARTNER_MARKERS: tuple[str, ...] = (
    "bergen funeral service",
    "national mortuary shipping",
    "international mortuary shipping",
    "las rosas",
    "dunn & sons",
    "karen c funeral",
)

# Corporate groups, identified from the account name or the OMS group field.
GROUP_PATTERNS: tuple[tuple[str, str], ...] = (
    ("SCI", r"sci location"),
    ("Foundation Partners", r"foundation partners"),
    ("Northstar", r"northstar"),
    ("Carriage Services", r"carriage"),
)

CURVE_POINTS: tuple[int, ...] = (1, 5, 10, 25, 50, 100)


# --- small, testable primitives --------------------------------------------


@dataclass(frozen=True)
class Booking:
    """One booking, reduced to what cohort analysis needs."""

    booking_id: int
    account_id: str
    flight_date: date
    status: str


@dataclass(frozen=True)
class Account:
    """One funeral-home account, business fields only."""

    account_id: str
    name: str
    state: str
    group: str
    duplicate_group_id: str


def normalize_name(raw: str) -> str:
    """Normalize an account name for joining across systems.

    Case, punctuation, corporate suffixes and a leading article are removed.
    Parentheticals and location numbers are **kept**, because
    "Kraeer Funeral Home (SCI Location #4356)" and "(SCI Location #7098)" are
    different homes and must not collapse.

    >>> normalize_name("Jorge Rivera Funeral Home, Inc.")
    'jorge rivera funeral home'
    >>> normalize_name("The Highlands Funeral Home")
    'highlands funeral home'
    >>> normalize_name("Kraeer Funeral Home (SCI Location #4356)")
    'kraeer funeral home (sci location #4356)'
    """
    text = raw.lower().strip()
    text = re.sub(r"[^a-z0-9#() ]+", " ", text)
    text = re.sub(r"\b(inc|llc|ltd|corp|company|pa|p a)\b", " ", text)
    text = re.sub(r"^the\s+", "", text)
    text = re.sub(r"\s*\(\s*", " (", text)
    text = re.sub(r"\s*\)", ")", text)
    return re.sub(r"\s+", " ", text).strip()


def is_partner(name: str) -> bool:
    """True when the account is a named strategic partner (`CLAUDE.md` §5)."""
    lowered = name.lower()
    return any(marker in lowered for marker in PARTNER_MARKERS)


def corporate_group(name: str, oms_group: str) -> str:
    """Corporate group for an account, from the OMS field or the name.

    >>> corporate_group("Forest Lawn (SCI Location #4365)", "")
    'SCI'
    >>> corporate_group("ACCENT FUNERAL HOME (Foundation Partners)", "")
    'Foundation Partners'
    >>> corporate_group("Smith Funeral Home", "")
    'Independent'
    """
    if oms_group.strip():
        return oms_group.strip()
    lowered = name.lower()
    for label, pattern in GROUP_PATTERNS:
        if re.search(pattern, lowered):
            return label
    return "Independent"


def parse_flight_date(value: object) -> date | None:
    """Parse the export's flight date. Blank and unparseable both yield None."""
    if value is None:
        return None
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    text = str(value).strip()
    if not text:
        return None
    try:
        return datetime.strptime(text[:10], "%Y-%m-%d").date()
    except ValueError:
        return None


def top_n_share(values: list[float], n: int) -> float:
    """Share of total held by the largest `n` values.

    >>> round(top_n_share([50.0, 30.0, 20.0], 1), 4)
    0.5
    >>> round(top_n_share([50.0, 30.0, 20.0], 2), 4)
    0.8
    >>> top_n_share([], 3)
    0.0
    """
    total = sum(values)
    if total <= 0:
        return 0.0
    return sum(sorted(values, reverse=True)[:n]) / total


def hhi(values: list[float]) -> float:
    """Herfindahl-Hirschman index of a revenue distribution, 0-10000.

    >>> hhi([100.0])
    10000.0
    >>> hhi([50.0, 50.0])
    5000.0
    """
    total = sum(values)
    if total <= 0:
        return 0.0
    return sum((v / total) ** 2 for v in values) * 10000.0


# --- loaders ----------------------------------------------------------------


def load_accounts(source: Path) -> tuple[dict[str, Account], int, list[str]]:
    """Load the account dimension, dropping identifier columns at load."""
    accounts: dict[str, Account] = {}
    rows_in = 0
    with source.open(newline="", encoding="utf-8-sig", errors="replace") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise ValueError(f"{source} has no header row")
        dropped = sorted(set(reader.fieldnames) - ACCOUNT_KEEP)
        for raw in reader:
            rows_in += 1
            account_id = (raw.get("funeral_home_id") or "").strip()
            if not account_id:
                continue
            name = (raw.get("name") or "").strip()
            accounts[account_id] = Account(
                account_id=account_id,
                name=name,
                state=(raw.get("state") or "").strip(),
                group=corporate_group(name, raw.get("funeral_home_group") or ""),
                duplicate_group_id=(raw.get("duplicate_group_id") or "").strip(),
            )
    LOG.info("accounts: rows_in=%d accounts_out=%d dropped=%s", rows_in, len(accounts), dropped)
    return accounts, rows_in, dropped


def load_bookings(source: Path) -> tuple[list[Booking], dict[str, int]]:
    """Load the shipment export and partition rows into usable and not.

    Returns the usable bookings and a counter of every exclusion reason, so that
    row loss is explained in the log rather than in anyone's head (`CLAUDE.md` §8).
    """
    workbook = openpyxl.load_workbook(source, read_only=True, data_only=True)
    try:
        sheet = workbook["Shipments"]
        rows = sheet.iter_rows(values_only=True)
        header = next(rows)
        expected = ("booking_id", "shipping_funeral_home_id", "flight_date", "status")
        if tuple(str(c) for c in header[:4]) != expected:
            raise ValueError(f"{source} header is {header[:4]}, expected {expected}")

        bookings: list[Booking] = []
        tally: Counter[str] = Counter()
        seen: set[int] = set()
        for raw in rows:
            tally["rows_in"] += 1
            booking_id = raw[0]
            if booking_id is None:
                tally["excluded_no_booking_id"] += 1
                continue
            booking_id = int(booking_id)
            if booking_id in seen:
                tally["excluded_duplicate_booking_id"] += 1
                continue
            seen.add(booking_id)

            account_id = "" if raw[1] is None else str(raw[1]).strip()
            flight = parse_flight_date(raw[2])
            status = ("" if raw[3] is None else str(raw[3])).strip()

            if not account_id:
                tally["excluded_no_funeral_home"] += 1
                continue
            if flight is None:
                tally["excluded_no_flight_date"] += 1
                continue
            if not (MIN_YEAR <= flight.year <= MAX_YEAR):
                tally["excluded_impossible_flight_date"] += 1
                continue
            if flight > DATA_CUT:
                tally["excluded_after_data_cut"] += 1
                continue
            bookings.append(Booking(booking_id, account_id, flight, status))
            tally["rows_out"] += 1
    finally:
        workbook.close()

    LOG.info("bookings: %s", dict(sorted(tally.items())))
    return bookings, dict(tally)


def load_revenue(source: Path) -> tuple[dict[str, dict[int, float]], dict[str, int]]:
    """Load QuickBooks annual revenue per customer.

    The report's own `TOTAL` row sits inside the customer list and is excluded;
    leaving it in doubles every annual figure.
    """
    workbook = openpyxl.load_workbook(source, read_only=True, data_only=True)
    try:
        sheet = workbook[workbook.sheetnames[0]]
        rows = [row for row in sheet.iter_rows(values_only=True)]
    finally:
        workbook.close()

    header = rows[QB_HEADER_ROW - 1]
    years: dict[int, int] = {}
    for index, cell in enumerate(header):
        text = str(cell).strip() if cell is not None else ""
        if re.fullmatch(r"20\d\d", text):
            years[int(text)] = index

    revenue: dict[str, dict[int, float]] = {}
    tally: Counter[str] = Counter()
    for raw in rows[QB_HEADER_ROW :]:
        name = "" if raw[0] is None else str(raw[0]).strip()
        if not name or name.startswith("Accrual Basis"):
            continue
        tally["rows_in"] += 1
        if name.upper() in QB_NON_CUSTOMERS:
            tally[f"excluded_pseudo_customer_{name.upper().replace(' ', '_')}"] += 1
            continue
        series = {
            year: float(raw[col])
            for year, col in years.items()
            if raw[col] not in (None, "")
        }
        if not series:
            tally["excluded_no_revenue_any_year"] += 1
            continue
        revenue[name] = series
        tally["rows_out"] += 1

    LOG.info("revenue: %s years=%s", dict(sorted(tally.items())), sorted(years))
    return revenue, dict(tally)


# --- cohort mechanics -------------------------------------------------------


def account_year_bookings(
    bookings: list[Booking], last_month: int | None = None
) -> dict[int, Counter[str]]:
    """Bookings per account per year, optionally restricted to Jan..last_month.

    >>> bs = [Booking(1, "a", date(2024, 3, 1), "Booked"),
    ...       Booking(2, "a", date(2024, 12, 1), "Booked"),
    ...       Booking(3, "b", date(2025, 2, 1), "Booked")]
    >>> dict(account_year_bookings(bs)[2024])
    {'a': 2}
    >>> dict(account_year_bookings(bs, last_month=10)[2024])
    {'a': 1}
    """
    out: dict[int, Counter[str]] = defaultdict(Counter)
    for booking in bookings:
        if last_month is not None and booking.flight_date.month > last_month:
            continue
        out[booking.flight_date.year][booking.account_id] += 1
    return out


def decompose_years(by_year: dict[int, Counter[str]]) -> list[dict[str, object]]:
    """The four-term volume decomposition, year by year.

    For each year Y against Y-1:

        B(Y) - B(Y-1) = new + reactivated + (retained_now - retained_then) - churned

    where `new` is bookings from accounts with no prior year on record,
    `reactivated` is bookings from accounts active earlier but not in Y-1,
    the bracket is same-account frequency change, and `churned` is the bookings
    the accounts that disappeared contributed in Y-1.

    >>> by = {2024: Counter({"a": 10, "b": 5}), 2025: Counter({"a": 12, "c": 3})}
    >>> row = decompose_years(by)[-1]
    >>> row["year"], row["new_accounts"], row["churned_accounts"]
    (2025, 1, 1)
    >>> row["bookings_from_new"], row["churned_bookings_prior_year"]
    (3, 5)
    >>> row["retained_bookings_delta"]
    2
    """
    years = sorted(by_year)
    rows: list[dict[str, object]] = []
    for year in years:
        now = by_year[year]
        prior = by_year.get(year - 1, Counter())
        ever_before = {
            account for earlier in years if earlier < year for account in by_year[earlier]
        }
        active = set(now)
        prior_active = set(prior)

        new = active - ever_before
        retained = active & prior_active
        reactivated = (active & ever_before) - prior_active
        churned = prior_active - active

        retained_now = sum(now[a] for a in retained)
        retained_then = sum(prior[a] for a in retained)
        rows.append(
            {
                "year": year,
                "active_accounts": len(active),
                "bookings": sum(now.values()),
                "bookings_per_active_account": round(
                    sum(now.values()) / len(active), 3
                )
                if active
                else 0.0,
                "new_accounts": len(new),
                "bookings_from_new": sum(now[a] for a in new),
                "reactivated_accounts": len(reactivated),
                "bookings_from_reactivated": sum(now[a] for a in reactivated),
                "retained_accounts": len(retained),
                "retained_bookings_now": retained_now,
                "retained_bookings_prior_year": retained_then,
                "retained_bookings_delta": retained_now - retained_then,
                "bookings_per_retained_account": round(retained_now / len(retained), 3)
                if retained
                else 0.0,
                "churned_accounts": len(churned),
                "churned_bookings_prior_year": sum(prior[a] for a in churned),
                "gross_churn_rate_pct": round(len(churned) / len(prior_active) * 100, 2)
                if prior_active
                else None,
                "logo_retention_rate_pct": round(
                    len(retained) / len(prior_active) * 100, 2
                )
                if prior_active
                else None,
                "bookings_delta_vs_prior": sum(now.values()) - sum(prior.values()),
            }
        )
    return rows


def retention_matrix(by_year: dict[int, Counter[str]]) -> list[dict[str, object]]:
    """For each acquisition cohort, accounts and bookings still present N years on."""
    years = sorted(by_year)
    first_year: dict[str, int] = {}
    for year in years:
        for account in by_year[year]:
            first_year.setdefault(account, year)

    cohorts: dict[int, set[str]] = defaultdict(set)
    for account, year in first_year.items():
        cohorts[year].add(account)

    rows: list[dict[str, object]] = []
    for cohort in sorted(cohorts):
        members = cohorts[cohort]
        base_bookings = sum(by_year[cohort][a] for a in members)
        for year in years:
            if year < cohort:
                continue
            present = {a for a in members if by_year[year][a] > 0}
            rows.append(
                {
                    "cohort_year": cohort,
                    "year": year,
                    "years_since_acquisition": year - cohort,
                    "cohort_size": len(members),
                    "accounts_active": len(present),
                    "pct_accounts_active": round(len(present) / len(members) * 100, 2),
                    "bookings": sum(by_year[year][a] for a in members),
                    "bookings_index_vs_first_year": round(
                        sum(by_year[year][a] for a in members) / base_bookings * 100, 1
                    )
                    if base_bookings
                    else None,
                }
            )
    return rows


def first_to_second(bookings: list[Booking]) -> list[dict[str, object]]:
    """First-to-second-booking conversion by acquisition cohort.

    The windowed rates are reported only for accounts whose first booking is at
    least that many days before the data cut, so an account acquired last month
    is not counted as a failure to re-book within a year.
    """
    dates: dict[str, list[date]] = defaultdict(list)
    for booking in bookings:
        dates[booking.account_id].append(booking.flight_date)

    windows = (90, 180, 365)
    buckets: dict[int, dict[str, object]] = {}
    for account, account_dates in dates.items():
        account_dates.sort()
        first = account_dates[0]
        cohort = first.year
        row = buckets.setdefault(
            cohort,
            {
                "cohort_year": cohort,
                "accounts": 0,
                "accounts_with_second_booking_ever": 0,
                "days_to_second": [],
                **{f"eligible_{w}d": 0 for w in windows},
                **{f"second_within_{w}d": 0 for w in windows},
            },
        )
        row["accounts"] = int(row["accounts"]) + 1
        second = account_dates[1] if len(account_dates) > 1 else None
        if second is not None:
            row["accounts_with_second_booking_ever"] = (
                int(row["accounts_with_second_booking_ever"]) + 1
            )
            gap = (second - first).days
            assert isinstance(row["days_to_second"], list)
            row["days_to_second"].append(gap)
        for window in windows:
            if (DATA_CUT - first).days >= window:
                row[f"eligible_{window}d"] = int(row[f"eligible_{window}d"]) + 1
                if second is not None and (second - first).days <= window:
                    row[f"second_within_{window}d"] = (
                        int(row[f"second_within_{window}d"]) + 1
                    )

    out: list[dict[str, object]] = []
    for cohort in sorted(buckets):
        row = buckets[cohort]
        gaps = sorted(row.pop("days_to_second"))  # type: ignore[arg-type]
        accounts = int(row["accounts"])
        record: dict[str, object] = {
            "cohort_year": cohort,
            "accounts": accounts,
            "accounts_with_second_booking_ever": row["accounts_with_second_booking_ever"],
            "pct_with_second_booking_ever": round(
                int(row["accounts_with_second_booking_ever"]) / accounts * 100, 2
            ),
            "median_days_to_second": gaps[len(gaps) // 2] if gaps else None,
        }
        for window in windows:
            eligible = int(row[f"eligible_{window}d"])
            record[f"eligible_{window}d"] = eligible
            record[f"pct_second_within_{window}d"] = (
                round(int(row[f"second_within_{window}d"]) / eligible * 100, 2)
                if eligible
                else None
            )
        out.append(record)
    return out


# --- revenue side -----------------------------------------------------------


def group_revenue(
    revenue: dict[str, dict[int, float]],
) -> tuple[dict[str, dict[int, float]], list[dict[str, str]]]:
    """Apply Donald's groupings and merge same-name duplicate QuickBooks customers.

    Returns the grouped revenue and a log of every merge performed.
    """
    mapping: dict[str, str] = {}
    log: list[dict[str, str]] = []

    for name in revenue:
        if name in BERGEN_GROUP:
            mapping[name] = "Bergen Funeral Service (group)"
            log.append(
                {"source_name": name, "grouped_as": mapping[name], "reason": "Donald 2026-11-10"}
            )
        elif name in ORTIZ_GROUP_DONALD:
            mapping[name] = "Ortiz funeral homes (group)"
            log.append(
                {"source_name": name, "grouped_as": mapping[name], "reason": "Donald 2026-11-10"}
            )

    # Merge customers whose names are identical once punctuation and corporate
    # suffixes are removed -- genuine QuickBooks duplicates.
    by_norm: dict[str, list[str]] = defaultdict(list)
    for name in revenue:
        if name not in mapping:
            by_norm[normalize_name(name)].append(name)
    for names in by_norm.values():
        if len(names) > 1:
            canonical = sorted(names, key=lambda n: (-len(n), n))[0]
            for name in names:
                mapping[name] = canonical
                if name != canonical:
                    log.append(
                        {
                            "source_name": name,
                            "grouped_as": canonical,
                            "reason": "duplicate QuickBooks customer (same normalized name)",
                        }
                    )

    grouped: dict[str, dict[int, float]] = defaultdict(dict)
    for name, series in revenue.items():
        key = mapping.get(name, name)
        target = grouped[key]
        for year, value in series.items():
            target[year] = target.get(year, 0.0) + value

    LOG.info(
        "revenue grouping: customers_in=%d customers_out=%d merges=%d",
        len(revenue),
        len(grouped),
        len(log),
    )
    return dict(grouped), sorted(log, key=lambda r: (r["grouped_as"], r["source_name"]))


def concentration_rows(grouped: dict[str, dict[int, float]]) -> list[dict[str, object]]:
    """Revenue concentration by year."""
    years = sorted({year for series in grouped.values() for year in series})
    rows: list[dict[str, object]] = []
    for year in years:
        values = [s[year] for s in grouped.values() if s.get(year, 0.0) > 0]
        row: dict[str, object] = {
            "year": year,
            "customers_with_revenue": len(values),
            "revenue": round(sum(values), 2),
            "hhi": round(hhi(values), 1),
        }
        for point in CURVE_POINTS:
            row[f"top{point}_share_pct"] = round(top_n_share(values, point) * 100, 2)
        rows.append(row)
    return rows


def revenue_churn_rows(grouped: dict[str, dict[int, float]]) -> list[dict[str, object]]:
    """Revenue-based acquisition and churn, which reaches back to 2016."""
    years = sorted({year for series in grouped.values() for year in series})
    active: dict[int, set[str]] = {
        year: {n for n, s in grouped.items() if s.get(year, 0.0) > 0} for year in years
    }
    rows: list[dict[str, object]] = []
    for year in years:
        prior = active.get(year - 1, set())
        ever_before = {n for y in years if y < year for n in active[y]}
        new = active[year] - ever_before
        retained = active[year] & prior
        reactivated = (active[year] & ever_before) - prior
        churned = prior - active[year]
        rev = lambda names, y: round(  # noqa: E731
            sum(grouped[n].get(y, 0.0) for n in names), 2
        )
        rows.append(
            {
                "year": year,
                "customers_with_revenue": len(active[year]),
                "revenue": rev(active[year], year),
                "new_customers": len(new),
                "revenue_from_new": rev(new, year),
                "reactivated_customers": len(reactivated),
                "revenue_from_reactivated": rev(reactivated, year),
                "retained_customers": len(retained),
                "revenue_from_retained": rev(retained, year),
                "revenue_from_retained_prior_year": rev(retained, year - 1),
                "churned_customers": len(churned),
                "revenue_lost_to_churn_prior_year": rev(churned, year - 1),
                "gross_churn_rate_pct": round(len(churned) / len(prior) * 100, 2)
                if prior
                else None,
            }
        )
    return rows


# --- joining the two sources ------------------------------------------------


def build_name_index(accounts: dict[str, Account]) -> dict[str, list[str]]:
    """Normalized account name -> account ids."""
    index: dict[str, list[str]] = defaultdict(list)
    for account in accounts.values():
        if account.name:
            index[normalize_name(account.name)].append(account.account_id)
    return {k: sorted(v) for k, v in index.items()}


def join_revenue_to_accounts(
    revenue_names: list[str],
    index: dict[str, list[str]],
    accounts: dict[str, Account],
) -> tuple[dict[str, list[str]], Counter[str]]:
    """Map each QuickBooks customer name to account ids.

    A name matching several account records is accepted only when those records
    are flagged duplicates of one another in the OMS export; otherwise the name
    is left unjoined and counted, so the error rate is visible rather than buried
    in a fuzzy match.
    """
    joined: dict[str, list[str]] = {}
    tally: Counter[str] = Counter()
    for name in revenue_names:
        ids = index.get(normalize_name(name), [])
        if not ids:
            tally["unmatched_no_account"] += 1
            continue
        if len(ids) == 1:
            joined[name] = ids
            tally["matched_unique"] += 1
            continue
        groups = {accounts[i].duplicate_group_id for i in ids if accounts[i].duplicate_group_id}
        if len(groups) == 1:
            joined[name] = ids
            tally["matched_via_duplicate_group"] += 1
        else:
            tally["unmatched_ambiguous"] += 1
    return joined, tally


# --- named accounts ---------------------------------------------------------


def named_account_rows(
    grouped_revenue: dict[str, dict[int, float]],
    raw_revenue: dict[str, dict[int, float]],
    bookings_by_account_year: dict[int, Counter[str]],
    joined: dict[str, list[str]],
    accounts: dict[str, Account],
) -> list[dict[str, object]]:
    """Trajectory rows for the accounts and groups the question turns on."""
    years = sorted(bookings_by_account_year)
    revenue_years = sorted({y for s in grouped_revenue.values() for y in s})

    def bookings_for(names: list[str]) -> dict[int, int]:
        ids: set[str] = set()
        for name in names:
            ids.update(joined.get(name, []))
        return {
            year: sum(bookings_by_account_year[year][i] for i in ids) for year in years
        }

    entities: list[tuple[str, str, list[str]]] = [
        ("Bergen Funeral Service (group)", "partner / Donald grouping", list(BERGEN_GROUP)),
        ("Ortiz funeral homes (group, Donald's five)", "Donald grouping", list(ORTIZ_GROUP_DONALD)),
        (
            "Ortiz funeral homes (extended, sensitivity)",
            "sensitivity -- adds names Donald did not list",
            list(ORTIZ_GROUP_DONALD) + list(ORTIZ_GROUP_EXTENDED_EXTRA),
        ),
    ]
    for label, marker in (
        ("National Mortuary Shipping", "national mortuary shipping"),
        ("International Mortuary Shipping", "international mortuary shipping"),
        ("Las Rosas (all)", "las rosas"),
    ):
        names = [n for n in raw_revenue if marker in n.lower()]
        entities.append((label, "partner tier", names))

    rows: list[dict[str, object]] = []
    for label, kind, names in entities:
        present = [n for n in names if n in raw_revenue]
        revenue: dict[int, float] = defaultdict(float)
        for name in present:
            for year, value in raw_revenue[name].items():
                revenue[year] += value
        book = bookings_for(present)
        for year in revenue_years:
            rows.append(
                {
                    "entity": label,
                    "kind": kind,
                    "component_customers": len(present),
                    "year": year,
                    "revenue": round(revenue.get(year, 0.0), 2),
                    "bookings": book.get(year) if year in years else None,
                }
            )

    # Corporate groups, from the account side (bookings) only -- group revenue is
    # often billed centrally, so per-location revenue understates them.
    for group_label in ("SCI", "Foundation Partners", "Northstar", "Carriage Services"):
        ids = {a.account_id for a in accounts.values() if a.group == group_label}
        for year in years:
            member_ids = {i for i in ids if bookings_by_account_year[year][i] > 0}
            rows.append(
                {
                    "entity": f"{group_label} (corporate group, booking side)",
                    "kind": "corporate group",
                    "component_customers": len(member_ids),
                    "year": year,
                    "revenue": None,
                    "bookings": sum(bookings_by_account_year[year][i] for i in ids),
                }
            )
    return rows


# --- output -----------------------------------------------------------------


def git_sha() -> str | None:
    """Current commit, when the tree is a git checkout."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            check=False,
            timeout=10,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    return result.stdout.strip() or None


def write_csv(path: Path, rows: list[dict[str, object]], sort_keys: tuple[str, ...]) -> None:
    """Write rows deterministically so that diffs are meaningful."""
    if not rows:
        raise ValueError(f"refusing to write empty output: {path}")
    fields: list[str] = []
    for row in rows:
        for key in row:
            if key not in fields:
                fields.append(key)
    ordered = sorted(
        rows, key=lambda r: tuple(str(r.get(k)) if r.get(k) is not None else "" for k in sort_keys)
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(ordered)
    LOG.info("wrote %s rows_out=%d", path, len(ordered))


def write_meta(
    path: Path,
    sources: list[Path],
    rows_in: int,
    rows_out: int,
    dropped: list[str],
    filters: list[str],
    note: str,
) -> None:
    """Write the companion `.meta.json` required by `CLAUDE.md` §8."""
    meta = {
        "script": SCRIPT_PATH,
        "script_version": VERSION,
        "source_files": [str(s) for s in sources],
        "rows_in": rows_in,
        "rows_out": rows_out,
        "dropped_columns_at_load": dropped,
        "filters_applied": filters,
        "git_sha": git_sha(),
        "run_timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "data_cut": DATA_CUT.isoformat(),
        "privacy_note": (
            "Shipment export carries no decedent or family data (four columns). "
            "OMS account export identifier columns dropped at load per CLAUDE.md "
            "§7.2. Funeral-home business names retained deliberately. No "
            "row-level shipment data is written."
        ),
        "note": note,
    }
    path.write_text(json.dumps(meta, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    """Entry point."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--shipments", type=Path, default=DEFAULT_SHIPMENTS)
    parser.add_argument("--revenue", type=Path, default=DEFAULT_REVENUE)
    parser.add_argument("--accounts", type=Path, default=DEFAULT_ACCOUNTS)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(levelname)s %(message)s",
    )

    accounts, accounts_in, dropped = load_accounts(args.accounts)
    bookings, booking_tally = load_bookings(args.shipments)
    revenue, revenue_tally = load_revenue(args.revenue)

    out = args.out
    sources = [args.shipments, args.revenue, args.accounts]

    # --- data quality -------------------------------------------------------
    workbook = openpyxl.load_workbook(args.shipments, read_only=True, data_only=True)
    try:
        rows = workbook["Shipments"].iter_rows(values_only=True)
        next(rows)
        quality: dict[str, Counter[str]] = defaultdict(Counter)
        for raw in rows:
            flight = parse_flight_date(raw[2])
            if flight is None:
                key = "no flight date"
            elif not (MIN_YEAR <= flight.year <= MAX_YEAR):
                key = f"impossible year {flight.year}"
            else:
                key = str(flight.year)
            bucket = quality[key]
            bucket["rows"] += 1
            if raw[1] is None or not str(raw[1]).strip():
                bucket["missing_funeral_home"] += 1
            status = ("" if raw[3] is None else str(raw[3])).strip()
            if status != "Booked":
                bucket["status_not_booked"] += 1
            bucket[f"status::{status or '(blank)'}"] += 1
    finally:
        workbook.close()

    quality_rows: list[dict[str, object]] = []
    for key in sorted(quality):
        bucket = quality[key]
        quality_rows.append(
            {
                "flight_date_year": key,
                "rows": bucket["rows"],
                "missing_funeral_home": bucket["missing_funeral_home"],
                "missing_funeral_home_pct": round(
                    bucket["missing_funeral_home"] / bucket["rows"] * 100, 2
                ),
                "status_not_booked": bucket["status_not_booked"],
                "status_not_booked_pct": round(
                    bucket["status_not_booked"] / bucket["rows"] * 100, 2
                ),
                "status_mix": "; ".join(
                    f"{k.split('::', 1)[1]}={v}"
                    for k, v in sorted(bucket.items())
                    if k.startswith("status::")
                ),
            }
        )
    write_csv(out / "cohort-shipment-data-quality.csv", quality_rows, ("flight_date_year",))
    write_meta(
        out / "cohort-shipment-data-quality.meta.json",
        [args.shipments],
        booking_tally["rows_in"],
        len(quality_rows),
        [],
        ["none -- every row in the export is counted here"],
        "Field completeness and status mix of the shipment export, by flight-date year.",
    )

    # --- cohort decomposition, full year and like-for-like -----------------
    full_year = account_year_bookings(bookings)
    like_for_like = account_year_bookings(bookings, last_month=LLF_LAST_MONTH)

    cohort_rows: list[dict[str, object]] = []
    for label, series in (("full_year", full_year), (f"jan_to_m{LLF_LAST_MONTH}", like_for_like)):
        for row in decompose_years(series):
            cohort_rows.append({"window": label, **row})
    write_csv(out / "cohort-yearly-accounts.csv", cohort_rows, ("window", "year"))
    write_meta(
        out / "cohort-yearly-accounts.meta.json",
        [args.shipments],
        booking_tally["rows_in"],
        len(cohort_rows),
        [],
        [
            "rows with no shipping_funeral_home_id excluded (cannot enter a cohort)",
            "rows with no flight_date excluded (cannot be assigned a year)",
            f"flight_date outside {MIN_YEAR}-{MAX_YEAR} excluded as a data-entry defect",
            f"flight_date after {DATA_CUT.isoformat()} excluded (beyond the data cut)",
            f"window jan_to_m{LLF_LAST_MONTH} restricts every year to January-October",
        ],
        "Four-term volume decomposition: acquisition, reactivation, same-account "
        "frequency, churn. 2023 'new' is inflated by the legacy system's 2022 "
        "adoption ramp; 2024 is the first trustworthy acquisition year.",
    )

    write_csv(
        out / "cohort-retention-matrix.csv",
        retention_matrix(full_year),
        ("cohort_year", "year"),
    )
    write_meta(
        out / "cohort-retention-matrix.meta.json",
        [args.shipments],
        booking_tally["rows_out"],
        0,
        [],
        ["as cohort-yearly-accounts"],
        "Accounts and bookings surviving by acquisition cohort. 2022 cohort is "
        "contaminated by left-censoring and is not an acquisition cohort.",
    )

    write_csv(out / "cohort-first-to-second.csv", first_to_second(bookings), ("cohort_year",))
    write_meta(
        out / "cohort-first-to-second.meta.json",
        [args.shipments],
        booking_tally["rows_out"],
        0,
        [],
        [
            "windowed rates restricted to accounts whose first booking is at least "
            "the window length before the data cut"
        ],
        "Does CSI keep what it wins? First-to-second-booking conversion by cohort.",
    )

    # --- revenue side -------------------------------------------------------
    grouped, merge_log = group_revenue(revenue)
    write_csv(
        out / "revenue-concentration-by-year.csv", concentration_rows(grouped), ("year",)
    )
    write_meta(
        out / "revenue-concentration-by-year.meta.json",
        [args.revenue],
        revenue_tally["rows_in"],
        0,
        [],
        [
            "QuickBooks 'TOTAL' row excluded -- it is the report's own grand total "
            "and including it doubles every annual figure",
            "'ALREADY PAID' pseudo-customer excluded",
            "Bergen FL+NJ combined and Donald's five Ortiz homes combined per his "
            "instruction 2026-11-10",
            "duplicate QuickBooks customers with the same normalized name merged",
            "2026 is partial, to 2026-11-10: shares are valid, the level is not",
        ],
        "Top-N revenue share and HHI, 2016-2026, on grouped customers.",
    )

    write_csv(
        out / "revenue-customer-churn-by-year.csv", revenue_churn_rows(grouped), ("year",)
    )
    write_meta(
        out / "revenue-customer-churn-by-year.meta.json",
        [args.revenue],
        revenue_tally["rows_in"],
        0,
        [],
        ["as revenue-concentration-by-year"],
        "Revenue-based acquisition and churn. Reaches back to 2016, so unlike the "
        "shipment file it can show churn before 2023. 2026 is partial.",
    )

    if merge_log:
        write_csv(
            out / "revenue-customer-grouping-log.csv",
            [dict(r) for r in merge_log],
            ("grouped_as", "source_name"),
        )
        write_meta(
            out / "revenue-customer-grouping-log.meta.json",
            [args.revenue],
            revenue_tally["rows_in"],
            len(merge_log),
            [],
            [],
            "Every customer-name merge applied, so each one can be reversed.",
        )

    # --- join and reconciliation -------------------------------------------
    index = build_name_index(accounts)
    joined, join_tally = join_revenue_to_accounts(sorted(revenue), index, accounts)
    matched_revenue_2024 = sum(
        revenue[n].get(2024, 0.0) for n in joined if 2024 in revenue[n]
    )
    total_revenue_2024 = sum(s.get(2024, 0.0) for s in revenue.values())
    matched_ids = {i for ids in joined.values() for i in ids}
    bookings_2024 = full_year.get(2024, Counter())
    join_rows = [
        {
            "metric": "quickbooks_customers",
            "value": len(revenue),
        },
        {"metric": "matched_unique_name", "value": join_tally["matched_unique"]},
        {
            "metric": "matched_via_duplicate_group",
            "value": join_tally["matched_via_duplicate_group"],
        },
        {"metric": "unmatched_no_account_record", "value": join_tally["unmatched_no_account"]},
        {"metric": "unmatched_ambiguous_name", "value": join_tally["unmatched_ambiguous"]},
        {
            "metric": "pct_2024_revenue_joined",
            "value": round(matched_revenue_2024 / total_revenue_2024 * 100, 2)
            if total_revenue_2024
            else None,
        },
        {
            "metric": "pct_2024_bookings_on_joined_accounts",
            "value": round(
                sum(bookings_2024[i] for i in matched_ids) / sum(bookings_2024.values()) * 100,
                2,
            )
            if bookings_2024
            else None,
        },
        {
            "metric": "shipping_accounts_in_export",
            "value": len({b.account_id for b in bookings}),
        },
        {
            "metric": "shipping_accounts_absent_from_account_dimension",
            "value": len({b.account_id for b in bookings} - set(accounts)),
        },
    ]
    write_csv(out / "cohort-join-quality.csv", join_rows, ("metric",))
    write_meta(
        out / "cohort-join-quality.meta.json",
        sources,
        accounts_in + revenue_tally["rows_in"],
        len(join_rows),
        dropped,
        ["exact match on normalized business name only -- no fuzzy matching"],
        "Join coverage between QuickBooks customer names and OMS account records. "
        "Ambiguous names are left unjoined rather than guessed.",
    )

    oms_revenue = {2023: 13900783.0, 2024: 14141792.0, 2025: 14417145.0}
    recon_rows: list[dict[str, object]] = []
    for year in sorted({y for s in revenue.values() for y in s}):
        qb = sum(s.get(year, 0.0) for s in revenue.values())
        oms = oms_revenue.get(year)
        recon_rows.append(
            {
                "year": year,
                "quickbooks_accrued_revenue": round(qb, 2),
                "oms_analytics_revenue": oms,
                "delta": round(qb - oms, 2) if oms else None,
                "delta_pct": round((qb - oms) / oms * 100, 2) if oms else None,
                "comparable": "yes" if oms else "no -- OMS history begins Sep 2022",
            }
        )
    write_csv(out / "qb-oms-revenue-reconciliation.csv", recon_rows, ("year",))
    write_meta(
        out / "qb-oms-revenue-reconciliation.meta.json",
        [args.revenue],
        revenue_tally["rows_in"],
        len(recon_rows),
        [],
        [
            "QuickBooks 'TOTAL' and 'ALREADY PAID' rows excluded",
            "OMS figures quoted from CLAUDE.md §2 / reports/analytics-reconciliation.md",
        ],
        "First reconciliation of QuickBooks accrued revenue against the OMS "
        "analytics export (CLAUDE.md §6).",
    )

    write_csv(
        out / "named-account-trajectory.csv",
        named_account_rows(grouped, revenue, full_year, joined, accounts),
        ("entity", "year"),
    )
    write_meta(
        out / "named-account-trajectory.meta.json",
        sources,
        revenue_tally["rows_in"] + booking_tally["rows_in"],
        0,
        dropped,
        [
            "Donald's groupings applied as instructed; an extended Ortiz grouping is "
            "reported alongside as a sensitivity, never folded into the primary figure",
            "corporate-group rows are booking-side only: group revenue is often "
            "billed centrally, so per-location revenue understates it",
        ],
        "Trajectory of the accounts and groups the retention-vs-acquisition question "
        "turns on.",
    )

    LOG.info("done")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
