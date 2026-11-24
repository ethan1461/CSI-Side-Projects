"""Round 2: realised carrier margin, and retention at both grains on a monthly grid.

RUN THIS FROM THE ENVIRONMENT ROUND 1 RAN IN
    `from utils.query import query` resolves on Ethan's machine (the backend helper that
    `scripts/db/README.md` permits), not from this repo, which has no `utils/` package.
    Round 1 ran there successfully. This is not a defect; it is a note for anyone
    reviewing the file from inside the repo and finding no such module.

        python platform_metrics_round2.py /path/to/output/dir

WHAT ROUND 1 RETURNED, AND WHAT IS FIXED HERE
    Ethan ran round 1 and returned D1-D3. data-analyst reviewed the script. Every
    substantive correction from both is applied:

    - **ALREADY PAID (funeral_home_id 8652) excluded.** Not a customer; 559 bookings
      across 2023-2026, inflating the customer count and the churn.
    - **Monthly grid, not annual.** `context/metric-definitions.md` §D fixes the retention
      window at N = 365 days with half-open windows, and forbids two windows in one table.
      A customer x year matrix cannot reproduce that and would create a second,
      incompatible retention series. Customer x **month** supports the 365-day rolling
      definition, calendar years, and cohort survival from one pull.
    - **Both grains, because they answer different questions** (M-25, now binding). The
      bill-to payer is the unit of dollars and ties to the books; the shipping funeral home
      is the unit of demand and of acquisition. They diverge on partner-routed volume,
      where ~254 homes collapse into four payers, which mechanically flatters logo
      retention. The existing published series is already on the shipping grain, so a
      bill-to-only pull would silently replace it rather than extend it. Both columns are
      returned.
    - **Attribution reported, never dropped** (M-23). 1,451 dated bookings have no bill-to
      at all. Q D5 breaks every booking down by attribution state, including a zero
      sentinel the COALESCE would not catch.
    - **Reconciliation gates the rest.** Q D6 counts bookings by year straight from the
      database against the published 10,571 / 10,867 / 10,985. If 2025 does not come back
      10,985, every number here sits on a different population from every published CSI
      figure, and that is the first thing a buyer's analyst would find.
    - **`hidden` is not a status filter.** M-02 defines a landed booking as completed and
      not cancelled; `hidden = 0` is not that. Q D7 returns bookings by year by status and
      by `hidden` so the choice is explicit and any delta is diagnosable in one pass.
    - **Leg-chaining loss is now measured.** The connectivity logic silently drops a
      booking whose legs revisit an airport (MIA->JFK plus JFK->MIA leaves no origin that
      is not also a destination, so `first_leg` returns nothing), and double-counts one
      with two independent origins. Q D8 reports both. This is the residual between 47,876
      resolved destinations and 49,128 visible dated bookings.
    - **Duplicate `iata_code_id` check restored.** `csi_airport_metadata_new` has no key
      and every column is nullable, so a duplicated id fans out every LEFT JOIN to it.
      Q D9 runs it; `shipping-geography.sql` does the same for the same reason.
    - **Lane grain changed, and this one changes the answer.** Paperwork is driven by
      destination country and shipment type, not by the airport pair: MIA->SDQ and
      JFK->SDQ share nearly all their documentation. Airport-pair concentration therefore
      **understates** how rule-bound the work is. Q A3 groups on origin airport,
      destination country and shipment type, by year.
    - **Destination class now uses the leg pair.** Classifying on the last leg alone marks
      an inbound repatriation whose final leg is US->US as "domestic" - and those carry the
      *most* international documentation. CSI's physical handling is export-only, so
      inbound is a different workflow. Q A4 classifies on (first-leg country, last-leg
      country) and puts US territories in their own bucket rather than letting a LIKE
      decide.

WHY THIS ROUND MATTERS MOST
    **`csi_airline_invoice_lines.billed_amount` is what the carrier actually charged.**
    `CLAUDE.md` §4.3 records cost as unknown for 15 carriers covering 6,441 of 6,919
    published lanes - "93% of the lane book has no cost side" - and
    `reports/carrier-margin-resolved.md` could only produce rate-card margin, unweighted by
    volume and excluding cost to serve. If this table holds real billed amounts per
    booking, CSI has **actual realised margin per shipment**. Q M1 tests it and Q M2
    reports coverage, because a margin figure is worth only the share of bookings carrying
    both sides. Margin is the lever in the 8-10x strategy, so this is the most valuable
    query in the file.

PRIVACY - CLAUDE.md §7.2
    `csi_booking_deceased_information` is never joined. No query selects a name, address or
    certificate field. Customer identifiers are funeral-home business ids. Outputs are
    aggregates or id-to-value mappings.

OWNER      pm-orchestrator, for data-analyst
CREATED    2026-11-24
RE-RUNNABLE  yes. Read-only; no writes to the database.
"""

