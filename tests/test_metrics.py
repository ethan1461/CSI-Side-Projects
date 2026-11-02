"""Known-answer tests for src/metrics.py. Run: python3 -m pytest tests/ -q

Every metric function gets at least one test whose expected value was computed by hand
(CLAUDE.md §8). Where a metric has a published figure in `CLAUDE.md §2` or in
`reports/`, the test asserts the function reproduces that published figure, so a change
to a definition breaks a test rather than quietly changing a number in a report.

PII (CLAUDE.md §7.2): the account fixture uses synthetic funeral home IDs (FH-001...) and
round synthetic revenue figures. No CSI account, no real revenue value, and above all no
person appears in this file.
"""

from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from metrics import (
    AccountCohorts,
    BookingRecord,
    attribution_completeness_pct,
    booking_accuracy_pct,
    classify_accounts,
    gross_margin_pct,
    like_for_like_growth_pct,
    revenue_weighted_churn,
    shipments_per_retained_account,
    yield_per_booking,
)

# --------------------------------------------------------------------------------------
# Account cohort fixture, hand-worked.
#
# as_of         = 2026-06-30
# window        = 365 days
# current window = (2025-06-30, 2026-06-30]
# prior window   = (2024-06-30, 2025-06-30]
#
# id      bookings (date, revenue)                        expected class
# FH-001  2024-08-01 None | 2025-03-01 1000               retained  (prior + current)
#         2026-02-01 1200 | 2026-05-01 1300
# FH-002  2026-01-15 900                                  new       (no prior history)
# FH-003  2023-05-01 800  | 2026-04-01 1100               reactivated (gap over prior)
# FH-004  2024-12-01 3000                                 churned   (prior only)
# FH-005  2023-01-10 700                                  none      (dormant, pre-prior)
# FH-006  2025-07-01 950                                  new       (boundary: opens + 1d)
# FH-007  2025-06-30 500                                  churned   (boundary: == opens,
#                                                                    so prior not current)
# FH-008  2025-01-01 1500 | 2026-08-01 1400               churned   (future row ignored)
# FH-009  2025-02-01 2000 | 2026-03-01 1000               retained
#
# retained = {001, 009}   new = {002, 006}   reactivated = {003}
# churned  = {004, 007, 008}                 unclassified = {005}
# active = 5, active_prior = 5, churn_rate = 3/5 = 0.60
# --------------------------------------------------------------------------------------

AS_OF = date(2026, 6, 30)

FIXTURE: list[BookingRecord] = [
    BookingRecord("FH-001", date(2024, 8, 1), None),
    BookingRecord("FH-001", date(2025, 3, 1), 1000.0),
    BookingRecord("FH-001", date(2026, 2, 1), 1200.0),
    BookingRecord("FH-001", date(2026, 5, 1), 1300.0),
    BookingRecord("FH-002", date(2026, 1, 15), 900.0),
    BookingRecord("FH-003", date(2023, 5, 1), 800.0),
    BookingRecord("FH-003", date(2026, 4, 1), 1100.0),
    BookingRecord("FH-004", date(2024, 12, 1), 3000.0),
    BookingRecord("FH-005", date(2023, 1, 10), 700.0),
    BookingRecord("FH-006", date(2025, 7, 1), 950.0),
    BookingRecord("FH-007", date(2025, 6, 30), 500.0),
    BookingRecord("FH-008", date(2025, 1, 1), 1500.0),
    BookingRecord("FH-008", date(2026, 8, 1), 1400.0),
    BookingRecord("FH-009", date(2025, 2, 1), 2000.0),
    BookingRecord("FH-009", date(2026, 3, 1), 1000.0),
]


@pytest.fixture(name="cohorts")
def cohorts_fixture() -> AccountCohorts:
    return classify_accounts(FIXTURE, as_of=AS_OF)


def test_cohort_membership_is_the_hand_worked_answer(cohorts: AccountCohorts) -> None:
    assert cohorts.retained == frozenset({"FH-001", "FH-009"})
    assert cohorts.new == frozenset({"FH-002", "FH-006"})
    assert cohorts.reactivated == frozenset({"FH-003"})
    assert cohorts.churned == frozenset({"FH-004", "FH-007", "FH-008"})


def test_dormant_account_is_in_no_cohort(cohorts: AccountCohorts) -> None:
    """FH-005 last shipped before the prior window. It is neither active nor churned.

    Churn is only ever measured against the prior window. An account silent for three
    years cannot churn again, and counting it would inflate churn every period forever.
    """
    everything = cohorts.active | cohorts.churned
    assert "FH-005" not in everything


def test_active_set_is_partitioned_exactly(cohorts: AccountCohorts) -> None:
    """active == new | reactivated | retained, with no overlap. The identity that makes
    the four definitions usable together in one table."""
    assert cohorts.active == cohorts.new | cohorts.reactivated | cohorts.retained
    assert len(cohorts.active) == len(cohorts.new) + len(cohorts.reactivated) + len(
        cohorts.retained
    )
    assert not cohorts.active & cohorts.churned


def test_boundary_dates_are_half_open_on_the_left(cohorts: AccountCohorts) -> None:
    """A booking dated exactly on the window open date belongs to the earlier window.

    FH-007 shipped on 2025-06-30, the instant the current window opens. It is churned,
    not active. FH-006 shipped one day later and is new. Without a stated convention two
    agents would split this account differently and both would be defensible.
    """
    assert "FH-007" in cohorts.churned
    assert "FH-006" in cohorts.new


