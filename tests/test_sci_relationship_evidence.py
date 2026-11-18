"""Known-answer tests for `scripts/sci_relationship_evidence.py`.

Every metric function gets at least one hand-computed fixture, per `CLAUDE.md` §8.
The tests at the end pin the published figures: if the SCI footprint numbers that
go into `reports/sci-relationship-evidence.md` ever move, these fail and someone
has to look at why.

Owner: data-analyst
Date: 2026-11-18
"""

from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.sci_relationship_evidence import (
    OmsAccount,
    SciLocation,
    annualisation_factor,
    concentration_rows,
    definition_reconciliation_rows,
    denominator_rows,
    footprint_rows,
    geography_rows,
    match_tier_rows,
    normalize_join_name,
    normalize_location_code,
    normalize_phone,
    normalize_revenue_name,
    parse_month_day,
    parse_year,
    partner_routed_rows,
    savings_sensitivity_rows,
    trajectory_rows,
    trajectory_summary_rows,
    unlabelled_location_rows,
)

# --- normalisation ----------------------------------------------------------


@pytest.mark.parametrize(
    ("raw", "strip_prefix", "expected"),
    [
        ("4356 - KRAEER FUNERAL HOME", True, "kraeer"),
        ("Kraeer Funeral Home (SCI Location #4356)", False, "kraeer"),
        ("Boardman-Smith Funeral Home, Inc.", False, "boardman smith"),
        (
            "Star of David Memorial Gardens Cemetery & Funeral Chapel",
            False,
            "star david",
        ),
        ("", False, ""),
    ],
)
def test_normalize_join_name_known_answers(
    raw: str, strip_prefix: bool, expected: str
) -> None:
    assert normalize_join_name(raw, strip_code_prefix=strip_prefix) == expected


def test_normalize_join_name_collapses_the_two_systems_onto_one_key() -> None:
    """The whole cross-system join rests on this pair agreeing."""
    register = normalize_join_name(
        "3597 - FRED HUNTER'S FUNERAL HOME", strip_code_prefix=True
    )
    oms = normalize_join_name("Fred Hunter's Funeral Home (SCI Location #3597)")
    assert register == oms == "fred hunter s"


def test_normalize_revenue_name_keeps_the_location_number() -> None:
    """Two SCI chapels can share a trade name; the location number separates them."""
    a = normalize_revenue_name("Riverside Chapels (SCI Location #4222)")
    b = normalize_revenue_name("Riverside Chapels (SCI Location #4128)")
    assert a != b
    assert a == "riverside chapels (sci location #4222)"


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("(713) 522-5141", "7135225141"),
        ("1-713-522-5141", "7135225141"),
        ("7135225141", "7135225141"),
        ("0049-2642 9057910", ""),  # non-NANP: must not become a join key
        ("", ""),
        (None, ""),
    ],
)
def test_normalize_phone_known_answers(raw: object, expected: str) -> None:
    assert normalize_phone(raw) == expected


@pytest.mark.parametrize(
    ("raw", "expected"),
    [("0672", "672"), (4873, "4873"), ("0000", "0"), ("", ""), (None, "")],
)
def test_normalize_location_code_known_answers(raw: object, expected: str) -> None:
    assert normalize_location_code(raw) == expected


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("2024-03-11", 2024),
        ("2060-02-02", 2060),
        ("", None),
        (None, None),
        ("not a date", None),
    ],
)
def test_parse_year_known_answers(raw: object, expected: int | None) -> None:
    assert parse_year(raw) == expected


@pytest.mark.parametrize(
    ("raw", "expected"),
    [("2026-11-10", (11, 10)), ("2026-11-11", (11, 11)), ("2026", None), (None, None)],
)
def test_parse_month_day_known_answers(
    raw: object, expected: tuple[int, int] | None
) -> None:
    assert parse_month_day(raw) == expected


def test_parse_month_day_boundary_is_the_data_cut() -> None:
    """The cut is inclusive of 10 November and exclusive of 11 November."""
    assert parse_month_day("2026-11-10") <= (11, 10)
    assert parse_month_day("2026-11-11") > (11, 10)


# --- annualisation ----------------------------------------------------------


def test_annualisation_factor_known_answer() -> None:
    assert round(annualisation_factor(1000, 866), 4) == 1.1547


def test_annualisation_factor_rejects_zero_denominator() -> None:
    with pytest.raises(ValueError, match="positive"):
        annualisation_factor(1000, 0)


# --- fixtures ---------------------------------------------------------------


