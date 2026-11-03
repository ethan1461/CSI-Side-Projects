"""Account (customer) concentration curve from the OMS funeral-home export.

Purpose
-------
Customer concentration is the first number any lender, buyer or investor asks for.
It was asked twice in one week, so per `CLAUDE.md` §9.3 it is a script, not an analysis.

Produces the concentration curve (top-N share of lifetime bookings) and the named
top-N accounts, so that a diligence answer costs a shell command.

Inputs
------
`data/raw/oms-funeral-homes-20261103.csv` (default; override with --source).
One row per funeral-home account, with a lifetime `booking_count` column.

Outputs
-------
`data/derived/account-concentration.csv`      — the top-N curve
`data/derived/account-concentration-top.csv`  — the named top-N accounts
plus a `.meta.json` for each, recording source, row counts, dropped columns,
script version and run timestamp.

Privacy (`CLAUDE.md` §7.2)
--------------------------
Identifier columns are dropped **at load**, never after. Funeral-home *business*
names are retained deliberately — §7.2 permits business names. No individual
contact name, email, phone or street address is ever read into memory, and the
dropped column list is recorded in the `.meta.json`.

Known limit
-----------
`booking_count` sums to 52,269 across this export against roughly 43,600 bookings
in OMS history (`tasks/backlog/BACKLOG.md` B-01). The *denominator is unreconciled*,
so treat every share below as a share of this field, not of booked shipments. The
shares are more robust than the absolute counts, because a uniform overcount cancels
in a ratio — but a non-uniform one does not. Do not quote these externally until
B-01 is resolved.

Owner: corpdev
Date: 2026-11-03
Version: 1.0.0
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

VERSION = "1.0.0"

# Columns kept at load. Everything else in the export is dropped before any row
# is held in memory. `address`, `phone`, `email`, `created_by` and `updated_by`
# are the identifier-bearing columns in this source and are never read.
KEEP_COLUMNS: frozenset[str] = frozenset(
    {
        "funeral_home_id",
        "name",
        "state",
        "country_code",
        "funeral_home_group",
        "booking_count",
        "last_booking_date",
        "likely_duplicate",
        "duplicate_group_id",
    }
)

# Buckets for the concentration curve.
CURVE_POINTS: tuple[int, ...] = (1, 5, 10, 20, 25, 50, 100, 250, 500, 1000)

# Accounts named in CLAUDE.md §5 and context/brain/accounts-and-pipeline.md as
# strategic partners rather than ordinary customers. Matched case-insensitively
# on a substring of the account name, purely to label the output.
PARTNER_MARKERS: tuple[str, ...] = (
    "bergen funeral service",
    "national mortuary shipping",
    "international mortuary shipping",
)


@dataclass(frozen=True)
class Account:
    """One funeral-home account, reduced to the non-identifying fields."""

    account_id: str
    name: str
    state: str
    bookings: int
    is_partner: bool


def to_int(value: str | None) -> int:
    """Parse a booking count. Blank, missing and non-numeric all mean zero."""
    if value is None:
        return 0
    text = value.strip()
    if not text:
        return 0
    try:
        return int(float(text))
    except ValueError:
        return 0


def is_partner(name: str) -> bool:
    """True when the account is a named strategic partner (`CLAUDE.md` §5)."""
    lowered = name.lower()
    return any(marker in lowered for marker in PARTNER_MARKERS)


def load_accounts(source: Path) -> tuple[list[Account], int, list[str]]:
    """Load accounts, dropping identifier columns at load.

    Returns the accounts, the raw row count read, and the columns dropped.
    """
    accounts: list[Account] = []
    rows_in = 0
    dropped: list[str] = []

    with source.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise ValueError(f"{source} has no header row")
        dropped = sorted(set(reader.fieldnames) - KEEP_COLUMNS)
        for raw in reader:
            rows_in += 1
            name = (raw.get("name") or "").strip()
            accounts.append(
                Account(
                    account_id=(raw.get("funeral_home_id") or "").strip(),
                    name=name,
                    state=(raw.get("state") or "").strip(),
                    bookings=to_int(raw.get("booking_count")),
                    is_partner=is_partner(name),
                )
            )

    return accounts, rows_in, dropped


def concentration_curve(
    accounts: list[Account], points: tuple[int, ...] = CURVE_POINTS
) -> list[dict[str, object]]:
    """Top-N share of total bookings, at each point in `points`.

    Accounts are ranked by bookings descending. Points beyond the number of
    booking accounts are omitted rather than reported as 100%.
    """
    ranked = sorted(
        (a for a in accounts if a.bookings > 0), key=lambda a: (-a.bookings, a.name)
    )
    total = sum(a.bookings for a in ranked)
    if total == 0:
        raise ValueError("total bookings is zero; nothing to rank")

    curve: list[dict[str, object]] = []
    for n in points:
        if n > len(ranked):
            continue
        bookings = sum(a.bookings for a in ranked[:n])
        curve.append(
            {
                "top_n": n,
                "bookings": bookings,
                "share_pct": round(bookings / total * 100, 2),
                "total_bookings": total,
                "booking_accounts": len(ranked),
            }
        )
    return curve


def top_accounts(accounts: list[Account], limit: int = 25) -> list[dict[str, object]]:
    """The `limit` largest accounts, with cumulative share and a partner flag."""
    ranked = sorted(
        (a for a in accounts if a.bookings > 0), key=lambda a: (-a.bookings, a.name)
    )
    total = sum(a.bookings for a in ranked)
    rows: list[dict[str, object]] = []
    cumulative = 0
    for rank, account in enumerate(ranked[:limit], start=1):
        cumulative += account.bookings
        rows.append(
            {
                "rank": rank,
                "account_id": account.account_id,
                "name": account.name,
                "state": account.state,
                "bookings": account.bookings,
                "share_pct": round(account.bookings / total * 100, 2),
                "cumulative_share_pct": round(cumulative / total * 100, 2),
                "strategic_partner": "yes" if account.is_partner else "no",
            }
        )
    return rows


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    """Write rows to CSV. Raises if there is nothing to write."""
    if not rows:
        raise ValueError(f"refusing to write an empty file: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_meta(
    path: Path, source: Path, rows_in: int, rows_out: int, dropped: list[str]
) -> None:
    """Write the companion `.meta.json` required by `CLAUDE.md` §8."""
    meta = {
        "script": "scripts/account_concentration.py",
        "script_version": VERSION,
        "source_file": str(source),
        "rows_in": rows_in,
        "rows_out": rows_out,
        "dropped_columns_at_load": dropped,
        "privacy_note": (
            "Identifier columns dropped at load per CLAUDE.md §7.2. Funeral-home "
            "business names retained deliberately; no individual name, email, "
            "phone or street address is read."
        ),
        "known_limit": (
            "booking_count sums to a figure above OMS booked-shipment history "
            "(BACKLOG B-01). Denominator unreconciled; shares are a share of this "
            "field, not of booked shipments. Not for external use until resolved."
        ),
        "run_timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    path.write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    """Entry point."""
    repo_root = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source",
        type=Path,
        default=repo_root / "data" / "raw" / "oms-funeral-homes-20261103.csv",
    )
    parser.add_argument("--out-dir", type=Path, default=repo_root / "data" / "derived")
    parser.add_argument("--top", type=int, default=25)
    args = parser.parse_args()

    accounts, rows_in, dropped = load_accounts(args.source)
    print(f"rows in:  {rows_in}")
    print(f"accounts with at least one booking: "
          f"{len([a for a in accounts if a.bookings > 0])}")
    print(f"dropped at load: {', '.join(dropped) or '(none)'}")

    curve = concentration_curve(accounts)
    top = top_accounts(accounts, args.top)

    curve_path = args.out_dir / "account-concentration.csv"
    top_path = args.out_dir / "account-concentration-top.csv"
    write_csv(curve_path, curve)
    write_csv(top_path, top)
    write_meta(
        curve_path.with_suffix(".meta.json"), args.source, rows_in, len(curve), dropped
    )
    write_meta(
        top_path.with_suffix(".meta.json"), args.source, rows_in, len(top), dropped
    )

    print(f"rows out: {len(curve)} -> {curve_path}")
    print(f"rows out: {len(top)} -> {top_path}")
    for row in curve:
        print(f"  top {row['top_n']:>5}: {row['share_pct']:>6}%")


if __name__ == "__main__":
    main()
