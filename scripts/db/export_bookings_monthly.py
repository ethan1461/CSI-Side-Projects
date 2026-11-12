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

DIALECT: CSI runs MySQL (DB_TYPE=mysql, confirmed 2026-11-12). The query is written
         dialect-aware so it also works on PostgreSQL. It deliberately uses YEAR()/
         MONTH() rather than DATE_TRUNC or DATE_FORMAT, because a literal '%' in the
         SQL collides with the DB-API parameter style under PyMySQL. The cancelled
         match is a bound parameter for the same reason.

SCHEMA CAVEAT: table and column names (csi_bookings, csi_status, registration_date,
         hidden, status_id) were taken from a single query Ethan ran on 2026-11-12.
         If the first run errors on a name, fix it here once.
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

# Schema facts confirmed against erp_production on 2026-11-12:
#   - registration_date is TEXT in MM/DD/YYYY, not a DATE. YEAR() on it returns NULL,
#     which is why an earlier version of this script returned two rows. Parse with
#     STR_TO_DATE before extracting anything.
#   - 2 of 49,467 rows parse to a zero date; they are excluded and counted separately.
#   - hidden = 1 on 695 rows (soft delete).
#   - There is NO cancellation signal. Status 23 "Cancelled" exists in csi_status and is
#     used by zero bookings, so this script does not report a cancelled count. Reporting
#     one would be reporting a constant zero as though it were a measurement.

_SQL_MYSQL = """
    SELECT
        DATE_FORMAT(STR_TO_DATE(b.registration_date, :fmt), :ym) AS month,
        COUNT(*)                                                 AS bookings
    FROM csi_bookings b
    WHERE COALESCE(b.hidden, 0) = 0
      AND STR_TO_DATE(b.registration_date, :fmt) IS NOT NULL
      AND YEAR(STR_TO_DATE(b.registration_date, :fmt)) > 1900
    GROUP BY 1
    ORDER BY 1
"""

_SQL_UNPARSEABLE = """
    SELECT COUNT(*) FROM csi_bookings b
    WHERE COALESCE(b.hidden, 0) = 0
      AND (STR_TO_DATE(b.registration_date, :fmt) IS NULL
           OR YEAR(STR_TO_DATE(b.registration_date, :fmt)) <= 1900)
"""

DATE_FMT = "%m/%d/%Y"
YEAR_MONTH = "%Y-%m"


def _script_version() -> str:
    """Return the current commit, so an output can be traced to the code that made it."""
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"], text=True
        ).strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "unknown"


def fetch_monthly() -> tuple[pd.DataFrame, int, str]:
    """Return the monthly series, the count of unparseable dates, and the dialect."""
    engine = get_engine()
    if not engine.dialect.name.startswith(("mysql", "maria")):
        raise RuntimeError(
            f"This query is MySQL-specific (STR_TO_DATE); dialect is "
            f"{engine.dialect.name!r}. Rewrite before running."
        )
    params = {"fmt": DATE_FMT, "ym": YEAR_MONTH}
    with engine.connect() as conn:
        frame = pd.read_sql(text(_SQL_MYSQL), conn, params=params)
        bad = conn.execute(text(_SQL_UNPARSEABLE), {"fmt": DATE_FMT}).scalar_one()
    print(f"rows in from database: {len(frame)} months")
    print(f"bookings with an unparseable registration_date (excluded): {bad}")
    return frame, int(bad), engine.dialect.name


def main() -> None:
    frame, unparseable, dialect = fetch_monthly()
    if frame.empty:
        raise RuntimeError(
            "Query returned no rows. The schema was confirmed on 2026-11-12; if this "
            "fails, the table has changed rather than the query being wrong."
        )

    frame = frame.sort_values("month").reset_index(drop=True)
    total = int(frame["bookings"].sum())

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    frame.to_csv(OUT_CSV, index=False)
    print(f"rows out to {OUT_CSV.name}: {len(frame)} months, {total:,} bookings")

    OUT_META.write_text(
        json.dumps(
            {
                "source": "erp_production.csi_bookings (MySQL, read-only user)",
                "dialect": dialect,
                "script": Path(__file__).name,
                "script_version": _script_version(),
                "run_timestamp": datetime.now(timezone.utc).isoformat(),
                "row_count": int(len(frame)),
                "months_covered": [frame["month"].iloc[0], frame["month"].iloc[-1]],
                "total_bookings": total,
                "aggregation": "monthly; aggregated in SQL, no row-level data fetched",
                "excludes": (
                    f"hidden <> 0 (695 rows as of 2026-11-12); "
                    f"{unparseable} rows whose registration_date does not parse"
                ),
                "columns_deliberately_not_selected": (
                    "every name, address and certificate field. Decedent data lives in "
                    "csi_booking_deceased_information, which this query never touches "
                    "(CLAUDE.md 7.2)"
                ),
                "known_limitation": (
                    "No cancellation count is reported. csi_status row 23 'Cancelled' is "
                    "used by zero bookings, so CSI has no cancellation signal in status."
                ),
            },
            indent=2,
        )
        + "\n"
    )
    print(f"wrote {OUT_META.name}")


if __name__ == "__main__":
    main()
