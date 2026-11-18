"""Known-answer tests for the partner-routing correction.

Every metric asserted here is hand-computed from the measured bill-to aggregates in
`config/partner-routing-measured-20261118.json`, so a change in the figures breaks
a test rather than silently changing a published number (`CLAUDE.md` §8).

Owner: data-analyst
Date: 2026-11-18
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from analyze_partner_routing import (
    CONFIG_PATH,
    QB_PSEUDO_CUSTOMERS,
    QB_YEAR_HEADER,
    corrected_new_accounts,
    normalize_name,
    partner_rows_by_year,
)

REPO = Path(__file__).resolve().parent.parent


@pytest.fixture(scope="module")
def measured() -> dict:
    return json.loads(CONFIG_PATH.read_text())


# --- the exclusion rules ----------------------------------------------------


def test_corrected_new_accounts_hand_computed() -> None:
    """418 homes less 121 / 125 / 129 partner-billed under each rule."""
    fixture = {
        "new_accounts_window": {
            "homes": 418,
            "purely_partner_billed_homes": 121,
            "first_booking_partner_billed_homes": 125,
            "partner_billed_homes": 129,
        }
    }
    assert corrected_new_accounts(fixture) == {
        "ever_billed_directly": 297,
        "first_booking_direct": 293,
        "no_partner_booking": 289,
    }


def test_corrected_new_accounts_small_fixture() -> None:
    """A ten-home fixture computed by hand: 10 - 3 / 4 / 5."""
    fixture = {
        "new_accounts_window": {
            "homes": 10,
            "purely_partner_billed_homes": 3,
            "first_booking_partner_billed_homes": 4,
            "partner_billed_homes": 5,
        }
    }
    assert corrected_new_accounts(fixture) == {
        "ever_billed_directly": 7,
        "first_booking_direct": 6,
        "no_partner_booking": 5,
    }


def test_rules_are_monotonic(measured: dict) -> None:
    """The stricter the rule, the fewer genuine new accounts it admits."""
    rules = corrected_new_accounts(measured)
    assert (
        rules["no_partner_booking"]
        <= rules["first_booking_direct"]
        <= rules["ever_billed_directly"]
    )


def test_published_figure_is_not_reproduced_by_any_rule(measured: dict) -> None:
    """No exclusion rule returns 411. The published figure was wrong, not a rounding."""
    assert 411 not in set(corrected_new_accounts(measured).values())


def test_partner_share_of_new_accounts_is_about_31_percent(measured: dict) -> None:
    """Donald's mechanism is real; his 80%+ magnitude is not. Both halves matter."""
    window = measured["new_accounts_window"]
    share = window["partner_billed_homes"] / window["homes"]
    assert 0.30 < share < 0.32
    assert share < 0.80, "if this ever reaches 80% Donald's estimate was right after all"


# --- internal consistency of the measured aggregates ------------------------


def test_new_account_subsets_carry_a_known_four_home_gap(measured: dict) -> None:
    """121 purely-partner + 4 also-direct = 125, against 129 partner-billed.

    Four homes are in neither subset. The relayed aggregates do not say why; the
    likeliest cause is the 19 since-deleted funeral home records carrying 88
    unattributable bookings. The gap is asserted here rather than smoothed over,
    so it stays visible until the per-home manifest resolves it. It is too small
    to move any corrected figure: 4 homes on a basis of 418 is 1.0%.
    """
    w = measured["new_accounts_window"]
    accounted = w["purely_partner_billed_homes"] + w["also_billed_directly_homes"]
    gap = w["partner_billed_homes"] - accounted
    assert gap == 4, "the unreconciled gap changed; re-check the relayed aggregates"
    assert gap / w["homes"] < 0.02


def test_new_account_subsets_are_bounded(measured: dict) -> None:
    """Partner-billed homes and bookings cannot exceed the cohort they sit in."""
    w = measured["new_accounts_window"]
    assert w["partner_billed_bookings"] <= w["bookings"]
    assert w["partner_billed_homes"] <= w["homes"]
    assert w["purely_partner_billed_homes"] <= w["partner_billed_homes"]


def test_new_account_per_partner_homes_sum_to_the_overlapping_total(measured: dict) -> None:
    """NMS 72 + IMS 43 + Bergen 14 = 129, so no new home used two partners."""
    w = measured["new_accounts_window"]
    assert sum(w["by_partner_homes"].values()) == w["partner_billed_homes"]


def test_all_partner_homes_partition(measured: dict) -> None:
    """535 homes split into 414 purely-partner and 121 that also bill direct."""
    block = measured["all_partner_billed_2022_2026"]
    assert block["purely_partner_billed_homes"] + block["homes_also_self_billed"] == (
        block["homes"]
    )
    assert block["homes_self_billed_gte_partner_billed"] <= block["homes_also_self_billed"]


def test_per_partner_bookings_sum_to_total(measured: dict) -> None:
    """NMS 523 + IMS 2,514 + Bergen 124 = 3,161 bookings."""
    block = measured["all_partner_billed_2022_2026"]
    assert sum(p["bookings"] for p in block["by_partner"].values()) == block["bookings"]


def test_per_partner_homes_overlap_is_consistent_with_multi_partner_homes(
    measured: dict,
) -> None:
    """266 + 257 + 52 = 575 home-slots against 535 distinct homes: 40 of overlap.

    A home using two partners contributes 1 to the overlap, a home using all three
    contributes 2. So with 38 multi-partner homes the overlap must lie between 38
    and 76; 40 implies 36 two-partner homes and 2 three-partner homes. This is a
    consistency band, not an equality -- the earlier version of this test asserted
    equality and was simply wrong about the arithmetic.
    """
    block = measured["all_partner_billed_2022_2026"]
    summed = sum(p["homes"] for p in block["by_partner"].values())
    overlap = summed - block["homes"]
    multi = block["homes_with_multiple_partners"]
    assert overlap == 40
    assert multi <= overlap <= 2 * multi


