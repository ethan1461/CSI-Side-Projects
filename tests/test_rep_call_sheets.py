"""Known-answer tests for scripts/build_rep_call_sheets.py (v3 partition rules)."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import build_rep_call_sheets as b


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
    assert [r["rep"] for r in carved] == ["Abe", "Renee", "Susej", "Abe", "Renee", "Susej"]
    assert otto[82]["rep"] == "Otto"
    assert all(r["rep"] == "Otto" for r in otto[:80])


def test_caution_holds_sci_releases_northstar() -> None:
    sci = {"group": "SCI", "funeral_home": "X (SCI Location #1)"}
    ns = {"group": "Northstar", "funeral_home": "Y (Northstar Location #2)"}
    ind = {"group": "Independent", "funeral_home": "Z Funeral Home"}
    assert b.caution(sci)[2] is True
    assert b.caution(ns)[2] is False
    assert b.caution(ind) == ("", "", False)
