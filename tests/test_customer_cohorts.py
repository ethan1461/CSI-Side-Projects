"""Known-answer tests for the customer cohort metrics.

Every metric reported in `reports/customer-cohort-analysis.md` is computed by a
function tested here against a hand-built fixture whose answer is worked out by
hand in the test. A metric with no known-answer test is a metric nobody should
trust (`CLAUDE.md` §8).

Owner: data-analyst
Date: 2026-11-12
"""

from __future__ import annotations

import sys
from collections import Counter
from datetime import date
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from analyze_customer_cohorts import (
    BASE_YEAR,
    Account,
    Booking,
    account_year_bookings,
    annualisation_factor,
    base_decay_rows,
    corporate_group,
    decompose_years,
    first_to_second,
    hhi,
    is_partner,
    join_revenue_to_accounts,
    normalize_name,
    partner_share_rows,
    retention_matrix,
    sales_lists,
    sort_value,
    top_n_share,
)

# --- fixture -----------------------------------------------------------------
#
# Four accounts, hand-built so every cohort answer can be worked out on paper.
#
#   A: 2 bookings in 2023, 3 in 2024, 1 in 2025        -> retained throughout
#   B: 1 booking in 2023 only                          -> churns into 2024
#   C: first booking 2024 (2), none 2025, 1 in 2026    -> new in 2024, reactivated 2026
#   D: first and only booking 2025                     -> new in 2025, one-and-done

FIXTURE: list[Booking] = [
    Booking(1, "A", date(2023, 3, 1), "Booked"),
    Booking(2, "A", date(2023, 11, 20), "Booked"),
    Booking(3, "A", date(2024, 2, 1), "Booked"),
    Booking(4, "A", date(2024, 6, 1), "Booked"),
    Booking(5, "A", date(2024, 12, 15), "Booked"),
    Booking(6, "A", date(2025, 5, 1), "Booked"),
    Booking(7, "B", date(2023, 4, 1), "Booked"),
    Booking(8, "C", date(2024, 1, 10), "Booked"),
    Booking(9, "C", date(2024, 9, 10), "Booked"),
    Booking(10, "C", date(2026, 2, 2), "Booked"),
    Booking(11, "D", date(2025, 6, 1), "Booked"),
]


def test_account_year_bookings_known_answer() -> None:
    """Counted by hand from the fixture."""
    by_year = account_year_bookings(FIXTURE)
    assert dict(by_year[2023]) == {"A": 2, "B": 1}
    assert dict(by_year[2024]) == {"A": 3, "C": 2}
    assert dict(by_year[2025]) == {"A": 1, "D": 1}
    assert dict(by_year[2026]) == {"C": 1}


def test_like_for_like_window_drops_november_and_december() -> None:
    """A's 2023-11-20 and 2024-12-15 bookings fall outside a Jan-Oct window."""
    by_year = account_year_bookings(FIXTURE, last_month=10)
    assert dict(by_year[2023]) == {"A": 1, "B": 1}
    assert dict(by_year[2024]) == {"A": 2, "C": 2}


def test_decomposition_identity_holds_on_every_year() -> None:
    """new + reactivated + retained delta - churned must equal the volume change.

    This identity is the whole argument of the report. If it does not hold, the
    decomposition is not a decomposition.
    """
    for row in decompose_years(account_year_bookings(FIXTURE)):
        reconstructed = (
            int(row["bookings_from_new"])
            + int(row["bookings_from_reactivated"])
            + int(row["retained_bookings_delta"])
            - int(row["churned_bookings_prior_year"])
        )
        assert reconstructed == int(row["bookings_delta_vs_prior"]), row["year"]


