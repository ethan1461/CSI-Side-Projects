"""Round 1 of the platform-metrics pull: schema discovery + the metrics computable today.

WHY THIS EXISTS
    `reports/ai-rollup-thesis-grounding.md` concludes that the prize in the AI-roll-up
    thesis is multiple expansion, and that a multiple has to be *demonstrated*. The two
    screens the investors running this model actually use are (a) logo retention and net
    revenue retention, and (b) the share of work that is rule-bound enough to automate.
    CSI has never computed either. This script starts both.

WHY IT IS "ROUND 1"
    The money column names on `csi_bookings` are not known to this repo, so revenue-based
    metrics (NRR, revenue per head, yield by cohort) cannot be written yet without
    guessing. Query D1 returns every table and its columns; round 2 is written from that
    and adds the revenue half. Everything that does NOT need a money column is in here
    and runs now.

PRIVACY — CLAUDE.md §7.2, read before editing
    `csi_booking_deceased_information` is NEVER joined, and D1 excludes it by name so its
    columns are not even listed. No query selects a name, address, or certificate field.
    Customer identifiers are funeral-home BUSINESS ids, not individuals. Every output is
    an aggregate count or an id-to-count mapping. Do not add a column to any query here
    without re-reading §7.2 first.

HOW TO RUN
    python platform_metrics_round1.py /path/to/output/dir

    Writes one TSV per query. Send pm1_D1_schema.tsv first — it unblocks round 2.

OUTPUTS
    pm1_D1_schema.tsv          every table, approx row count, column list
    pm1_D2_join_cardinality    whether the bill-to joins fan out (guards every other query)
    pm1_D3_date_sanity         registration_date format check and year spread
    pm1_R1_customer_year       customer x year booking matrix -> retention, churn, cohorts
    pm1_R2_customer_first_last customer tenure -> survival curves
    pm1_A1_lane_concentration  repeated lane patterns -> automatability proxy
    pm1_A2_intl_share_by_year  international share -> documentation-work proxy

OWNER      pm-orchestrator, for data-analyst to consume
CREATED    2026-11-24
RE-RUNNABLE  yes. Read-only; no writes to the database.
"""

import csv
import sys
import time

from utils.query import query

OUT = sys.argv[1] if len(sys.argv) > 1 else "."

# Shared leg-chaining logic. leg_type and leg_seq are both unreliable, so routes are
# ordered by connectivity: the first origin is the origin that is no other leg's
# destination; the last destination is the destination that is no other leg's origin.
LEGS = """WITH all_legs AS (
    SELECT d.booking_id, d.origin, d.destination
    FROM csi_booking_domestic_airline d
    JOIN csi_bookings b ON b.booking_id = d.booking_id AND b.hidden = 0
    UNION ALL
    SELECT i.booking_id, i.origin, i.destination
    FROM csi_booking_inter_airline i
    JOIN csi_bookings b ON b.booking_id = i.booking_id AND b.hidden = 0
)"""
FIRST = """, first_leg AS (
    SELECT DISTINCT l.booking_id, l.origin AS ap FROM all_legs l
    WHERE NOT EXISTS (SELECT 1 FROM all_legs x
                      WHERE x.booking_id = l.booking_id AND x.destination = l.origin))"""
LAST = """, last_leg AS (
    SELECT DISTINCT l.booking_id, l.destination AS ap FROM all_legs l
    WHERE NOT EXISTS (SELECT 1 FROM all_legs x
                      WHERE x.booking_id = l.booking_id AND x.origin = l.destination))"""

# The bill-to rule established in the IMS work: the invoice table wins, falling back to
# the shipper record. DISTINCT guards against either table fanning out - D2 verifies.
BILLTO = """SELECT DISTINCT b.booking_id,
       COALESCE(i.shipper_id, s.shipper_funeral_home_id) AS billto_id,
       SUBSTRING(b.registration_date, 7, 4) AS yr
FROM csi_bookings b
LEFT JOIN csi_new_shipper_to_invoice i ON i.booking_id = b.booking_id
LEFT JOIN csi_booking_shipper_information s ON s.booking_id = b.booking_id
WHERE b.hidden = 0"""

