"""Canonical metric functions for CSI. The executable half of context/metric-definitions.md.

Purpose
    Every metric in `context/metric-definitions.md` that can be reduced to arithmetic or
    to a classification rule lives here, so that two agents computing "churn" or "yield"
    compute the same thing. Prose definitions drift; functions do not.

    The account-cohort functions are written and tested BEFORE the data exists. That is
    deliberate. When the booking-level export lands (TASK-0003) the definition is already
    settled and nobody has to negotiate it under time pressure.

Inputs
    Pure functions over values and over booking-level records passed as
    `Iterable[BookingRecord]`. Nothing in this module reads a file, so nothing in it can
    touch `data/raw/` or print a decedent name.

Outputs
    Return values only. No side effects, no I/O, no globals.

PII (CLAUDE.md §7.2)
    `BookingRecord` carries a funeral home ID and a date and nothing else. There is
    deliberately no field for any person. Callers building records from an OMS export must
    drop decedent and family columns at load, not after.

Owner
    data-analyst
Date
    2026-11-02
"""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from datetime import date, timedelta

# The trailing window that defines account activity. 365 days, not 90.
# Justified in context/metric-definitions.md M-12. Do not change without a handoff:
# every churn and retention figure CSI has ever published rests on it.
ACTIVITY_WINDOW_DAYS = 365

# OMS history begins September 2022, and pre-2023 records reflect migration artifacts
# rather than real history (context/brain/company-facts.md).
OMS_HISTORY_BEGINS = date(2022, 9, 1)
COHORT_ANALYSIS_BEGINS = date(2023, 1, 1)


@dataclass(frozen=True)
class BookingRecord:
    """One landed booking, reduced to the only two fields cohort analysis needs.

    `revenue` is optional and used only for revenue-weighted churn. A booking with
    unknown revenue carries None, which is not the same as 0.0 and must not be coerced
    to it.
    """

    funeral_home_id: str
    booking_date: date
    revenue: float | None = None


@dataclass(frozen=True)
class AccountCohorts:
    """Account classification as at a single date. See metric-definitions.md M-12..M-15.

    The active set is partitioned exactly: active == new | reactivated | retained.
    `churned` is disjoint from `active` by construction.
    """

    as_of: date
    window_days: int
    new: frozenset[str]
    reactivated: frozenset[str]
    retained: frozenset[str]
    churned: frozenset[str]

    @property
    def active(self) -> frozenset[str]:
        """Accounts with at least one landed booking in the current window."""
        return self.new | self.reactivated | self.retained

    @property
    def active_prior(self) -> frozenset[str]:
        """Accounts active in the prior window: the churn denominator."""
        return self.retained | self.churned

    def churn_rate(self) -> float:
        """Churned accounts as a share of accounts active in the prior window.

        Returns 0.0 when no account was active in the prior window, which is a real
        answer for a period before the business had a base, not a missing value.
        """
        denominator = len(self.active_prior)
        if denominator == 0:
            return 0.0
        return len(self.churned) / denominator