def test_decomposition_2024_known_answer() -> None:
    """Worked by hand: A retained 2->3, B churns with 1, C is new with 2."""
    rows = {int(r["year"]): r for r in decompose_years(account_year_bookings(FIXTURE))}
    row = rows[2024]
    assert row["active_accounts"] == 2
    assert row["bookings"] == 5
    assert row["new_accounts"] == 1
    assert row["bookings_from_new"] == 2
    assert row["reactivated_accounts"] == 0
    assert row["retained_accounts"] == 1
    assert row["retained_bookings_prior_year"] == 2
    assert row["retained_bookings_now"] == 3
    assert row["retained_bookings_delta"] == 1
    assert row["churned_accounts"] == 1
    assert row["churned_bookings_prior_year"] == 1
    # Two accounts active in 2023, one survived.
    assert row["gross_churn_rate_pct"] == 50.0
    assert row["logo_retention_rate_pct"] == 50.0
    assert row["bookings_delta_vs_prior"] == 2


def test_decomposition_2026_counts_c_as_reactivated_not_new() -> None:
    """C shipped in 2024, skipped 2025 and returned in 2026: reactivated, not new."""
    rows = {int(r["year"]): r for r in decompose_years(account_year_bookings(FIXTURE))}
    row = rows[2026]
    assert row["new_accounts"] == 0
    assert row["reactivated_accounts"] == 1
    assert row["bookings_from_reactivated"] == 1
    # A and D were active in 2025 and both disappear in 2026.
    assert row["churned_accounts"] == 2
    assert row["churned_bookings_prior_year"] == 2


def test_retention_matrix_known_answer() -> None:
    """The 2023 cohort is {A, B}; only A survives into 2024."""
    rows = {
        (int(r["cohort_year"]), int(r["year"])): r
        for r in retention_matrix(account_year_bookings(FIXTURE))
    }
    assert rows[(2023, 2023)]["cohort_size"] == 2
    assert rows[(2023, 2023)]["bookings"] == 3
    assert rows[(2023, 2024)]["accounts_active"] == 1
    assert rows[(2023, 2024)]["pct_accounts_active"] == 50.0
    # A contributed 3 bookings in 2024 against the cohort's 3 in 2023.
    assert rows[(2023, 2024)]["bookings_index_vs_first_year"] == 100.0
    assert rows[(2024, 2025)]["accounts_active"] == 0


def test_first_to_second_known_answer() -> None:
    """A re-books 264 days later; B never; C after 244 days; D never."""
    rows = {int(r["cohort_year"]): r for r in first_to_second(FIXTURE)}
    assert rows[2023]["accounts"] == 2
    assert rows[2023]["accounts_with_second_booking_ever"] == 1
    assert rows[2023]["pct_with_second_booking_ever"] == 50.0
    assert rows[2023]["median_days_to_second"] == (date(2023, 11, 20) - date(2023, 3, 1)).days
    # A's second booking is 264 days out: inside 365, outside 180.
    assert rows[2023]["pct_second_within_365d"] == 50.0
    assert rows[2023]["pct_second_within_180d"] == 0.0
    assert rows[2025]["accounts"] == 1
    assert rows[2025]["pct_with_second_booking_ever"] == 0.0


def test_first_to_second_excludes_accounts_too_young_to_judge() -> None:
    """An account acquired three days before the cut cannot fail a 90-day window."""
    bookings = FIXTURE + [Booking(99, "E", date(2026, 11, 7), "Booked")]
    rows = {int(r["cohort_year"]): r for r in first_to_second(bookings)}
    # E is the only 2026 cohort member -- C's first booking was in 2024. Three days
    # before the cut, E is in the denominator of nothing.
    assert rows[2026]["accounts"] == 1
    assert rows[2026]["eligible_90d"] == 0
    assert rows[2026]["eligible_365d"] == 0
    assert rows[2026]["pct_second_within_90d"] is None
    assert rows[2026]["pct_second_within_365d"] is None
    # But E still counts as an account with no second booking yet.
    assert rows[2026]["pct_with_second_booking_ever"] == 0.0


def test_annualisation_factor_known_answer() -> None:
    """Three bookings in the year, two on or before 10 November: factor 3/2."""
    bookings = [
        Booking(1, "A", date(2024, 1, 1), "Booked"),
        Booking(2, "A", date(2024, 6, 1), "Booked"),
        Booking(3, "A", date(2024, 12, 1), "Booked"),
    ]
    assert annualisation_factor(bookings, (2024,)) == pytest.approx(1.5)