def _location(**kwargs: object) -> SciLocation:
    defaults: dict[str, object] = {
        "name": "0001 - A CHAPEL",
        "city": "HOUSTON",
        "state": "TX",
        "location_code": "1",
        "location_id": "00001",
        "location_type": "Operating",
        "product_line": "Funeral Home Product Line",
        "business_line": "Funeral",
    }
    defaults.update(kwargs)
    return SciLocation(**defaults)  # type: ignore[arg-type]


def _account(account_id: str, **kwargs: object) -> OmsAccount:
    defaults: dict[str, object] = {
        "name": f"Home {account_id} (SCI Location #{account_id})",
        "city": "MIAMI",
        "state": "FL",
        "group_field": "SCI",
        "sci_flagged": True,
        "sci_code": account_id,
    }
    defaults.update(kwargs)
    return OmsAccount(account_id=account_id, **defaults)  # type: ignore[arg-type]


# --- denominator ------------------------------------------------------------


def test_denominator_rows_separate_places_from_accounting_structures() -> None:
    """Hand fixture: 5 rows, of which 2 are operating funeral homes."""
    locations = [
        _location(location_code="1"),
        _location(location_code="2"),
        _location(
            location_code="3",
            location_type="Legal Posting Location",
            business_line="Cemetery",
        ),
        _location(
            location_code="4",
            product_line="Cemetery Product Line",
            business_line="Cemetery",
        ),
        _location(
            location_code="5",
            location_type="Overhead",
            business_line="Corporate Segment",
        ),
    ]
    rows = {str(row["denominator"]): row for row in denominator_rows(locations)}
    assert rows["all_register_rows"]["locations"] == 5
    assert rows["operating_locations"]["locations"] == 3
    assert rows["operating_funeral_business_line"]["locations"] == 2
    assert rows["operating_shipping_capable_product_lines"]["locations"] == 2
    assert rows["operating_cemetery_product_line"]["locations"] == 1
    assert rows["operating_locations"]["pct_of_register"] == 60.0


# --- match tiers ------------------------------------------------------------


def test_match_tier_property_ranks_signals_in_order() -> None:
    account = _account("100")
    account.match_methods = {"code", "phone_shared"}
    assert account.match_tier == "T1_location_code"
    account.match_methods = {"name_zip", "phone_unique"}
    assert account.match_tier == "T2_name_zip_and_phone"
    account.match_methods = {"phone_unique"}
    assert account.match_tier == "T3_single_signal"
    account.match_methods = {"phone_shared"}
    assert account.match_tier == "T4_shared_phone"
    account.match_methods = set()
    assert account.match_tier == "T0_no_register_match"


def test_shared_phone_alone_is_never_counted_as_sci() -> None:
    """1,276 register rows carry SCI's Houston head-office number."""
    account = _account(
        "200", sci_flagged=False, group_field="", name="Smith Funeral Home"
    )
    account.match_methods = {"phone_shared"}
    assert account.is_sci is False
    account.match_methods = {"phone_unique"}
    assert account.is_sci is True


def test_strict_rule_reproduces_the_cohort_report_definition() -> None:
    labelled = _account("300", group_field="", name="Kraeer FH (SCI Location #4356)")
    group_only = _account("301", group_field="SCI", name="Neptune Society")
    marker_only = _account(
        "302", group_field="", name="Kennedy Roth Funeral Home (SCI)"
    )
    assert labelled.is_sci_strict is True
    assert group_only.is_sci_strict is True
    # The strict rule deliberately misses a bare "(SCI)" with no location code --
    # which is why the wide rule exists and why the two are reconciled.
    assert marker_only.is_sci_strict is False
    assert marker_only.sci_flagged is True


def test_match_tier_rows_excludes_the_unrelated_majority() -> None:
    accounts = {
        "1": _account("1"),
        "2": _account("2", sci_flagged=False, group_field="", name="Unrelated Home"),
    }
    accounts["1"].match_methods = {"code"}
    accounts["2"].match_methods = set()
    rows = match_tier_rows(accounts, {"1": Counter({2025: 4})})
    assert len(rows) == 1
    assert rows[0]["bookings_all_years"] == 4
    assert rows[0]["shipping_accounts"] == 1
    assert rows[0]["counted_as_sci"] == "yes"


# --- footprint --------------------------------------------------------------