import csv
import json
import sys
import time
from datetime import UTC, datetime
from pathlib import Path

from utils.query import query

SCRIPT_VERSION = "2.0.0"
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path()
NOT_A_CUSTOMER = "8652"  # ALREADY PAID - Ethan, 2026-11-24

# Both grains on every row, plus a month key. D2 confirmed at most one invoice-override row
# and exactly one shipper row per booking, so this cannot fan out; the MIN() is belt and
# braces so a future duplicate with a differing id cannot silently split one booking
# across two customers (DISTINCT would not catch that - it collapses identical tuples, not
# a fan-out with differing ids).
BILLTO = f"""SELECT b.booking_id,
       MIN(COALESCE(i.shipper_id, s.shipper_funeral_home_id)) AS billto_id,
       MIN(s.shipper_funeral_home_id) AS shipping_fh_id,
       SUBSTRING(b.registration_date, 7, 4) AS yr,
       CONCAT(SUBSTRING(b.registration_date, 7, 4), '-',
              SUBSTRING(b.registration_date, 1, 2)) AS ym,
       STR_TO_DATE(b.registration_date, '%m/%d/%Y') AS reg_date
FROM csi_bookings b
LEFT JOIN csi_new_shipper_to_invoice i ON i.booking_id = b.booking_id
LEFT JOIN csi_booking_shipper_information s ON s.booking_id = b.booking_id
WHERE b.hidden = 0
GROUP BY b.booking_id, yr, ym, reg_date
HAVING billto_id IS NOT NULL
   AND billto_id NOT IN (0, {NOT_A_CUSTOMER})"""

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

INVOICED = """(SELECT booking_id, SUM(invoiced_amount) AS invoiced_amount
            FROM csi_invoiced_bookings GROUP BY booking_id)"""
CARRIER = """(SELECT booking_id, SUM(billed_amount) AS carrier_cost
           FROM csi_airline_invoice_lines GROUP BY booking_id)"""

