"""Export monthly booking counts from the CSI production database.

Purpose: produce a monthly bookings series (total and cancelled) that agents can read
         without any database access, as the worked example of the local-export loop
         described in scripts/db/README.md.
Inputs:  CSI_DB_URL (environment); the csi_bookings and csi_status tables.
Outputs: data/derived/db-bookings-monthly.csv and a companion .meta.json.
Owner:   data-analyst
Date:    2026-11-12

CLAUDE.md compliance:
  §7.2 — aggregates in SQL. No row-level data and no name column is ever selected,
         so nothing identifying can reach the output file or the terminal.
  §8   — idempotent, type-hinted, logs row counts, writes a .meta.json, no credentials.
  §9.3 — a recurring question answered by a command rather than a session.

SCHEMA CAVEAT: the table and column names below were taken from a single query Ethan
ran on 2026-11-12 (csi_bookings, csi_status, registration_date, hidden, status_id).
Verify them against the live schema on first run; if they differ, fix them here once
so the next person does not have to.
"""

from __future__ import annotations

import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
from sqlalchemy import text

from _conn import get_engine

OUT_DIR = Path(__file__).resolve().parents[2] / "data" / "derived"
OUT_CSV = OUT_DIR / "db-bookings-monthly.csv"
OUT_META = OUT_DIR / "db-bookings-monthly.meta.json"

# Aggregated in SQL on purpose: the row-level table carries decedent names (§7.2),
# so they must never be fetched, not merely dropped after fetching.
SQL = text(
    """
    SELECT
        DATE_TRUNC('month', b.registration_date) AS month,
        COUNT(*)                                  AS bookings,
        SUM(CASE WHEN LOWER(COALESCE(s.status, '')) LIKE '%cancel%'
                 THEN 1 ELSE 0 END)               AS cancelled
    FROM csi_bookings b
    LEFT JOIN csi_status s ON s.status_id = b.status_id
    WHERE b.registration_date IS NOT NULL
      AND COALESCE(b.hidden, 0) = 0
    GROUP BY 1
    ORDER BY 1
    """
)


def _script_version() -> str:
    """Return the current commit, so an output can be traced to the code that made it."""
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"], text=True
        ).strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "unknown"


def fetch_monthly() -> pd.DataFrame:
    """Read the monthly aggregate from the database."""
    engine = get_engine()
    with engine.connect() as conn:
        frame = pd.read_sql(SQL, conn)
    print(f"rows in from database: {len(frame)}")
    return frame


def main() -> None:
    frame = fetch_monthly()
    if frame.empty:
        raise RuntimeError(
            "Query returned no rows. Check the schema caveat in this file's docstring "
            "before assuming the database is empty."
        )

    frame["month"] = pd.to_datetime(frame["month"]).dt.strftime("%Y-%m")
    frame = frame.sort_values("month").reset_index(drop=True)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    frame.to_csv(OUT_CSV, index=False)
    print(f"rows out to {OUT_CSV.name}: {len(frame)}")

    OUT_META.write_text(
        json.dumps(
            {
                "source": "CSI production database (csi_bookings, csi_status)",
                "script": Path(__file__).name,
                "script_version": _script_version(),
                "run_timestamp": datetime.now(timezone.utc).isoformat(),
                "row_count": int(len(frame)),
                "months_covered": [frame["month"].iloc[0], frame["month"].iloc[-1]],
                "total_bookings": int(frame["bookings"].sum()),
                "aggregation": "monthly; aggregated in SQL, no row-level data fetched",
                "columns_deliberately_not_selected": (
                    "every name, address and certificate field -- aggregated in SQL so "
                    "no identifying column is read at all (CLAUDE.md 7.2)"
                ),
                "excludes": "rows where hidden <> 0, and rows with no registration_date",
            },
            indent=2,
        )
        + "\n"
    )
    print(f"wrote {OUT_META.name}")


if __name__ == "__main__":
    main()
