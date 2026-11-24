"""Known-answer tests for the revenue-retention metrics (M-25, M-26).

A metric with no test is a metric nobody should trust. Every figure here is
hand-computed in the docstring before being asserted.

Owner: data-analyst · Date: 2026-11-24
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pandas as pd
import pytest

_SPEC = importlib.util.spec_from_file_location(
    "arr", Path(__file__).resolve().parents[1] / "scripts" / "analyze_revenue_retention.py"
)
assert _SPEC and _SPEC.loader
arr = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(arr)


@pytest.fixture
def fixture() -> pd.DataFrame:
    """Four customers over two years, chosen so every term is exercised.

        key  2024    2025    behaviour
        a    1000    1500    expansion  (+500)
        b    1000     500    contraction (-500)
        c    1000       0    churn      (absent in 2025)
        d       0     800    new in 2025 -> MUST be excluded from the cohort

    Cohort = {a, b, c}: base 3000.
      compare revenue      = 1500 + 500 + 0      = 2000  -> NRR = 66.67%
      capped at base       = 1000 +  500 + 0      = 1500  -> GRR = 50.00%
      expansion gap        = (2000 - 1500) / 3000         = 16.67pp
      logos retained       = a, b                = 2 of 3 -> 66.67%
    """
    return pd.DataFrame(
        [
            {"customer_key": "a", "year": 2024, "revenue": 1000.0},
            {"customer_key": "a", "year": 2025, "revenue": 1500.0},
            {"customer_key": "b", "year": 2024, "revenue": 1000.0},
            {"customer_key": "b", "year": 2025, "revenue": 500.0},
            {"customer_key": "c", "year": 2024, "revenue": 1000.0},
            {"customer_key": "d", "year": 2025, "revenue": 800.0},
        ]
    )


def test_nrr_grr_and_logo_retention_match_hand_computation(fixture: pd.DataFrame) -> None:
    row = arr.retention_pairs(fixture).iloc[0]
    assert row["base_year"] == 2024
    assert row["cohort_customers"] == 3, "new-in-2025 customer d must not be in the cohort"
    assert row["cohort_base_revenue"] == pytest.approx(3000.0)
    assert row["cohort_compare_revenue"] == pytest.approx(2000.0)
    assert row["nrr_pct"] == pytest.approx(66.67, abs=0.01)
    assert row["grr_pct"] == pytest.approx(50.00, abs=0.01)
    assert row["expansion_gap_pp"] == pytest.approx(16.67, abs=0.01)
    assert row["logo_retained"] == 2
    assert row["logo_retention_pct"] == pytest.approx(66.67, abs=0.01)


def test_grr_never_exceeds_100_and_never_exceeds_nrr(fixture: pd.DataFrame) -> None:
    """GRR caps each numerator at its own base, so it cannot exceed 100% or NRR.

    Exercised against a cohort that is pure expansion, where NRR is 200%.
    """
    pure_expansion = pd.DataFrame(
        [
            {"customer_key": "a", "year": 2024, "revenue": 100.0},
            {"customer_key": "a", "year": 2025, "revenue": 200.0},
        ]
    )
    row = arr.retention_pairs(pure_expansion).iloc[0]
    assert row["nrr_pct"] == pytest.approx(200.0)
    assert row["grr_pct"] == pytest.approx(100.0)
    for r in arr.retention_pairs(fixture).itertuples():
        assert r.grr_pct <= 100.0 + 1e-9
        assert r.grr_pct <= r.nrr_pct + 1e-9


def test_total_churn_gives_zero_retention() -> None:
    """A cohort with no revenue in the compare year scores 0 on all three."""
    df = pd.DataFrame(
        [
            {"customer_key": "a", "year": 2024, "revenue": 500.0},
            {"customer_key": "b", "year": 2025, "revenue": 900.0},
        ]
    )
    row = arr.retention_pairs(df).iloc[0]
    assert row["nrr_pct"] == pytest.approx(0.0)
    assert row["grr_pct"] == pytest.approx(0.0)
    assert row["logo_retention_pct"] == pytest.approx(0.0)


def test_annual_totals_sum_and_count_customers_not_rows() -> None:
    """Revenue sums per year; the customer count is distinct customers."""
    df = pd.DataFrame(
        [
            {"customer_key": "a", "year": 2025, "revenue": 10.0},
            {"customer_key": "b", "year": 2025, "revenue": 30.0},
            {"customer_key": "a", "year": 2026, "revenue": 5.0},
        ]
    )
    out = arr.annual_totals(df).set_index("year")
    assert out.loc[2025, "revenue"] == pytest.approx(40.0)
    assert out.loc[2025, "revenue_customers"] == 2
    assert out.loc[2025, "revenue_per_customer"] == pytest.approx(20.0)
    assert bool(out.loc[2026, "complete_year"]) is False, "2026 is the partial year"


def test_grain_sensitivity_reports_both_and_their_delta() -> None:
    """Grouping two logos into one must leave the dollars alone and raise logo retention.

    Ungrouped: a (100 -> 100) and b (100 -> 0). NRR 50%, logo retention 50%.
    Grouped as one customer g: 200 -> 100. NRR still 50%, but the single logo is
    retained, so logo retention is 100%. The delta columns must show +50pp on logo
    retention and 0 on NRR.
    """
    ungrouped = pd.DataFrame(
        [
            {"customer_key": "a", "year": 2024, "revenue": 100.0},
            {"customer_key": "a", "year": 2025, "revenue": 100.0},
            {"customer_key": "b", "year": 2024, "revenue": 100.0},
        ]
    )
    grouped = pd.DataFrame(
        [
            {"customer_key": "g", "year": 2024, "revenue": 200.0},
            {"customer_key": "g", "year": 2025, "revenue": 100.0},
        ]
    )
    row = arr.grain_sensitivity(grouped, ungrouped).iloc[0]
    assert row["nrr_pct_ungrouped"] == pytest.approx(50.0)
    assert row["nrr_pct_grouped"] == pytest.approx(50.0)
    assert row["nrr_pct_delta"] == pytest.approx(0.0)
    assert row["logo_retention_pct_ungrouped"] == pytest.approx(50.0)
    assert row["logo_retention_pct_grouped"] == pytest.approx(100.0)
    assert row["logo_retention_pct_delta"] == pytest.approx(50.0)