def test_footprint_rows_known_answer() -> None:
    """Three locations: hand-computed counts, averages and the cumulative column."""
    accounts = [_account("1"), _account("2"), _account("3")]
    bookings = {
        "1": Counter({2024: 10, 2025: 12}),
        "2": Counter({2025: 4}),
        "3": Counter({2026: 6}),
    }
    rows = {int(row["year"]): row for row in footprint_rows(accounts, bookings, 2.0)}
    assert rows[2024]["shipping_locations"] == 1
    assert rows[2024]["bookings"] == 10
    assert rows[2024]["locations_ever_shipped_by_end_of_year"] == 1
    assert rows[2025]["shipping_locations"] == 2
    assert rows[2025]["bookings"] == 16
    assert rows[2025]["bookings_per_location"] == 8.0
    assert rows[2025]["locations_ever_shipped_by_end_of_year"] == 2
    assert rows[2026]["bookings"] == 6
    assert rows[2026]["bookings_annualised"] == 12.0
    assert rows[2026]["is_partial_year"] == "yes"
    assert rows[2026]["locations_ever_shipped_by_end_of_year"] == 3


def test_definition_reconciliation_shows_the_wide_rule_as_an_addition() -> None:
    strict = _account("1", group_field="SCI")
    wide_only = _account(
        "2", sci_flagged=False, group_field="", name="Plain Home", sci_code=""
    )
    wide_only.match_methods = {"name_zip", "phone_unique"}
    accounts = {"1": strict, "2": wide_only}
    bookings = {"1": Counter({2025: 10}), "2": Counter({2025: 3})}
    rows = {
        int(row["year"]): row
        for row in definition_reconciliation_rows(accounts, bookings, 1.0)
    }
    assert rows[2025]["strict_shipping_locations"] == 1
    assert rows[2025]["strict_bookings"] == 10
    assert rows[2025]["wide_shipping_locations"] == 2
    assert rows[2025]["wide_bookings"] == 13
    assert rows[2025]["location_delta"] == 1
    assert rows[2025]["booking_delta"] == 3


# --- trajectory -------------------------------------------------------------


def test_trajectory_classes_known_answers() -> None:
    """One location per class, with the annualisation factor fixed at 1.0.

    With factor 1.0 the thresholds are plain arithmetic: grew above 1.15x 2025,
    declined below 0.85x, flat in between.
    """
    accounts = [_account(str(n)) for n in range(1, 8)]
    bookings = {
        "1": Counter({2024: 5, 2025: 10, 2026: 20}),  # 20 > 11.5  -> grew
        "2": Counter({2024: 5, 2025: 10, 2026: 10}),  # 10 in band -> flat
        "3": Counter({2024: 5, 2025: 10, 2026: 5}),  # 5 < 8.5     -> declined
        "4": Counter({2024: 5, 2025: 10}),  # nothing in 2026       -> lapsed
        "5": Counter({2026: 7}),  # first year is 2026              -> new_2026
        "6": Counter({2025: 3, 2026: 4}),  # 2025 cohort, +33%      -> grew
        "7": Counter({2023: 9, 2026: 2}),  # gap through 2025       -> reactivated
    }
    rows = {
        str(row["funeral_home_id"]): row
        for row in trajectory_rows(accounts, bookings, {}, 1.0)
    }
    assert rows["1"]["trajectory"] == "grew"
    assert rows["2"]["trajectory"] == "flat"
    assert rows["3"]["trajectory"] == "declined"
    assert rows["4"]["trajectory"] == "lapsed"
    assert rows["5"]["trajectory"] == "new_2026"
    assert rows["7"]["trajectory"] == "reactivated"


def test_a_2025_cohort_location_is_classified_on_its_movement_not_parked_as_new() -> (
    None
):
    """Regression: `new_2025` used to pre-empt grew/flat/declined.

    A location CSI won in 2025 and grew in 2026 was being reported as "new",
    which hid whether last year's wins are developing. The cohort belongs in the
    `cohort` column; the trajectory column reports movement.
    """
    accounts = [_account("1"), _account("2")]
    bookings = {"1": Counter({2025: 3, 2026: 9}), "2": Counter({2025: 10, 2026: 2})}
    rows = {
        str(row["funeral_home_id"]): row
        for row in trajectory_rows(accounts, bookings, {}, 1.0)
    }
    assert rows["1"]["trajectory"] == "grew"
    assert rows["1"]["cohort"] == "first_shipped_2025"
    assert rows["2"]["trajectory"] == "declined"


def test_trajectory_compares_2026_annualised_not_part_year() -> None:
    """A location holding steady must not read as declining on a part year."""
    accounts = [_account("1")]
    bookings = {"1": Counter({2024: 20, 2025: 20, 2026: 15})}
    flat = trajectory_rows(accounts, bookings, {}, 1.1543)[0]
    assert flat["trajectory"] == "flat"
    declining = trajectory_rows(accounts, bookings, {}, 1.0)[0]
    assert declining["trajectory"] == "declined"