def classify_accounts(
    bookings: Iterable[BookingRecord],
    as_of: date,
    window_days: int = ACTIVITY_WINDOW_DAYS,
    history_begins: date = OMS_HISTORY_BEGINS,
) -> AccountCohorts:
    """Classify every funeral home as new, reactivated, retained or churned as at `as_of`.

    Windows, both half-open on the left so that no booking is counted twice:
        current = (as_of - window_days, as_of]
        prior   = (as_of - 2*window_days, as_of - window_days]

    Rules:
        active       at least one landed booking in `current`
        new          active, and no booking at all before the current window opened
        reactivated  active, has a booking before the current window, none in `prior`
        retained     active, and also active in `prior`
        churned      active in `prior`, not active in `current`

    Raises:
        ValueError: if the prior window opens before `history_begins`. Classifying
            new-versus-reactivated needs a full window of history behind the prior
            window; without it, every long-dormant account looks new and churn is
            unmeasurable. With OMS history from 2022-09-01 and a 365-day window, the
            earliest valid `as_of` is 2024-08-31. This fails loudly rather than
            returning a number nobody can trust (CLAUDE.md §8).
    """
    if window_days <= 0:
        raise ValueError(f"window_days must be positive, got {window_days}")

    current_opens = as_of - timedelta(days=window_days)
    prior_opens = as_of - timedelta(days=2 * window_days)
    if prior_opens < history_begins:
        raise ValueError(
            f"Cannot classify accounts as at {as_of.isoformat()} with a "
            f"{window_days}-day window: the prior window opens "
            f"{prior_opens.isoformat()}, before OMS history begins "
            f"{history_begins.isoformat()}. Two full windows of history are required. "
            f"Earliest valid as_of is "
            f"{(history_begins + timedelta(days=2 * window_days)).isoformat()}."
        )

    in_current: set[str] = set()
    in_prior: set[str] = set()
    ever_before_current: set[str] = set()

    for record in bookings:
        account = record.funeral_home_id
        booking_date = record.booking_date
        if booking_date > as_of:
            # Future-dated bookings exist in the OMS analytics export (M-02). They are
            # not landed yet and must not enter a cohort classification.
            continue
        if booking_date > current_opens:
            in_current.add(account)
            continue
        ever_before_current.add(account)
        if booking_date > prior_opens:
            in_prior.add(account)

    retained = in_current & in_prior
    new = in_current - ever_before_current
    reactivated = in_current - in_prior - new
    churned = in_prior - in_current

    return AccountCohorts(
        as_of=as_of,
        window_days=window_days,
        new=frozenset(new),
        reactivated=frozenset(reactivated),
        retained=frozenset(retained),
        churned=frozenset(churned),
    )


def revenue_weighted_churn(
    bookings: Iterable[BookingRecord],
    cohorts: AccountCohorts,
) -> float:
    """Churn weighted by the prior window's revenue, not by account count.

    Account-count churn treats a funeral home that ships twice a decade the same as one
    that ships weekly. In a business with low per-account frequency that overstates the
    problem. This is the figure to lead with; count-based churn is the supporting one.

    Formula:
        revenue in prior window from churned accounts
        -------------------------------------------------
        revenue in prior window from all prior-active accounts

    Bookings with `revenue is None` are excluded from both numerator and denominator and
    are the caller's problem to report; silently treating them as zero would understate
    churn.

    Returns 0.0 when the denominator is zero.
    """
    current_opens = cohorts.as_of - timedelta(days=cohorts.window_days)
    prior_opens = cohorts.as_of - timedelta(days=2 * cohorts.window_days)

    churned_revenue = 0.0
    base_revenue = 0.0
    prior_active = cohorts.active_prior

    for record in bookings:
        if record.revenue is None:
            continue
        if not (prior_opens < record.booking_date <= current_opens):
            continue
        if record.funeral_home_id not in prior_active:
            continue
        base_revenue += record.revenue
        if record.funeral_home_id in cohorts.churned:
            churned_revenue += record.revenue

    if base_revenue == 0.0:
        return 0.0
    return churned_revenue / base_revenue


def shipments_per_retained_account(
    bookings: Iterable[BookingRecord],
    cohorts: AccountCohorts,
) -> float:
    """Mean landed bookings in the current window across retained accounts only.

    The frequency term in the volume decomposition: volume moves because accounts are
    gained, lost, or because retained accounts ship more or less often. Restricting to
    retained accounts isolates the third effect from the first two.

    Returns 0.0 when there are no retained accounts.
    """
    if not cohorts.retained:
        return 0.0

    current_opens = cohorts.as_of - timedelta(days=cohorts.window_days)
    counts: dict[str, int] = defaultdict(int)
    for record in bookings:
        if record.funeral_home_id not in cohorts.retained:
            continue
        if current_opens < record.booking_date <= cohorts.as_of:
            counts[record.funeral_home_id] += 1

    return sum(counts.values()) / len(cohorts.retained)