def test_annualisation_factor_refuses_when_no_reference_year() -> None:
    with pytest.raises(ValueError, match="no reference years"):
        annualisation_factor(FIXTURE, (2019,))


def test_base_decay_bands_reconcile_to_the_total() -> None:
    """Every band plus the new-since row must sum to all accounts.

    The table is only an argument if it adds up.
    """
    rows = {str(r["segment"]): r for r in base_decay_rows(account_year_bookings(FIXTURE), 1.0)}
    banded = sum(int(rows[s]["accounts"]) for s in rows if s[0] in "12345")
    assert banded == int(rows[f"6 base {BASE_YEAR} total"]["accounts"])
    assert int(rows[f"6 base {BASE_YEAR} total"]["accounts"]) + int(
        rows[f"7 accounts absent in {BASE_YEAR}"]["accounts"]
    ) == int(rows["8 all accounts"]["accounts"])
    for year in (2023, 2024, 2025, 2026):
        key = f"bookings_{year}"
        assert int(rows[f"6 base {BASE_YEAR} total"][key]) + int(
            rows[f"7 accounts absent in {BASE_YEAR}"][key]
        ) == int(rows["8 all accounts"][key])


def test_sales_lists_known_answer() -> None:
    """A is at risk (3 bookings in 2024, 0 in 2026); D is one-and-done."""
    accounts = {
        name: Account(name, f"{name} Funeral Home", "NY", "Independent", "")
        for name in ("A", "B", "C", "D")
    }
    by_year = account_year_bookings(FIXTURE)
    # Threshold of 12 bookings would exclude the whole fixture, so patch it down.
    import analyze_customer_cohorts as module

    original = module.AT_RISK_MIN_PRIOR_BOOKINGS
    module.AT_RISK_MIN_PRIOR_BOOKINGS = 3
    try:
        at_risk, dormant, one_and_done = sales_lists(FIXTURE, by_year, accounts, 1.0)
    finally:
        module.AT_RISK_MIN_PRIOR_BOOKINGS = original

    assert [r["funeral_home_id"] for r in at_risk] == ["A"]
    assert at_risk[0]["bookings_at_stake_vs_prior"] == 3
    assert at_risk[0]["retention_pct"] == 0.0
    # D's only booking was 2025-06-01, well over 120 days before the cut.
    assert [r["funeral_home_id"] for r in one_and_done] == ["D"]
    # Nobody clears the five-booking dormancy bar in this fixture.
    assert dormant == []


def test_partner_share_known_answer() -> None:
    revenue = {
        "Bergen Funeral Service (New Jersey)": {2025: 600.0},
        "Ponce Funeral Home": {2025: 200.0},
        "Smith Funeral Home": {2025: 200.0},
    }
    row = partner_share_rows(revenue)[0]
    assert row["revenue"] == 1000.0
    assert row["partner_tier_share_pct"] == 60.0
    assert row["bergen_group_share_pct"] == 60.0
    assert row["ortiz_group_share_pct"] == 20.0


def test_top_n_share_and_hhi_known_answers() -> None:
    assert top_n_share([40.0, 30.0, 20.0, 10.0], 2) == pytest.approx(0.70)
    assert top_n_share([5.0], 10) == pytest.approx(1.0)
    assert top_n_share([0.0, 0.0], 1) == 0.0
    # Four equal shares of 25%: 4 * 0.0625 * 10000.
    assert hhi([1.0, 1.0, 1.0, 1.0]) == pytest.approx(2500.0)


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("International Mortuary Shipping, LLC", "international mortuary shipping"),
        ("W.H. Bacon Funeral Home, Inc.", "w h bacon funeral home"),
        ("The Highlands Funeral Home", "highlands funeral home"),
        # Location numbers must survive: these are different homes.
        ("Kraeer Funeral Home (SCI Location #4356)", "kraeer funeral home (sci location #4356)"),
        ("Kraeer Funeral Home (SCI Location #7098)", "kraeer funeral home (sci location #7098)"),
    ],
)
def test_normalize_name(raw: str, expected: str) -> None:
    assert normalize_name(raw) == expected