def test_trajectory_summary_deltas_sum_to_the_net_movement() -> None:
    accounts = [_account("1"), _account("2")]
    bookings = {"1": Counter({2025: 10, 2026: 20}), "2": Counter({2025: 10})}
    trajectories = trajectory_rows(accounts, bookings, {}, 1.0)
    summary = {
        str(row["trajectory"]): row for row in trajectory_summary_rows(trajectories)
    }
    assert summary["grew"]["booking_delta_annualised"] == 10.0
    assert summary["lapsed"]["booking_delta_annualised"] == -10.0
    assert (
        sum(float(row["booking_delta_annualised"]) for row in summary.values()) == 0.0
    )


# --- geography, concentration, partner routing ------------------------------


def test_geography_labels_gateway_and_pickup_states() -> None:
    accounts = [
        _account("1", state="FL"),
        _account("2", state="HI"),
        _account("3", state="TX"),
    ]
    bookings = {
        "1": Counter({2026: 5}),
        "2": Counter({2026: 3}),
        "3": Counter({2025: 1}),
    }
    rows = {str(row["state"]): row for row in geography_rows(accounts, bookings)}
    assert rows["FL"]["csi_gateway_in_state"] == "MIA"
    assert rows["FL"]["csi_pickup_metro_in_state"] == "yes"
    assert rows["HI"]["csi_gateway_in_state"] == ""
    assert rows["HI"]["csi_pickup_metro_in_state"] == "no"
    assert rows["TX"]["bookings_2026"] == 0
    assert rows["TX"]["bookings_all"] == 1


def test_concentration_known_answer() -> None:
    """Four locations with 50/30/15/5 bookings: top 1 is 50%, top 3 is 95%."""
    accounts = [_account(str(n)) for n in range(1, 5)]
    bookings = {
        "1": Counter({2025: 50}),
        "2": Counter({2025: 30}),
        "3": Counter({2025: 15}),
        "4": Counter({2025: 5}),
    }
    revenue = {"1": 500.0, "2": 300.0, "3": 150.0, "4": 50.0}
    rows = {
        int(row["top_n_locations"]): row
        for row in concentration_rows(accounts, bookings, revenue)
    }
    assert rows[1]["bookings_in_top_n"] == 50
    assert rows[1]["pct_of_sci_bookings"] == 50.0
    assert rows[3]["pct_of_sci_bookings"] == 95.0
    assert rows[3]["pct_of_sci_revenue"] == 95.0


def test_partner_routed_rows_report_share_and_exclude_clean_locations() -> None:
    accounts = [_account("1"), _account("2")]
    manifest = {
        "1": {
            "partner_bookings": 486,
            "self_billed_bookings": 15,
            "other_billed_bookings": 0,
            "main_partner": "MIXED",
            "first_booking_date": "2022-06-06",
            "last_booking_date": "2026-11-18",
        },
        "2": {
            "partner_bookings": 0,
            "self_billed_bookings": 40,
            "other_billed_bookings": 0,
            "main_partner": "",
            "first_booking_date": "",
            "last_booking_date": "",
        },
    }
    rows = partner_routed_rows(accounts, {"1": Counter({2025: 495})}, manifest)
    assert len(rows) == 1
    assert rows[0]["partner_billed_bookings"] == 486
    assert rows[0]["partner_share_pct"] == 97.0


def test_unlabelled_locations_require_a_register_match_and_a_booking() -> None:
    labelled = _account("1")
    unlabelled_shipping = _account(
        "2", sci_flagged=False, group_field="", name="Plain Home", sci_code=""
    )
    unlabelled_shipping.match_methods = {"name_zip", "phone_unique"}
    unlabelled_quiet = _account(
        "3", sci_flagged=False, group_field="", name="Quiet Home", sci_code=""
    )
    unlabelled_quiet.match_methods = {"name_zip", "phone_unique"}
    shared_only = _account(
        "4", sci_flagged=False, group_field="", name="Shared", sci_code=""
    )
    shared_only.match_methods = {"phone_shared"}
    accounts = {
        a.account_id: a
        for a in (labelled, unlabelled_shipping, unlabelled_quiet, shared_only)
    }
    bookings = {
        "1": Counter({2025: 9}),
        "2": Counter({2025: 2}),
        "4": Counter({2025: 7}),
    }
    rows = unlabelled_location_rows(accounts, bookings)
    assert [row["funeral_home_id"] for row in rows] == ["2"]


# --- savings model ----------------------------------------------------------