def yield_per_booking(revenue: float, landed_bookings: int) -> float:
    """Revenue per landed booking. The metric 2026's growth is actually coming from.

    Equals the OMS analytics export's `Average Revenue per Booking`. Both inputs must
    come from the same period and the same status filter; mixing a revenue figure and a
    booking count from two different filters is the commonest way this number goes wrong.

    Bookings with zero or missing revenue stay in the denominator. Dropping them flatters
    yield, so report `Bookings Missing Revenue` alongside instead.

    Raises:
        ValueError: on a zero or negative booking count.
    """
    if landed_bookings <= 0:
        raise ValueError(f"landed_bookings must be positive, got {landed_bookings}")
    return revenue / landed_bookings


def gross_margin_pct(published_rate: float, contracted_rate: float) -> float:
    """Rate-card gross margin on one lane, as a percentage of the customer price.

    NOT contribution margin. Excludes cost to serve, accessorials and rework entirely.
    See metric-definitions.md M-07 before quoting this anywhere.

    Raises:
        ValueError: on a zero or negative published rate.
    """
    if published_rate <= 0:
        raise ValueError(f"published_rate must be positive, got {published_rate}")
    return (published_rate - contracted_rate) / published_rate * 100.0


def booking_accuracy_pct(total_bookings: int, bookings_with_internal_errors: int) -> float:
    """Booking accuracy, adopted verbatim from the Bookings Director scorecard KR1.

    Accuracy % = (total bookings - bookings with internal errors) / total bookings

    Only errors attributable to the bookings team count; airline schedule changes,
    weather, airline operational failures, late funeral-home documents and
    customer-driven changes do not. The twelve counted error classes are listed in
    `context/okrs-2026-master.md` and must not be re-derived here.

    A booking with two errors counts once, not twice: the unit is the booking.

    Raises:
        ValueError: on a non-positive total, or an error count above the total.
    """
    if total_bookings <= 0:
        raise ValueError(f"total_bookings must be positive, got {total_bookings}")
    if not 0 <= bookings_with_internal_errors <= total_bookings:
        raise ValueError(
            f"bookings_with_internal_errors must be between 0 and {total_bookings}, "
            f"got {bookings_with_internal_errors}"
        )
    return (total_bookings - bookings_with_internal_errors) / total_bookings * 100.0


def attribution_completeness_pct(total_bookings: int, bookings_missing_funeral_home: int) -> float:
    """Share of bookings that carry a shipping funeral home link.

    Source fields: the OMS analytics export header rows `Total Bookings` and
    `Bookings Missing Funeral Home Link`. This is the gate on every account metric —
    churn, retention and CAC are all computed over the attributed subset only, and the
    unattributed remainder is reported, never dropped quietly.

    Raises:
        ValueError: on a non-positive total, or a missing count above the total.
    """
    if total_bookings <= 0:
        raise ValueError(f"total_bookings must be positive, got {total_bookings}")
    if not 0 <= bookings_missing_funeral_home <= total_bookings:
        raise ValueError(
            f"bookings_missing_funeral_home must be between 0 and {total_bookings}, "
            f"got {bookings_missing_funeral_home}"
        )
    return (total_bookings - bookings_missing_funeral_home) / total_bookings * 100.0


def like_for_like_growth_pct(current: Mapping[str, float], prior: Mapping[str, float]) -> float:
    """Growth between two periods, computed only over months present in both.

    CSI's business is seasonal: January indexes at 115 and June at 92 against the annual
    mean (reports/analytics-reconciliation.md). Comparing a part-year against a full year,
    or any month against a different month, produces a number that looks like a trend and
    is not one. This function makes the like-for-like rule mechanical.

    Args:
        current: month key -> value for the current period, e.g. {"Jan": 1.0}.
        prior: month key -> value for the prior period.

    Raises:
        ValueError: if the periods share no months, or the shared prior total is zero.
    """
    shared = sorted(set(current) & set(prior))
    if not shared:
        raise ValueError(
            "current and prior periods share no months; no like-for-like comparison exists"
        )
    current_total = sum(current[month] for month in shared)
    prior_total = sum(prior[month] for month in shared)
    if prior_total == 0:
        raise ValueError(f"prior total over shared months {shared} is zero; growth is undefined")
    return (current_total - prior_total) / prior_total * 100.0
