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
from sqlalchemy import Engine, text

from _conn import get_engine

OUT_DIR = Path(__file__).resolve().parents[2] / "data" / "derived"
OUT_CSV = OUT_DIR / "db-bookings-monthly.csv"
OUT_META = OUT_DIR / "db-bookings-monthly.meta.json"

CANCEL_PATTERN = "%cancel%"

# Aggregated in SQL on purpose: the row-level table carries decedent names (§7.2),
# so those columns must never be fetched, not merely dropped after fetching.
_SQL_MYSQL = """
    SELECT
        YEAR(b.registration_date)  AS yr,
        MONTH(b.registration_date) AS mo,
        COUNT(*)                   AS bookings,
        SUM(CASE WHEN LOWER(COALESCE(s.status, '')) LIKE :cancel
                 THEN 1 ELSE 0 END) AS cancelled
    FROM csi_bookings b
    LEFT JOIN csi_status s ON s.status_id = b.status_id
    WHERE b.registration_date IS NOT NULL
      AND COALESCE(b.hidden, 0) = 0
    GROUP BY YEAR(b.registration_date), MONTH(b.registration_date)
    ORDER BY yr, mo
"""

_SQL_POSTGRES = """
    SELECT
        EXTRACT(YEAR  FROM b.registration_date)::int AS yr,
        EXTRACT(MONTH FROM b.registration_date)::int AS mo,
        COUNT(*)                                     AS bookings,
        SUM(CASE WHEN LOWER(COALESCE(s.status, '')) LIKE :cancel
                 THEN 1 ELSE 0 END)                  AS cancelled
    FROM csi_bookings b
    LEFT JOIN csi_status s ON s.status_id = b.status_id
    WHERE b.registration_date IS NOT NULL
      AND COALESCE(b.hidden, 0) = 0
    GROUP BY 1, 2
    ORDER BY 1, 2
"""


def _sql_for(engine: Engine) -> str:
    """Pick the statement matching the connected database."""
    name = engine.dialect.name
    if name.startswith("mysql") or name.startswith("maria"):
        return _SQL_MYSQL
    if name.startswith("postgre"):
        return _SQL_POSTGRES
    raise RuntimeError(
        f"Unsupported database dialect {name!r}. Add a statement for it in this file."
    )


def _script_version() -> str:
    """Return the current commit, so an output can be traced to the code that made it."""
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"], text=True
        ).strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "unknown"


def fetch_monthly() -> tuple[pd.DataFrame, str]:
    """Read the monthly aggregate from the database. Returns the frame and the dialect."""
    engine = get_engine()
    statement = _sql_for(engine)
    with engine.connect() as conn:
        frame = pd.read_sql(text(statement), conn, params={"cancel": CANCEL_PATTERN})
    print(f"rows in from database: {len(frame)}")
    return frame, engine.dialect.name


def main() -> None:
    frame, dialect = fetch_monthly()
    if frame.empty:
        raise RuntimeError(
            "Query returned no rows. Check the schema caveat in this file's docstring "
            "before assuming the database is empty."
        )

    frame["month"] = (
        frame["yr"].astype(int).astype(str)
        + "-"
        + frame["mo"].astype(int).astype(str).str.zfill(2)
    )
    frame = frame[["month", "bookings", "cancelled"]].sort_values("month")
    frame = frame.reset_index(drop=True)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    frame.to_csv(OUT_CSV, index=False)
    print(f"rows out to {OUT_CSV.name}: {len(frame)}")

    OUT_META.write_text(
        json.dumps(
            {
                "source": "CSI production database (csi_bookings, csi_status)",
                "dialect": dialect,
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