def test_savings_arithmetic_is_exactly_what_the_report_shows() -> None:
    """1,000 bookings at $1,000 revenue each, 75% air share, 10% fee, half diverted.

    base            = 1000 * 0.75          = $750
    fee per booking = 750 * 0.10           = $75
    total           = 1000 * 0.5 * 75      = $37,500
    """
    rows = savings_sensitivity_rows(1_000, 1_000_000.0, "fixture")
    cell = next(
        row
        for row in rows
        if row["assumption_diversion_share"] == 0.50
        and row["assumption_air_rate_share"] == 0.75
        and row["assumption_ewa_fee_rate"] == 0.10
    )
    assert cell["csi_revenue_per_booking"] == 1000.0
    assert cell["assumed_air_rate_base"] == 750.0
    assert cell["avoided_fee_per_diverted_booking"] == 75.0
    assert cell["total_avoided_fee"] == 37_500.0


def test_savings_grid_spread_is_wide_enough_to_be_honest() -> None:
    """The grid must not be mistaken for a point estimate.

    If the spread between the smallest and largest cell ever drops below ~10x,
    someone has narrowed an assumption band and the report's central claim --
    that this figure is not fit to quote as a number -- needs rewriting.
    """
    rows = savings_sensitivity_rows(4_000, 4_000_000.0, "fixture")
    totals = [float(row["total_avoided_fee"]) for row in rows]
    assert len(rows) == 64
    assert max(totals) / min(totals) > 10


def test_savings_model_rejects_a_zero_denominator() -> None:
    with pytest.raises(ValueError, match="positive booking count"):
        savings_sensitivity_rows(0, 100.0, "fixture")


# --- published-figure guards ------------------------------------------------

_SUMMARY = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "derived"
    / "sci-evidence-summary.json"
)


@pytest.mark.skipif(
    not _SUMMARY.exists(), reason="run scripts/sci_relationship_evidence.py first"
)
def test_published_sci_figures_have_not_moved() -> None:
    """Pins the figures quoted in `reports/sci-relationship-evidence.md`."""
    import json

    summary = json.loads(_SUMMARY.read_text(encoding="utf-8"))
    assert summary["register_rows"] == 4439
    assert summary["sci_accounts_identified"] == 688
    assert summary["sci_accounts_identified_strict_rule"] == 292
    assert summary["sci_accounts_ever_shipped"] == 248
    assert summary["sci_accounts_ever_shipped_strict_rule"] == 210
    assert summary["sci_bookings_all_years"] == 4634
    assert summary["partner_routed_sci_locations"] == 12
    assert summary["partner_routed_sci_bookings"] == 509


@pytest.mark.skipif(
    not _SUMMARY.exists(), reason="run scripts/sci_relationship_evidence.py first"
)
def test_strict_rule_still_reproduces_the_published_cohort_figures() -> None:
    """97 / 120 / 123 shipping locations and 1,044 / 1,128 / 1,038 bookings.

    These are the figures in `reports/customer-cohort-analysis.md` and in
    gtm-strategist's `reports/sci-footprint-strategy-2026-12.md`. If this test
    fails, one of the three documents is now wrong and all three need checking.
    """
    import csv

    path = _SUMMARY.parent / "sci-definition-reconciliation.csv"
    rows = {
        int(row["year"]): row for row in csv.DictReader(path.open(encoding="utf-8"))
    }
    assert int(rows[2024]["strict_shipping_locations"]) == 97
    assert int(rows[2025]["strict_shipping_locations"]) == 120
    assert int(rows[2026]["strict_shipping_locations"]) == 123
    assert int(rows[2024]["strict_bookings"]) == 1044
    assert int(rows[2025]["strict_bookings"]) == 1128
    assert int(rows[2026]["strict_bookings"]) == 1038
    assert float(rows[2026]["strict_bookings_annualised"]) == 1198.0


@pytest.mark.skipif(
    not _SUMMARY.exists(), reason="run scripts/sci_relationship_evidence.py first"
)
def test_borthwick_is_one_location_not_a_pattern() -> None:
    """The finding the brief asked to be chased, pinned so it cannot drift.

    Borthwick (SCI Honolulu, id 2773) carries 486 of the 509 partner-billed SCI
    bookings. If another SCI location ever approaches it, this test fails and the
    "one location, not a pattern" conclusion must be re-examined.
    """
    import csv

    path = _SUMMARY.parent / "sci-partner-routed.csv"
    rows = list(csv.DictReader(path.open(encoding="utf-8")))
    assert rows[0]["funeral_home_id"] == "2773"
    assert int(rows[0]["partner_billed_bookings"]) == 486
    others = sum(int(row["partner_billed_bookings"]) for row in rows[1:])
    assert others == 23
    assert max(int(row["partner_billed_bookings"]) for row in rows[1:]) == 7
