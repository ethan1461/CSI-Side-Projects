"""Known-answer tests for the adjacent-lane sizing model.

Owner: gtm-strategist. Date: 2026-11-24.
Covers the two functions that compute reported metrics (`product`, `totals`) plus the
geography read, per the quality bar in CLAUDE.md §8.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from size_adjacent_lanes import (
    LaneResult,
    csi_international_annual,
    product,
    read_geography,
    scalar,
    totals,
)


def test_product_multiplies_elementwise() -> None:
    assert product((1.0, 2.0, 3.0), (10.0, 10.0, 10.0)) == (10.0, 20.0, 30.0)


def test_product_compounds_corners_not_midpoints() -> None:
    """Low x low must be the low corner -- the model's uncertainty widens, never narrows."""
    low, central, high = product((100.0, 200.0, 400.0), (0.1, 0.2, 0.4))
    assert low == pytest.approx(10.0)
    assert central == pytest.approx(40.0)
    assert high == pytest.approx(160.0)
    assert high / low == pytest.approx(16.0)


def test_product_rejects_wrong_arity() -> None:
    with pytest.raises(ValueError, match="3-tuple"):
        product((1.0, 2.0))  # type: ignore[arg-type]


def test_scalar_lifts_to_triple() -> None:
    assert scalar(7) == (7.0, 7.0, 7.0)


def _lane(ebitda: tuple[float, float, float], *, new: bool) -> LaneResult:
    return LaneResult(
        lane="x",
        pool="y",
        inside_74m="INSIDE",
        spend_pool=(0.0, 0.0, 0.0),
        csi_revenue=(0.0, 0.0, 0.0),
        csi_ebitda=ebitda,
        ceiling_ebitda=(ebitda[0] * 2, ebitda[1] * 2, ebitda[2] * 2),
        counts_toward_new_ebitda=new,
        note="test fixture",
    )


def test_totals_separates_new_from_excluded() -> None:
    agg = totals(
        [
            _lane((1.0, 10.0, 100.0), new=True),
            _lane((2.0, 20.0, 200.0), new=True),
            _lane((5.0, 50.0, 500.0), new=False),
        ]
    )
    assert agg["new_ebitda"] == (3.0, 30.0, 300.0)
    assert agg["excluded_ebitda"] == (5.0, 50.0, 500.0)
    # The ceiling counts only the new lanes, at twice each per the fixture.
    assert agg["ceiling_at_full_capture"] == (6.0, 60.0, 600.0)


def test_geography_read_is_internally_consistent() -> None:
    geo = read_geography()
    assert (
        geo["sending_us_origin"] + geo["sending_foreign_origin"] == geo["sending_total"]
    )
    assert (
        geo["receiving_us_domestic"] + geo["receiving_foreign"]
        == geo["receiving_total"]
    )
    # CSI's book is overwhelmingly US-origin; if this ever fails, the inbound finding in
    # reports/adjacent-lane-sizing.md §4 needs revisiting.
    assert geo["sending_foreign_origin"] / geo["sending_total"] < 0.01


def test_csi_international_annual_is_about_half_the_book() -> None:
    geo = read_geography()
    intl = csi_international_annual(geo)
    assert 5_000 <= intl <= 6_200