Q = {
    # ================= gates: run first, read first =================
    # Does the database agree with every published CSI figure? Three lines, and it decides
    # whether anything else here is quotable.
    "D6_reconcile_bookings_by_year": """
SELECT SUBSTRING(registration_date, 7, 4) AS yr, COUNT(*) AS bookings_hidden_0
FROM csi_bookings WHERE hidden = 0
GROUP BY yr ORDER BY yr""",
    # hidden is not a status. Make the filter choice explicit and diagnosable.
    "D7_status_and_hidden": """
SELECT SUBSTRING(b.registration_date, 7, 4) AS yr, b.hidden,
       COALESCE(b.status, '(null)') AS status, COUNT(*) AS bookings
FROM csi_bookings b
GROUP BY yr, b.hidden, status
ORDER BY yr, b.hidden, status""",
    # Columns for the tables round 1 could not see into. csi_bookings_new truncated at 54
    # of 88 in D1.
    "D4_money_tables": """
SELECT TABLE_NAME, ORDINAL_POSITION, COLUMN_NAME, DATA_TYPE, IS_NULLABLE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = DATABASE()
  AND TABLE_NAME IN ('csi_bookings_new', 'csi_invoiced_bookings',
                     'csi_airline_invoice_lines', 'csi_fh_dedup_pairs',
                     'csi_booking_rates', 'csi_booking_rate_line_items')
ORDER BY TABLE_NAME, ORDINAL_POSITION""",
    # Attribution state for every booking. Reported, never dropped (M-23).
    "D5_attribution_state": """
SELECT SUBSTRING(b.registration_date, 7, 4) AS yr,
       CASE
         WHEN i.shipper_id IS NOT NULL AND s.shipper_funeral_home_id IS NOT NULL
              THEN 'both'
         WHEN i.shipper_id IS NOT NULL THEN 'invoice_override_only'
         WHEN s.shipper_funeral_home_id IS NOT NULL THEN 'shipper_only'
         ELSE 'neither'
       END AS attribution,
       SUM(CASE WHEN COALESCE(i.shipper_id, s.shipper_funeral_home_id) = 0
                THEN 1 ELSE 0 END) AS zero_sentinel,
       COUNT(*) AS bookings
FROM csi_bookings b
LEFT JOIN csi_new_shipper_to_invoice i ON i.booking_id = b.booking_id
LEFT JOIN csi_booking_shipper_information s ON s.booking_id = b.booking_id
WHERE b.hidden = 0
GROUP BY yr, attribution
ORDER BY yr, attribution""",
    # How many bookings does the leg chaining lose or double-count?
    "D8_leg_chain_loss": f"""{LEGS}{FIRST}{LAST}
SELECT (SELECT COUNT(DISTINCT booking_id) FROM all_legs)   AS bookings_with_legs,
       (SELECT COUNT(DISTINCT booking_id) FROM first_leg)  AS with_first_leg,
       (SELECT COUNT(DISTINCT booking_id) FROM last_leg)   AS with_last_leg,
       (SELECT COUNT(*) FROM (SELECT booking_id FROM first_leg
                              GROUP BY booking_id HAVING COUNT(*) > 1) a)
                                                           AS multi_first_leg,
       (SELECT COUNT(*) FROM (SELECT booking_id FROM last_leg
                              GROUP BY booking_id HAVING COUNT(*) > 1) b)
                                                           AS multi_last_leg""",
    # The metadata table has no key. A duplicated id fans out every join to it.
    "D9_airport_metadata_dupes": """
SELECT iata_code_id, COUNT(*) AS rows_for_id
FROM csi_airport_metadata_new
GROUP BY iata_code_id HAVING COUNT(*) > 1
ORDER BY rows_for_id DESC""",
    # ================= the margin question =================
    "M1_realised_margin_by_year": f"""{LEGS}{LAST}
SELECT SUBSTRING(b.registration_date, 7, 4) AS yr,
       CASE WHEN COALESCE(m.country_name, '') = '' THEN 'unmapped'
            WHEN m.us_state IN ('PR','VI','GU','AS','MP','UM') THEN 'us_territory'
            WHEN m.us_state IS NOT NULL AND m.us_state <> '' THEN 'us_state'
            ELSE 'foreign' END AS dest_class,
       COUNT(DISTINCT b.booking_id)   AS bookings,
       COUNT(DISTINCT inv.booking_id) AS with_invoice,
       COUNT(DISTINCT ail.booking_id) AS with_carrier_cost,
       ROUND(SUM(inv.invoiced_amount), 2) AS invoiced,
       ROUND(SUM(ail.carrier_cost), 2)    AS carrier_cost
FROM csi_bookings b
LEFT JOIN last_leg t ON t.booking_id = b.booking_id
LEFT JOIN csi_airport_metadata_new m ON m.iata_code_id = t.ap
LEFT JOIN {INVOICED} inv ON inv.booking_id = b.booking_id
LEFT JOIN {CARRIER} ail ON ail.booking_id = b.booking_id
WHERE b.hidden = 0
GROUP BY yr, dest_class
HAVING yr REGEXP '^[0-9]{{4}}$'
ORDER BY yr, dest_class""",
    "M2_cost_coverage": f"""
SELECT SUBSTRING(b.registration_date, 7, 4) AS yr,
       COUNT(*) AS visible_bookings,
       SUM(CASE WHEN inv.booking_id IS NOT NULL THEN 1 ELSE 0 END) AS has_invoice,
       SUM(CASE WHEN ail.booking_id IS NOT NULL THEN 1 ELSE 0 END) AS has_carrier_cost,
       SUM(CASE WHEN inv.booking_id IS NOT NULL AND ail.booking_id IS NOT NULL
                THEN 1 ELSE 0 END) AS has_both
FROM csi_bookings b
LEFT JOIN (SELECT DISTINCT booking_id FROM csi_invoiced_bookings) inv
       ON inv.booking_id = b.booking_id
LEFT JOIN (SELECT DISTINCT booking_id FROM csi_airline_invoice_lines) ail
       ON ail.booking_id = b.booking_id
WHERE b.hidden = 0
GROUP BY yr HAVING yr REGEXP '^[0-9]{{4}}$' ORDER BY yr""",
    # ================= retention, monthly, both grains =================
    # One pull that supports the binding 365-day rolling window, calendar years, and
    # cohort survival. Dedup applied so a merged home does not read as one lost and one
    # gained.
    "R6_customer_month_both_grains": f"""
SELECT COALESCE(dpb.canonical_id, x.billto_id) AS billto_id,
       COALESCE(dps.canonical_id, x.shipping_fh_id) AS shipping_fh_id,
       x.ym,
       COUNT(DISTINCT x.booking_id) AS bookings,
       ROUND(SUM(COALESCE(inv.invoiced_amount, 0)), 2) AS invoiced
FROM ({BILLTO}) x
LEFT JOIN {INVOICED} inv ON inv.booking_id = x.booking_id
LEFT JOIN csi_fh_dedup_pairs dpb ON dpb.duplicate_id = x.billto_id
LEFT JOIN csi_fh_dedup_pairs dps ON dps.duplicate_id = x.shipping_fh_id
WHERE x.yr REGEXP '^[0-9]{{4}}$'
GROUP BY billto_id, shipping_fh_id, x.ym
ORDER BY x.ym, billto_id""",
    # ================= automation proxies, corrected =================
    # Destination country x shipment type is the grain the paperwork actually follows.
    "A3_work_pattern_concentration": f"""{LEGS}{FIRST}{LAST}
SELECT SUBSTRING(b.registration_date, 7, 4) AS yr,
       COALESCE(mo.airport_code, CONCAT('id:', f.ap)) AS origin,
       COALESCE(md.country_name, '(unmapped)') AS dest_country,
       COALESCE(st.shipment_rate_type, CONCAT('type:', b.shipment_rate_type_id))
            AS shipment_type,
       COUNT(DISTINCT f.booking_id) AS bookings
FROM first_leg f
JOIN last_leg t ON t.booking_id = f.booking_id
JOIN csi_bookings b ON b.booking_id = f.booking_id
LEFT JOIN csi_airport_metadata_new mo ON mo.iata_code_id = f.ap
LEFT JOIN csi_airport_metadata_new md ON md.iata_code_id = t.ap
LEFT JOIN csi_shipment_rate_types st
       ON st.shipment_rate_type_id = b.shipment_rate_type_id
GROUP BY yr, origin, dest_country, shipment_type
HAVING yr REGEXP '^[0-9]{{4}}$'
ORDER BY bookings DESC""",
    # Classified on the leg PAIR, so inbound repatriation is not mislabelled domestic.
    "A4_flow_direction_by_year": f"""{LEGS}{FIRST}{LAST}
SELECT SUBSTRING(b.registration_date, 7, 4) AS yr,
       CASE WHEN COALESCE(mo.us_state, '') <> '' THEN 'US' ELSE 'foreign' END AS origin_side,
       CASE WHEN COALESCE(md.country_name, '') = '' THEN 'unmapped'
            WHEN md.us_state IN ('PR','VI','GU','AS','MP','UM') THEN 'us_territory'
            WHEN COALESCE(md.us_state, '') <> '' THEN 'us_state'
            ELSE 'foreign' END AS dest_side,
       COUNT(DISTINCT f.booking_id) AS bookings
FROM first_leg f
JOIN last_leg t ON t.booking_id = f.booking_id
JOIN csi_bookings b ON b.booking_id = f.booking_id
LEFT JOIN csi_airport_metadata_new mo ON mo.iata_code_id = f.ap
LEFT JOIN csi_airport_metadata_new md ON md.iata_code_id = t.ap
GROUP BY yr, origin_side, dest_side
HAVING yr REGEXP '^[0-9]{{4}}$'
ORDER BY yr, origin_side, dest_side""",
}