def test_different_sci_locations_do_not_collapse() -> None:
    """The join must never merge two SCI locations of the same brand."""
    assert normalize_name("Forest Lawn (SCI Location #4365)") != normalize_name(
        "Forest Lawn (SCI Location #4416)"
    )


def test_corporate_group_prefers_the_oms_field() -> None:
    assert corporate_group("Anything", "Foundation Partners") == "Foundation Partners"
    assert corporate_group("Forest Lawn (SCI Location #1)", "") == "SCI"
    assert corporate_group("Smith Funeral Home", "") == "Independent"


def test_partner_detection() -> None:
    assert is_partner("Bergen Funeral Service (Florida)")
    assert is_partner("NATIONAL MORTUARY SHIPPING")
    assert not is_partner("Smith Funeral Home")


def test_ambiguous_name_is_left_unjoined_rather_than_guessed() -> None:
    """Two unrelated accounts sharing a name must not be joined to revenue."""
    accounts = {
        "1": Account("1", "Smith Funeral Home", "NY", "Independent", ""),
        "2": Account("2", "Smith Funeral Home", "TX", "Independent", ""),
        "3": Account("3", "Jones Funeral Home", "FL", "Independent", "dup-7"),
        "4": Account("4", "Jones Funeral Home", "FL", "Independent", "dup-7"),
    }
    index = {"smith funeral home": ["1", "2"], "jones funeral home": ["3", "4"]}
    joined, tally = join_revenue_to_accounts(
        ["Smith Funeral Home", "Jones Funeral Home", "Absent Funeral Home"], index, accounts
    )
    assert "Smith Funeral Home" not in joined
    assert tally["unmatched_ambiguous"] == 1
    # Jones is two records of the same home, so it joins to both.
    assert joined["Jones Funeral Home"] == ["3", "4"]
    assert tally["matched_via_duplicate_group"] == 1
    assert tally["unmatched_no_account"] == 1


def test_sort_value_orders_numbers_numerically() -> None:
    """Guards the output ordering: "10" must not sort before "9"."""
    assert sorted([9, 10, 100], key=sort_value) == [9, 10, 100]
    assert sort_value(None) > sort_value("zzz")
    assert sort_value("a") > sort_value(10**9)


def test_decomposition_handles_an_empty_prior_year() -> None:
    """The first year on record has no prior year and must not divide by zero."""
    rows = decompose_years({2023: Counter({"A": 1})})
    assert rows[0]["gross_churn_rate_pct"] is None
    assert rows[0]["logo_retention_rate_pct"] is None


# --- the canonical rolling-window figures -----------------------------------
#
# A second fixture, built so the published churn figures can be checked by hand.
# as_of = 2024-11-10, so current = (2023-11-10, 2024-11-10] and
# prior = (2022-11-10, 2023-11-10].
#
#   P: 5 bookings prior, 5 current   -> retained, frequent (>=4 prior)
#   Q: 2 bookings prior, 0 current   -> churned, infrequent
#   R: 6 bookings prior, 0 current   -> churned, frequent
#   S: 0 prior, 1 current, no history -> new

ROLLING_AS_OF = date(2024, 11, 10)


def _spread(account: str, year: int, month: int, count: int) -> list[Booking]:
    return [Booking(0, account, date(year, month, day), "Booked") for day in range(1, count + 1)]


ROLLING_FIXTURE: list[Booking] = (
    _spread("P", 2023, 6, 5)
    + _spread("P", 2024, 6, 5)
    + _spread("Q", 2023, 6, 2)
    + _spread("R", 2023, 6, 6)
    + _spread("S", 2024, 6, 1)
)


