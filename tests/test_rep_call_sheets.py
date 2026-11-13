"""Known-answer tests for scripts/build_rep_call_sheets.py (v3 partition rules)."""

from __future__ import annotations

import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import build_rep_call_sheets as b
import pytest


def _row(rank: int, rep: str, lst: str = "one_and_done", held: str = "") -> dict:
    return {
        "bucket": "rep",
        "rep": rep,
        "territory_rep": rep,
        "list": lst,
        "list_rank": rank,
        "call_status": held,
        "owner_rule": "",
    }


def test_carve_tail_round_robin_keeps_held_and_head() -> None:
    otto = [_row(i, "Otto") for i in range(1, 86)]  # 85 one-and-done
    otto[82]["call_status"] = b.HELD  # held row beyond the cut stays put
    stacy = [_row(i, "Stacy") for i in range(1, 83)]  # 82
    rows = otto + stacy
    carved = b.carve_tail(rows)
    # Otto: 5 beyond the 80 cut, 1 held stays -> 4; Stacy: 2 -> total 6
    assert len(carved) == 6
    assert [r["rep"] for r in carved] == [
        "Abe",
        "Renee",
        "Susej",
        "Abe",
        "Renee",
        "Susej",
    ]
    assert otto[82]["rep"] == "Otto"
    assert all(r["rep"] == "Otto" for r in otto[:80])


def test_caution_holds_sci_releases_northstar() -> None:
    sci = {"group": "SCI", "funeral_home": "X (SCI Location #1)"}
    ns = {"group": "Northstar", "funeral_home": "Y (Northstar Location #2)"}
    ind = {"group": "Independent", "funeral_home": "Z Funeral Home"}
    assert b.caution(sci)[2] is True
    assert b.caution(ns)[2] is False
    assert b.caution(ind) == ("", "", False)


def _src(
    fid: str, name: str, state: str, b24: int, b25: int, group: str = "Independent"
) -> dict:
    return {
        "funeral_home_id": fid,
        "funeral_home": name,
        "state": state,
        "group": group,
        "is_partner_tier": "False",
        "bookings_2024": str(b24),
        "bookings_2025": str(b25),
        "bookings_2026_to_cut": "5",
        "bookings_2026_annualised": "6",
        "bookings_at_stake_vs_prior": "10",
        "last_booking": "2026-10-01",
    }


def test_key_account_threshold_boundary_and_peak() -> None:
    assert b.peak_bookings({"bookings_2024": "49", "bookings_2025": "10"}) == 49
    assert b.peak_bookings({"bookings_2024": "", "bookings_2025": "50"}) == 50
    assert b.peak_bookings({}) == 0  # one-and-done rows carry neither column
    assert not b.is_key_account(49)
    assert b.is_key_account(50)
    assert b.is_key_account(40, threshold=40) and not b.is_key_account(39, threshold=40)


def test_build_rows_routes_key_account_off_rep_and_keeps_hold() -> None:
    data = [
        _src("1", "Big Funeral Home", "TX", 60, 10),
        _src("2", "Just Under Funeral Home", "TX", 49, 10),
        _src("3", "Big SCI Home (SCI Location #1)", "FL", 10, 55, group="SCI"),
    ]
    rows = {r["funeral_home_id"]: r for r in b.build_rows([("at_risk", data)], {})}
    assert rows["1"]["bucket"] == "key" and rows["1"]["rep"] == b.OWNER_KEY
    assert rows["2"]["bucket"] == "rep" and rows["2"]["rep"] in ("Otto", "Stacy")
    assert rows["3"]["bucket"] == "key" and rows["3"]["call_status"] == b.HELD


def _sheet(name: str) -> list[dict]:
    path = b.D / name
    if not path.exists():
        pytest.skip(f"{name} not generated")
    with path.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def test_no_caller_sheet_holds_an_account_at_or_above_threshold() -> None:
    """Key-account rule: no rep-owned (or Ethan-owned) sheet contains a row at or above the threshold."""
    callers = ["otto", "stacy", "abe", "renee", "susej"]
    if b.KEY_RULE_COVERS_ETHAN_SHEET:
        callers.append("ethan")
    for who in callers:
        for r in _sheet(f"rep-call-sheet-{who}-2026-11.csv"):
            assert int(r["peak_annual_bookings"]) < b.KEY_ACCOUNT_PEAK, (
                who,
                r["funeral_home"],
            )
    key = _sheet("call-sheet-key-accounts-2026-11.csv")
    assert all(r["rep"] == b.OWNER_KEY for r in key)
    by_rule = [r for r in key if r["in_ortiz_group"] != "Y"]
    assert all(int(r["peak_annual_bookings"]) >= b.KEY_ACCOUNT_PEAK for r in by_rule)
    assert (
        sum(1 for r in key if r["in_ortiz_group"] == "Y") == 3
    )  # Ortiz grouping stays identifiable


def test_levitt_weinstein_3242_not_pulled_across_by_name() -> None:
    names = {r["funeral_home"] for r in _sheet("call-sheet-key-accounts-2026-11.csv")}
    assert not any("3242" in n for n in names)
    rows = [
        r
        for who in ("otto", "stacy", "abe", "renee", "susej")
        for r in _sheet(f"rep-call-sheet-{who}-2026-11.csv") + []
        if "Location #3242" in r["funeral_home"]
    ]
    rows += [
        r
        for r in _sheet("call-sheet-unrouted-2026-11.csv")
        if "Location #3242" in r["funeral_home"]
    ]
    assert len(rows) == 1
