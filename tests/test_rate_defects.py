"""Known-answer tests for scripts/rate_defects.py."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))

import rate_defects as rd


def _row(
    origin: str, price: str, rate_type: str = "flat", discount: str = ""
) -> dict[str, str]:
    return {
        "airline": "Test Air",
        "origin_type": "zone",
        "origin": origin,
        "destination_type": "zone",
        "destination": "West",
        "rate_type": rate_type,
        "published_rate": price,
        "discount_rate": discount,
        "shipment_rate_type": "",
    }


SYNTHETIC = [
    # three rows, two prices: the documented example shape (207.19 / 615.94 / 207.19)
    _row("West", "207.19"),
    _row("West", "615.94"),
    _row("West", "207.19"),
    # two identical rows: a violation that does not change the price
    _row("East", "100.00"),
    _row("East", "100"),
    # text in a numeric column
    _row("North", "varies per city"),
    _row("North", "300"),
    # unique, and a same-lane row with a different rate_type, which is NOT a duplicate
    _row("South", "50"),
    _row("South", "9.5", rate_type="var", discount="take $35 off pub"),
]


def test_classify_prices() -> None:
    assert rd.classify_prices(["207.19", "615.94", "207.19"]) == rd.CONFLICT
    assert rd.classify_prices(["100.00", "100"]) == rd.EXACT_REPEAT
    assert rd.classify_prices(["varies per city", "300"]) == rd.NON_NUMERIC


def test_find_duplicate_keys_known_answer() -> None:
    records = rd.find_duplicate_keys(SYNTHETIC)
    assert len(records) == 3
    by_origin = {r["origin"]: r for r in records}
    assert by_origin["West"]["row_count"] == 3
    assert by_origin["West"]["defect_class"] == rd.CONFLICT
    assert by_origin["West"]["max_over_min"] == pytest.approx(2.97, abs=0.01)
    assert by_origin["East"]["defect_class"] == rd.EXACT_REPEAT
    assert by_origin["North"]["defect_class"] == rd.NON_NUMERIC


def test_summarise_known_answer() -> None:
    summary = rd.summarise(SYNTHETIC, rd.find_duplicate_keys(SYNTHETIC))
    assert summary["published_rows"] == 9
    assert summary["shipment_rate_type_blank"] == 9
    assert summary["duplicate_keys"] == 3
    assert summary["rows_in_duplicate_keys"] == 7
    assert summary["conflicting_keys"] == 1
    assert summary["exact_repeat_keys"] == 1
    assert summary["non_numeric_keys"] == 1
    assert summary["non_numeric_published_rate_rows"] == 1
    assert summary["non_numeric_discount_rate_rows"] == 1


def test_real_export_matches_figures_cited_in_the_ask() -> None:
    """Skips where data/raw is absent (it is gitignored). 181 / 487 / 133 come from the 2026-11-02 export."""
    if not rd.DEFAULT_INPUT.exists():
        pytest.skip(
            "data/raw/rates-published-20261102.csv not present in this checkout"
        )
    rows = rd.load_rows(rd.DEFAULT_INPUT)
    summary = rd.summarise(rows, rd.find_duplicate_keys(rows))
    assert summary["published_rows"] == 6919
    assert summary["shipment_rate_type_blank"] == 6919
    assert summary["duplicate_keys"] == 181
    assert summary["rows_in_duplicate_keys"] == 487
    assert summary["conflicting_keys"] == 133