def test_rolling_window_known_answer() -> None:
    """Every figure here is counted by hand from ROLLING_FIXTURE."""
    from analyze_customer_cohorts import rolling_window_rows

    row = rolling_window_rows(ROLLING_FIXTURE, (ROLLING_AS_OF,))[0]
    assert row["window_days"] == 365
    assert row["active_accounts"] == 2  # P and S
    assert row["bookings_in_window"] == 6  # P's 5 plus S's 1
    assert row["new_accounts"] == 1
    assert row["reactivated_accounts"] == 0
    assert row["retained_accounts"] == 1
    assert row["churned_accounts"] == 2  # Q and R
    # Three accounts were active in the prior window; two did not return.
    assert row["churn_rate_count_pct"] == pytest.approx(66.67, abs=0.01)
    # Weighted by prior volume: (2 + 6) / (5 + 2 + 6).
    assert row["churn_rate_volume_weighted_pct"] == pytest.approx(61.54, abs=0.01)
    assert row["bookings_lost_to_churn"] == 8
    assert row["shipments_per_retained_account"] == 5.0


def test_rolling_window_size_split_known_answer() -> None:
    """The split M-15 requires: R is frequent and churned, Q is infrequent and churned."""
    from analyze_customer_cohorts import rolling_window_rows

    row = rolling_window_rows(ROLLING_FIXTURE, (ROLLING_AS_OF,))[0]
    assert row["frequent_prior_active"] == 2  # P with 5, R with 6
    assert row["frequent_churned"] == 1
    assert row["frequent_churn_rate_pct"] == 50.0
    assert row["frequent_bookings_lost"] == 6
    assert row["infrequent_prior_active"] == 1  # Q with 2
    assert row["infrequent_churned"] == 1
    assert row["infrequent_churn_rate_pct"] == 100.0
    assert row["infrequent_bookings_lost"] == 2
    # The two splits must partition the churn denominator exactly.
    assert row["frequent_prior_active"] + row["infrequent_prior_active"] == 3
    assert row["frequent_churned"] + row["infrequent_churned"] == row["churned_accounts"]
    assert (
        row["frequent_bookings_lost"] + row["infrequent_bookings_lost"]
        == row["bookings_lost_to_churn"]
    )


def test_rolling_window_refuses_a_date_without_enough_history() -> None:
    """Two full windows of history are required, or churn is unmeasurable."""
    from analyze_customer_cohorts import rolling_window_rows

    with pytest.raises(ValueError, match="Cannot classify accounts"):
        rolling_window_rows(ROLLING_FIXTURE, (date(2023, 6, 1),))


def test_base_attrition_identity_and_known_answer() -> None:
    """The three effects must sum to the net change, or it is not a decomposition.

    From FIXTURE: the 2023 base is {A, B}, neither ships in 2026, so 3 bookings
    leave with stopped accounts and nothing remains to shrink. C contributes the
    one 2026 booking and was acquired after 2023.
    """
    from analyze_customer_cohorts import base_attrition_rows

    rows = {
        str(r["effect"])[0]: r for r in base_attrition_rows(account_year_bookings(FIXTURE), 1.0)
    }
    assert rows["1"]["accounts"] == 2
    assert rows["1"]["bookings_change"] == -3
    assert rows["2"]["accounts"] == 0
    assert rows["2"]["bookings_change"] == 0
    assert rows["3"]["accounts"] == 2  # C and D
    assert rows["3"]["bookings_change"] == 1
    assert rows["4"]["bookings_change"] == -2
    assert (
        rows["1"]["bookings_change"] + rows["2"]["bookings_change"] + rows["3"]["bookings_change"]
        == rows["4"]["bookings_change"]
    )


def test_base_attrition_separates_a_shrinking_survivor_from_a_stopped_account() -> None:
    """A survivor at half its base volume must land in effect 2, not effect 1."""
    from analyze_customer_cohorts import base_attrition_rows

    by_year = {
        2023: Counter({"big": 10, "quit": 4}),
        2026: Counter({"big": 5, "fresh": 3}),
    }
    rows = {str(r["effect"])[0]: r for r in base_attrition_rows(by_year, 1.0)}
    assert rows["1"]["accounts"] == 1 and rows["1"]["bookings_change"] == -4
    assert rows["2"]["accounts"] == 1 and rows["2"]["bookings_change"] == -5
    assert "0 grew by 0, 1 shrank by 5" in str(rows["2"]["note"])
    assert rows["3"]["accounts"] == 1 and rows["3"]["bookings_change"] == 3
    assert rows["4"]["bookings_change"] == -6
