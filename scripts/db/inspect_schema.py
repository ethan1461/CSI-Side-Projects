"""Inspect the CSI database schema so export queries stop being guesswork.

Purpose: print the shape of the booking tables -- table names, column names and
         types, row counts, and date coverage -- so a query can be written against
         what is actually there rather than against a screenshot.
Inputs:  CSI_DB_URL (environment).
Outputs: printed to the terminal only. Writes no files.
Owner:   data-analyst
Date:    2026-11-12

CLAUDE.md compliance:
  §7.2 — prints column NAMES, types and COUNTS only. It never selects a column's
         contents, so no decedent, family or address data can reach the terminal.
         The one exception is date minimum and maximum, which are not identifying.
  §8   — no credentials in code; no bare except.
"""

from __future__ import annotations

from sqlalchemy import inspect, text

from _conn import get_engine

INTERESTING = ("booking", "status", "funeral", "shipment")


def main() -> None:
    engine = get_engine()
    inspector = inspect(engine)

    all_tables = inspector.get_table_names()
    print(f"=== {len(all_tables)} tables in the database ===")
    hits = [t for t in all_tables if any(k in t.lower() for k in INTERESTING)]
    for t in sorted(hits):
        print("   ", t)
    if not hits:
        print("    (none matched booking/status/funeral/shipment -- first 40 tables:)")
        for t in sorted(all_tables)[:40]:
            print("   ", t)

    for table in sorted(hits):
        print(f"\n=== {table} ===")
        try:
            cols = inspector.get_columns(table)
        except Exception as exc:  # noqa: BLE001 - surface the reason, keep going
            print(f"    could not read columns: {exc}")
            continue

        date_cols: list[str] = []
        for c in cols:
            type_name = str(c["type"])
            print(f"    {c['name']:<34} {type_name}")
            if any(k in type_name.upper() for k in ("DATE", "TIME")):
                date_cols.append(c["name"])

        with engine.connect() as conn:
            total = conn.execute(text(f"SELECT COUNT(*) FROM `{table}`")).scalar_one()
            print(f"    -- row count: {total:,}")

            for dc in date_cols[:6]:
                row = conn.execute(
                    text(
                        f"SELECT COUNT(`{dc}`) AS non_null, "
                        f"MIN(`{dc}`) AS lo, MAX(`{dc}`) AS hi FROM `{table}`"
                    )
                ).mappings().one()
                print(
                    f"    -- {dc}: {row['non_null']:,} non-null "
                    f"({row['lo']} .. {row['hi']})"
                )


if __name__ == "__main__":
    main()