def test_by_year_bookings_reconcile_to_the_five_year_total(measured: dict) -> None:
    """The by-year series must sum to the 3,161 lifetime figure."""
    rows = partner_rows_by_year(measured)
    assert sum(int(r["bookings_total"]) for r in rows) == (
        measured["all_partner_billed_2022_2026"]["bookings"]
    )


def test_by_year_rows_are_hand_checked(measured: dict) -> None:
    """2026: NMS 177 + IMS 569 + Bergen 47 = 793 bookings, 254 home-slots."""
    rows = {r["year"]: r for r in partner_rows_by_year(measured)}
    assert rows["2026"]["bookings_total"] == 793
    assert rows["2026"]["homes_upper_bound"] == 254
    assert rows["2023"]["bookings_total"] == 767


def test_partner_volume_is_flat_while_homes_rotate(measured: dict) -> None:
    """The finding that matters: volume stable, home count churning upward.

    IMS routed 652 bookings across 108 homes in 2023 and 569 across 104 in 2026 --
    but 257 distinct IMS homes appear over five years. The volume persists; the
    originating names rotate. That rotation inflates measured acquisition and
    measured churn at the same time.
    """
    block = measured["by_year_homes_bookings"]
    ims_bookings = block["IMS"]["bookings"]
    ims_homes_per_year = block["IMS"]["homes"]
    distinct_ims_homes = measured["all_partner_billed_2022_2026"]["by_partner"]["IMS"]["homes"]
    # volume within 15% across the four full years
    full_years = ims_bookings[1:]
    assert max(full_years) / min(full_years) < 1.15
    # yet distinct homes over the period far exceed any single year's count
    assert distinct_ims_homes > max(ims_homes_per_year) * 2


# --- the QuickBooks traps ---------------------------------------------------


def test_total_row_is_excluded() -> None:
    """The `TOTAL` pseudo-customer row doubles every annual figure if admitted."""
    assert "TOTAL" in QB_PSEUDO_CUSTOMERS
    assert "ALREADY PAID" in QB_PSEUDO_CUSTOMERS


@pytest.mark.parametrize("header", ["2016", "2026", "1999"])
def test_year_header_accepted(header: str) -> None:
    assert QB_YEAR_HEADER.match(header)


@pytest.mark.parametrize("header", ["Total", "total", "", "20262", "Q1", "2026 "])
def test_non_year_header_rejected(header: str) -> None:
    """`Total` is a formula column; summing it doubles lifetime revenue exactly."""
    assert not QB_YEAR_HEADER.match(header)


def test_total_column_would_exactly_double() -> None:
    """Hand-computed: a Total column equal to the row sum doubles the total."""
    row = ("Some Funeral Home", 100.0, 200.0, 300.0, 600.0)
    header = ("", "2024", "2025", "2026", "Total")
    year_cols = [i for i, h in enumerate(header) if h and QB_YEAR_HEADER.match(str(h))]
    assert sum(row[i] for i in year_cols) == 600.0
    naive = sum(v for v in row[1:] if isinstance(v, float))
    assert naive == 1200.0 == 2 * 600.0


# --- name normalization -----------------------------------------------------


def test_normalize_name_doctests() -> None:
    assert normalize_name("Jorge Rivera Funeral Home, Inc.") == "jorge rivera funeral home"
    assert normalize_name("The Highlands Funeral Home") == "highlands funeral home"


def test_normalize_name_keeps_location_parentheticals() -> None:
    """Two SCI locations must not collapse onto one another."""
    a = normalize_name("Kraeer Funeral Home (SCI Location #4356)")
    b = normalize_name("Kraeer Funeral Home (SCI Location #7098)")
    assert a != b


def test_partner_suffix_marker_is_not_a_reliable_identifier() -> None:
    """The `(NMS)`/`(IMS)` naming convention exists but is applied ad hoc.

    It catches 40 homes against 535 measured, so it must never be used as the
    identifier. This test documents that, so nobody reaches for it again.
    """
    pattern = re.compile(r"\(\s*(NMS|IMS)\b", re.IGNORECASE)
    assert pattern.search("STROWDERS FUNERAL HOME (NMS)")
    assert pattern.search("SHELLHOUSE- RIVERS FUNERAL HOME  (IMS)")
    assert not pattern.search("Beasley Funeral Home")


# --- the published figures being corrected ----------------------------------


def test_published_baseline_matches_the_derived_file(measured: dict) -> None:
    """Guard against the config drifting from the file it claims to correct."""
    path = REPO / "data" / "derived" / "rolling-window-account-metrics.csv"
    if not path.exists():
        pytest.skip("rolling-window-account-metrics.csv not present")
    import csv as _csv

    with path.open() as fh:
        row = {r["as_of"]: r for r in _csv.DictReader(fh)}["2026-11-10"]
    pub = measured["published_figures_being_corrected"]
    assert int(row["new_accounts"]) == pub["new_accounts"] == 411
    assert int(row["active_accounts"]) == pub["active_accounts"] == 1091
    assert int(row["churned_accounts"]) == pub["churned_accounts"] == 318
    assert int(row["bookings_in_window"]) == pub["bookings_in_window"] == 10943
