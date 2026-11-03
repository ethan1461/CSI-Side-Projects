"""Known-answer tests for scripts/account_concentration.py."""

from __future__ import annotations

import csv
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))

import account_concentration as ac


def _acct(name: str, bookings: int) -> ac.Account:
    return ac.Account(
        account_id=name.lower().replace(" ", "-"),
        name=name,
        state="FL",
        bookings=bookings,
        is_partner=ac.is_partner(name),
    )


# --- to_int -----------------------------------------------------------------


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("12", 12),
        ("12.0", 12),
        ("", 0),
        ("   ", 0),
        (None, 0),
        ("not a number", 0),
        ("0", 0),
    ],
)
def test_to_int(raw: str | None, expected: int) -> None:
    assert ac.to_int(raw) == expected


# --- partner labelling ------------------------------------------------------


def test_partner_markers_match_the_named_allies() -> None:
    """CLAUDE.md §5 partners are labelled; an ordinary account is not."""
    assert ac.is_partner("Bergen Funeral Service (New Jersey)")
    assert ac.is_partner("National Mortuary Shipping")
    assert ac.is_partner("International Mortuary Shipping, LLC")
    assert not ac.is_partner("Gutterman-Warheit Memorial Chapel")
    # Must not fire on a merely similar name.
    assert not ac.is_partner("Bergen County Cremation Society")


# --- concentration curve: known answer --------------------------------------


def test_curve_known_answer() -> None:
    """Ten accounts of 100, 90, ..., 10 bookings. Total 550.

    Top 1 = 100/550 = 18.18%. Top 5 = (100+90+80+70+60)/550 = 400/550 = 72.73%.
    """
    accounts = [_acct(f"Home {i}", bookings) for i, bookings in enumerate(range(100, 0, -10))]
    curve = {row["top_n"]: row for row in ac.concentration_curve(accounts, (1, 5, 10))}

    assert curve[1]["share_pct"] == 18.18
    assert curve[5]["share_pct"] == 72.73
    assert curve[10]["share_pct"] == 100.0
    assert curve[1]["total_bookings"] == 550
    assert curve[1]["booking_accounts"] == 10


def test_curve_omits_points_beyond_the_account_count() -> None:
    """A top-500 point on a 3-account book is omitted, not reported as 100%."""
    accounts = [_acct("A", 10), _acct("B", 5), _acct("C", 1)]
    points = {row["top_n"] for row in ac.concentration_curve(accounts, (1, 5, 500))}
    assert points == {1}


def test_curve_ignores_zero_booking_accounts() -> None:
    """Dormant accounts change neither the denominator nor the ranking."""
    live = [_acct("A", 10), _acct("B", 10)]
    padded = live + [_acct(f"Dormant {i}", 0) for i in range(500)]
    assert ac.concentration_curve(live, (1,)) == ac.concentration_curve(padded, (1,))


def test_curve_raises_when_there_are_no_bookings() -> None:
    with pytest.raises(ValueError, match="total bookings is zero"):
        ac.concentration_curve([_acct("A", 0)], (1,))


# --- top accounts -----------------------------------------------------------


def test_top_accounts_cumulative_share_and_partner_flag() -> None:
    accounts = [
        _acct("Bergen Funeral Service (New Jersey)", 60),
        _acct("Ordinary Chapel", 30),
        _acct("Small Home", 10),
    ]
    rows = ac.top_accounts(accounts, limit=3)

    assert [row["rank"] for row in rows] == [1, 2, 3]
    assert rows[0]["strategic_partner"] == "yes"
    assert rows[1]["strategic_partner"] == "no"
    assert rows[0]["share_pct"] == 60.0
    assert rows[1]["cumulative_share_pct"] == 90.0
    assert rows[2]["cumulative_share_pct"] == 100.0


def test_top_accounts_respects_the_limit() -> None:
    accounts = [_acct(f"Home {i}", 100 - i) for i in range(40)]
    assert len(ac.top_accounts(accounts, limit=25)) == 25


# --- load: privacy and row counts -------------------------------------------


def test_load_drops_identifier_columns_at_load(tmp_path: Path) -> None:
    """`CLAUDE.md` §7.2 — identifier columns must never enter the Account."""
    source = tmp_path / "homes.csv"
    with source.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "funeral_home_id",
                "name",
                "address",
                "phone",
                "email",
                "state",
                "booking_count",
                "created_by",
            ],
        )
        writer.writeheader()
        writer.writerow(
            {
                "funeral_home_id": "1",
                "name": "Example Chapel",
                "address": "1 Main St",
                "phone": "555-0100",
                "email": "someone@example.com",
                "state": "FL",
                "booking_count": "7",
                "created_by": "A Person",
            }
        )

    accounts, rows_in, dropped = ac.load_accounts(source)

    assert rows_in == 1
    assert len(accounts) == 1
    assert accounts[0].bookings == 7
    assert dropped == ["address", "created_by", "email", "phone"]
    # No identifier value survives anywhere on the loaded record.
    for forbidden in ("1 Main St", "555-0100", "someone@example.com", "A Person"):
        assert forbidden not in str(accounts[0])


def test_load_raises_on_a_headerless_file(tmp_path: Path) -> None:
    source = tmp_path / "empty.csv"
    source.write_text("", encoding="utf-8")
    with pytest.raises(ValueError, match="no header row"):
        ac.load_accounts(source)


def test_write_csv_refuses_an_empty_file(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="refusing to write an empty file"):
        ac.write_csv(tmp_path / "out.csv", [])


# --- idempotence ------------------------------------------------------------


def test_curve_is_order_independent() -> None:
    """Same input in a different order gives the same output (`CLAUDE.md` §8)."""
    accounts = [_acct("A", 10), _acct("B", 30), _acct("C", 20)]
    assert ac.concentration_curve(accounts, (1, 2, 3)) == ac.concentration_curve(
        list(reversed(accounts)), (1, 2, 3)
    )