def main() -> int:
    """Run every query independently, write a TSV and a .meta.json for each."""
    OUT.mkdir(parents=True, exist_ok=True)
    failed: list[str] = []
    for name, sql in Q.items():
        t0 = time.time()
        try:
            rows = query(sql, as_dataframe=False)
        except Exception as exc:  # noqa: BLE001 - one bad column must not stop the rest
            print(f"!! {name}: FAILED after {time.time() - t0:.1f}s\n   {exc}\n", flush=True)
            failed.append(name)
            continue
        path = OUT / f"pm2_{name}.tsv"
        with path.open("w", newline="", encoding="utf-8") as fh:
            if rows:
                w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()), delimiter="\t")
                w.writeheader()
                w.writerows(rows)
            else:
                fh.write("(no rows)\n")
        path.with_suffix(".meta.json").write_text(
            json.dumps(
                {
                    "query": name,
                    "script": "scripts/db/platform_metrics_round2.py",
                    "script_version": SCRIPT_VERSION,
                    "generated_at": datetime.now(UTC).isoformat(),
                    "row_count": len(rows),
                    "excluded": [f"funeral_home_id {NOT_A_CUSTOMER} (ALREADY PAID)"],
                    "pii": "none - aggregate counts and business ids (CLAUDE.md s7.2)",
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        print(f"== {name}: {len(rows)} rows, {time.time() - t0:.1f}s -> {path}", flush=True)

    print(f"\n{len(Q) - len(failed)}/{len(Q)} queries succeeded.", flush=True)
    if failed:
        print("FAILED: " + ", ".join(failed), flush=True)
        print("Send the successful files anyway; say which failed.", flush=True)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
