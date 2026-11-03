"""Known-answer tests for scripts/fy27_target_lists.py (TASK-0021)."""

from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import fy27_target_lists as t


def test_parse_date_handles_bad_input() -> None:
    assert t.parse_date("2026-06-01 00:00:00") == date(2026, 6, 1)
    assert t.parse_date("") is None
    assert t.parse_date("not a date") is None


def test_territory_rule() -> None:
    assert t.territory("OH", "us") == "Otto (Midwest)"
    assert t.territory("CA", "us") == "Stacy (West)"
    assert t.territory("NY", "us") == "Unassigned (Northeast/South)"
    assert t.territory("", "us") == "no state"
    assert t.territory("", "mx") == "non-US (not routed)"


def test_model_base_case_known_answer() -> None:
    summ = {
        "seg1_callable_shipper_split": {"shipper": 100, "non-shipper": 100},
        "seg2_waterfall": {"minus_non_us": 100, "of_which_lifetime_bookings_ge_2": 50},
        "seg4_tiers": {"4A shipper account, never booked": 100},
        "seg4_waterfall": {},
    }
    base = t.build_model(summ)["scenarios"]["base"]
    # seg1: (100*.08 + 100*.03) * 1.5 = 16.5
    assert base["seg1_bookings"] == 16.5
    # seg3: 100 locations * 2.0 * 0.5 = 100
    assert base["seg3_bookings"] == 100.0
    # seg4: (100*.10 + 2000*.01) * 1.5 = 45
    assert base["seg4_bookings"] == 45.0