def test_future_dated_bookings_do_not_make_an_account_active(cohorts: AccountCohorts) -> None:
    """The OMS analytics export carries bookings dated after the export date (M-02).

    FH-008's only recent row is dated 2026-08-01, after as_of. It has not landed, so
    FH-008 is churned. Treating scheduled shipments as landed would hide real churn.
    """
    assert "FH-008" in cohorts.churned
    assert "FH-008" not in cohorts.active


def test_churn_rate_counts_against_the_prior_active_base(cohorts: AccountCohorts) -> None:
    assert cohorts.active_prior == frozenset({"FH-001", "FH-009", "FH-004", "FH-007", "FH-008"})
    assert cohorts.churn_rate() == pytest.approx(3 / 5)


def test_revenue_weighted_churn_differs_from_count_churn(cohorts: AccountCohorts) -> None:
    """Hand-worked: prior-window revenue of prior-active accounts is
    1000 + 3000 + 500 + 1500 + 2000 = 8000, of which the churned accounts are
    3000 + 500 + 1500 = 5000. So 0.625 against a count churn of 0.60.

    The FH-001 2024-08-01 row carries revenue None and is excluded from both sides;
    coercing it to zero would have understated the base and overstated churn.
    """
    assert revenue_weighted_churn(FIXTURE, cohorts) == pytest.approx(0.625)
    assert revenue_weighted_churn(FIXTURE, cohorts) != pytest.approx(cohorts.churn_rate())


def test_shipments_per_retained_account(cohorts: AccountCohorts) -> None:
    """FH-001 shipped twice in the current window, FH-009 once. Mean 1.5."""
    assert shipments_per_retained_account(FIXTURE, cohorts) == pytest.approx(1.5)


def test_classification_before_two_windows_of_history_fails_loudly() -> None:
    """OMS history begins 2022-09-01, so the earliest classifiable date is 2024-08-31.

    CSI cannot compute a churn rate for any date before then, and the function says so
    rather than returning a number built on truncated history.
    """
    with pytest.raises(ValueError, match="before OMS history begins"):
        classify_accounts(FIXTURE, as_of=date(2024, 8, 30))

    classify_accounts(FIXTURE, as_of=date(2024, 8, 31))  # earliest valid date, must not raise


def test_negative_window_rejected() -> None:
    with pytest.raises(ValueError, match="window_days must be positive"):
        classify_accounts(FIXTURE, as_of=AS_OF, window_days=0)


# --------------------------------------------------------------------------------------
# Scalar metrics. Expected values are the published CSI figures where one exists.
# --------------------------------------------------------------------------------------


def test_yield_reproduces_the_published_2026_figure() -> None:
    """CLAUDE.md §2: Jan-Aug 2026 revenue $10,030,160 on 7,451 bookings, yield $1,346."""
    assert yield_per_booking(10_030_160.0, 7_451) == pytest.approx(1346.15, abs=0.01)
    assert round(yield_per_booking(10_030_160.0, 7_451)) == 1346


def test_yield_rejects_zero_bookings() -> None:
    with pytest.raises(ValueError, match="landed_bookings must be positive"):
        yield_per_booking(1000.0, 0)


def test_gross_margin_pct_hand_computed() -> None:
    """A $1,000 customer price against a $650 contracted cost is 35.0% margin -- the
    order of CSI's measured domestic figure, computed from synthetic round numbers."""
    assert gross_margin_pct(1000.0, 650.0) == pytest.approx(35.0)
    assert gross_margin_pct(1000.0, 1000.0) == pytest.approx(0.0)
    assert gross_margin_pct(1000.0, 1200.0) == pytest.approx(-20.0)  # loss-making lane


def test_gross_margin_rejects_zero_published_rate() -> None:
    with pytest.raises(ValueError, match="published_rate must be positive"):
        gross_margin_pct(0.0, 650.0)


def test_booking_accuracy_pct_at_the_scorecard_threshold() -> None:
    """Bookings Director KR1 threshold is >= 95%: 10 errored bookings in 200."""
    assert booking_accuracy_pct(200, 10) == pytest.approx(95.0)
    assert booking_accuracy_pct(200, 0) == pytest.approx(100.0)


def test_booking_accuracy_rejects_more_errors_than_bookings() -> None:
    with pytest.raises(ValueError, match="must be between 0 and 200"):
        booking_accuracy_pct(200, 201)


def test_attribution_completeness_reproduces_the_published_counts() -> None:
    """2026 YTD to the Sep 2026 export: 59 of 7,725 bookings unattributed -> 99.24%.
    Full OMS history: 823 of 43,590 -> 98.11%. Totals from
    data/derived/annual-totals.csv (2022-2026 booking column).
    """
    assert attribution_completeness_pct(7_725, 59) == pytest.approx(99.236, abs=0.001)
    assert attribution_completeness_pct(43_590, 823) == pytest.approx(98.112, abs=0.001)


def test_like_for_like_growth_ignores_months_present_in_only_one_period() -> None:
    """Shared months Jan+Feb: 231 against 210 is exactly +10%. The Sep figure in the
    current period and the Dec figure in the prior period are both excluded -- including
    either would produce a growth rate driven by calendar coverage, not by the business.
    """
    current = {"Jan": 110.0, "Feb": 121.0, "Sep": 500.0}
    prior = {"Jan": 100.0, "Feb": 110.0, "Dec": 900.0}
    assert like_for_like_growth_pct(current, prior) == pytest.approx(10.0)


def test_like_for_like_growth_with_no_shared_months_fails_loudly() -> None:
    with pytest.raises(ValueError, match="share no months"):
        like_for_like_growth_pct({"Jan": 1.0}, {"Feb": 1.0})