Q = {
    # ---------- discovery ----------
    # One row per table with its full column list. group_concat truncates at 1024 chars by
    # default, so n_cols is returned too: if n_cols looks higher than the list, say so and
    # that table gets its own SHOW COLUMNS in round 2.
    "D1_schema": """
SELECT c.TABLE_NAME,
       COUNT(*) AS n_cols,
       MAX(t.TABLE_ROWS) AS approx_rows,
       GROUP_CONCAT(c.COLUMN_NAME ORDER BY c.ORDINAL_POSITION SEPARATOR ', ') AS cols
FROM INFORMATION_SCHEMA.COLUMNS c
LEFT JOIN INFORMATION_SCHEMA.TABLES t
       ON t.TABLE_SCHEMA = c.TABLE_SCHEMA AND t.TABLE_NAME = c.TABLE_NAME
WHERE c.TABLE_SCHEMA = DATABASE()
  AND c.TABLE_NAME NOT LIKE '%deceased%'
GROUP BY c.TABLE_NAME
ORDER BY c.TABLE_NAME""",
    # Does either bill-to table have more than one row per booking? If any cnt > 1
    # appears, every per-booking count built on these joins needs DISTINCT (they all
    # already use it) and round 2 needs a tie-break rule for revenue.
    "D2_join_cardinality": """
SELECT 'invoice_rows_per_booking' AS check_name, cnt AS rows_per_booking,
       COUNT(*) AS n_bookings
FROM (SELECT booking_id, COUNT(*) AS cnt FROM csi_new_shipper_to_invoice
      GROUP BY booking_id) a
GROUP BY cnt
UNION ALL
SELECT 'shipper_rows_per_booking', cnt, COUNT(*)
FROM (SELECT booking_id, COUNT(*) AS cnt FROM csi_booking_shipper_information
      GROUP BY booking_id) b
GROUP BY cnt
ORDER BY check_name, rows_per_booking""",
    # registration_date is TEXT in MM/DD/YYYY. Confirm nothing else is in there before any
    # year-based metric is trusted.
    "D3_date_sanity": """
SELECT CASE
         WHEN b.registration_date IS NULL OR b.registration_date = '' THEN 'empty'
         WHEN b.registration_date REGEXP '^[0-9]{2}/[0-9]{2}/[0-9]{4}$' THEN 'MM/DD/YYYY'
         ELSE 'other'
       END AS date_shape,
       SUBSTRING(b.registration_date, 7, 4) AS yr,
       COUNT(*) AS n
FROM csi_bookings b
WHERE b.hidden = 0
GROUP BY date_shape, yr
ORDER BY date_shape, yr""",
    # ---------- retention: the primary screen ----------
    # Customer x year booking matrix. Logo retention, gross and net churn, new vs
    # returning, and cohort survival all derive from this one table, computed locally.
    # Ids only - no funeral-home names leave the database.
    "R1_customer_year": f"""
SELECT x.billto_id, x.yr, COUNT(*) AS bookings
FROM ({BILLTO}) x
WHERE x.billto_id IS NOT NULL
  AND x.yr REGEXP '^[0-9]{{4}}$'
GROUP BY x.billto_id, x.yr
ORDER BY x.billto_id, x.yr""",
    # Tenure per customer, for survival curves and to separate "lost" from "never
    # repeated". A one-booking customer is a different problem from a churned one.
    "R2_customer_first_last": f"""
SELECT x.billto_id,
       MIN(x.yr) AS first_yr,
       MAX(x.yr) AS last_yr,
       COUNT(DISTINCT x.yr) AS active_years,
       COUNT(*) AS lifetime_bookings
FROM ({BILLTO}) x
WHERE x.billto_id IS NOT NULL
  AND x.yr REGEXP '^[0-9]{{4}}$'
GROUP BY x.billto_id
ORDER BY lifetime_bookings DESC""",
    # ---------- automatability proxy ----------
    # The published screen wants 30-70% of work rule-bound. Nobody can answer that from
    # the database alone - it needs Vadim's hours per booking type and Donald's cost per
    # hour. But repetition is a defensible PROXY: a lane flown 400 times is rule-bound
    # work; a lane flown once is bespoke. This gives the concentration curve, from which
    # the share of volume sitting in the top N repeated patterns is computed locally.
    "A1_lane_concentration": f"""{LEGS}{FIRST}{LAST}
SELECT f.ap AS origin_id, t.ap AS dest_id, COUNT(DISTINCT f.booking_id) AS bookings
FROM first_leg f
JOIN last_leg t ON t.booking_id = f.booking_id
GROUP BY f.ap, t.ap
ORDER BY bookings DESC""",
    # International share by year. International is where the consular documentation,
    # apostille and customs work lives - the most rule-bound, highest-volume paperwork in
    # the business, and therefore where an automation pilot should be aimed.
    "A2_intl_share_by_year": f"""{LEGS}{LAST}
SELECT SUBSTRING(b.registration_date, 7, 4) AS yr,
       CASE WHEN COALESCE(m.country_name, '') LIKE 'United State%' THEN 'domestic'
            WHEN COALESCE(m.country_name, '') = '' THEN 'unmapped'
            ELSE 'international' END AS leg_type,
       COUNT(DISTINCT t.booking_id) AS bookings
FROM last_leg t
JOIN csi_bookings b ON b.booking_id = t.booking_id
LEFT JOIN csi_airport_metadata_new m ON m.iata_code_id = t.ap
GROUP BY yr, leg_type
HAVING yr REGEXP '^[0-9]{{4}}$'
ORDER BY yr, leg_type""",
}


def main() -> None:
    """Run every query and write one TSV each."""
    for name, sql in Q.items():
        t0 = time.time()
        try:
            rows = query(sql, as_dataframe=False)
        except Exception as exc:  # noqa: BLE001 - surface loudly, keep going
            print(f"!! {name}: FAILED after {time.time() - t0:.1f}s\n   {exc}", flush=True)
            continue
        path = f"{OUT}/pm1_{name}.tsv"
        with open(path, "w", newline="", encoding="utf-8") as fh:
            if rows:
                w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()), delimiter="\t")
                w.writeheader()
                w.writerows(rows)
        print(f"== {name}: {len(rows)} rows, {time.time() - t0:.1f}s -> {path}", flush=True)


if __name__ == "__main__":
    main()
