"""Find out why the database and every published CSI booking figure disagree.

THE PROBLEM
    Round 2's D6 counted bookings straight from `csi_bookings WHERE hidden = 0`:

        2023  10,840      2024  10,995      2025  11,013

    Every published CSI figure says otherwise - `CLAUDE.md` §2 and
    `data/derived/annual-totals.csv`, both built from the OMS analytics export:

        2023  10,571      2024  10,867      2025  10,985

    Gaps of +269, +128 and +28. D7 rules out a status filter: 2023 with drafts and
    Pending AWB removed is 10,776, still 205 above the published figure. The gap also
    shrinks each year, which looks more like historical data than a definition.

    This matters because every retention, margin and geography number produced this week
    sits on the database population, and no published CSI figure matches it. It is the
    first thing a buyer's analyst would check.

THE HYPOTHESIS THIS TESTS FIRST
    **There are two booking tables.** D1 listed both `csi_bookings` and `csi_bookings_new`,
    the latter with 88 columns, and D1's column list for it was truncated at 54 so nobody
    has seen the rest. If the OMS analytics module reads `csi_bookings_new` while every
    query this week read `csi_bookings`, that alone would explain the discrepancy - and it
    would mean the wrong table has been used all week, including for the geography
    workbook that has already gone to counsel.

    Q2 is therefore the single most important query here. If `csi_bookings_new` returns
    10,571 / 10,867 / 10,985, the question is answered and the fix is mechanical.

    If it does not, the remaining candidates are a different date basis (flight or ship
    date rather than `registration_date`), or an exclusion applied inside the analytics
    module that is not visible in either table. Both are questions for Kyri and Alex, and
    Q4 and Q5 narrow which one to ask about.

HOW TO RUN
    python reconcile_booking_population.py /path/to/output/dir

    Run from the same environment as the earlier rounds. Queries are independent and
    wrapped, so one failure does not stop the rest.

PRIVACY - CLAUDE.md §7.2
    `csi_booking_deceased_information` is never joined. Q1 lists column names for one
    table. No query selects a name, address or certificate field.

OWNER      pm-orchestrator
CREATED    2026-11-25
RE-RUNNABLE  yes. Read-only.
"""

import csv
import sys
import time
from pathlib import Path

from utils.query import query

OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path()

Q = {
    # The 34 columns D1 could not show, plus the 54 it could. Needed to know which date
    # and status columns csi_bookings_new actually has.
    "B1_bookings_new_columns": """
SELECT ORDINAL_POSITION, COLUMN_NAME, DATA_TYPE, IS_NULLABLE, COLUMN_KEY
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = 'csi_bookings_new'
ORDER BY ORDINAL_POSITION""",
    # THE KEY QUERY. If this returns 10,571 / 10,867 / 10,985 the mystery is solved.
    # Wrapped because registration_date may not be the column name on this table - if it
    # fails, B1 says what to use instead.
    "B2_bookings_new_by_year": """
SELECT SUBSTRING(registration_date, 7, 4) AS yr,
       COUNT(*) AS all_rows,
       SUM(CASE WHEN hidden = 0 THEN 1 ELSE 0 END) AS hidden_0
FROM csi_bookings_new
GROUP BY yr ORDER BY yr""",
    # How do the two tables relate? Same rows, a subset, or a parallel universe?
    "B3_table_overlap": """
SELECT (SELECT COUNT(*) FROM csi_bookings)                        AS old_rows,
       (SELECT COUNT(*) FROM csi_bookings_new)                    AS new_rows,
       (SELECT COUNT(*) FROM csi_bookings o
          WHERE EXISTS (SELECT 1 FROM csi_bookings_new n
                        WHERE n.booking_id = o.booking_id))       AS in_both,
       (SELECT COUNT(*) FROM csi_bookings o
          WHERE NOT EXISTS (SELECT 1 FROM csi_bookings_new n
                            WHERE n.booking_id = o.booking_id))   AS only_old,
       (SELECT COUNT(*) FROM csi_bookings_new n
          WHERE NOT EXISTS (SELECT 1 FROM csi_bookings o
                            WHERE o.booking_id = n.booking_id))   AS only_new""",
    # If the gap is a date basis rather than a table, it shows up here: the same bookings
    # counted on a different date column land in different years.
    "B4_date_basis_2025": """
SELECT 'registration_date' AS basis,
       SUBSTRING(b.registration_date, 7, 4) AS yr, COUNT(*) AS bookings
FROM csi_bookings b WHERE b.hidden = 0
GROUP BY yr
HAVING yr IN ('2023', '2024', '2025')
ORDER BY basis, yr""",
    # Which other date columns exist to test as a basis, across both tables.
    "B5_candidate_date_columns": """
SELECT TABLE_NAME, COLUMN_NAME, DATA_TYPE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = DATABASE()
  AND TABLE_NAME IN ('csi_bookings', 'csi_bookings_new')
  AND (COLUMN_NAME LIKE '%date%' OR COLUMN_NAME LIKE '%_at'
       OR DATA_TYPE IN ('date', 'datetime', 'timestamp'))
ORDER BY TABLE_NAME, ORDINAL_POSITION""",
}


def main() -> int:
    """Run each query, write a TSV, and print the comparison that matters."""
    OUT.mkdir(parents=True, exist_ok=True)
    failed = []
    for name, sql in Q.items():
        t0 = time.time()
        try:
            rows = query(sql, as_dataframe=False)
        except Exception as exc:  # noqa: BLE001 - surface and continue
            print(f"!! {name}: FAILED after {time.time() - t0:.1f}s\n   {exc}\n", flush=True)
            failed.append(name)
            continue
        path = OUT / f"rec_{name}.tsv"
        with path.open("w", newline="", encoding="utf-8") as fh:
            if rows:
                w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()), delimiter="\t")
                w.writeheader()
                w.writerows(rows)
            else:
                fh.write("(no rows)\n")
        print(f"== {name}: {len(rows)} rows, {time.time() - t0:.1f}s -> {path}", flush=True)

        if name == "B2_bookings_new_by_year":
            published = {"2023": 10571, "2024": 10867, "2025": 10985}
            print("\n   csi_bookings_new against the published figures:")
            print(f"   {'yr':<6}{'new.hidden_0':>14}{'published':>11}{'gap':>7}")
            for r in rows:
                yr = str(r.get("yr"))
                if yr in published:
                    got = int(r.get("hidden_0") or 0)
                    print(f"   {yr:<6}{got:>14}{published[yr]:>11}{got - published[yr]:>+7}")
            print("   If every gap is 0, the published figures come from this table.\n")

    print(f"\n{len(Q) - len(failed)}/{len(Q)} queries succeeded.", flush=True)
    if failed:
        print("FAILED: " + ", ".join(failed), flush=True)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
