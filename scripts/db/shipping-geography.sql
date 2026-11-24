-- Where CSI ships: origin and destination geography across the whole book.
--
-- Serves two asks (2026-11-24):
--   1. Counsel - highest-volume sending and receiving states and countries,
--      to scope cross-border privacy obligations.
--   2. Rowland Brothers - volumes to the UK, Europe ex-UK, Ukraine, South-East
--      Asia, Middle East, Australia/NZ and South America, so they can quote a
--      flat rate against real traffic.
--
-- AGGREGATES ONLY. Counts by geography, never a shipment list.
-- CLAUDE.md §7.2: no decedent or family data. csi_booking_deceased_information
-- carries airport columns and is deliberately NOT joined.
--
-- Joins legs straight to csi_airport_metadata_new on iata_code_id - the metadata
-- table carries it, so csi_iata_codes is not needed and no text join is involved.
--
-- Needs MySQL 8 for CTEs. Read-only.
-- Owner: pm-orchestrator · Created: 2026-11-24

-- ============================================================
-- 0. Sanity check. csi_airport_metadata_new has no key defined and every
--    column is nullable, so a duplicated iata_code_id would double-count.
--    Expect zero rows. If not, tell me before the numbers are used.
-- ============================================================
SELECT iata_code_id, COUNT(*) AS rows_for_this_id
FROM csi_airport_metadata_new
GROUP BY iata_code_id
HAVING COUNT(*) > 1
ORDER BY rows_for_this_id DESC
LIMIT 20;

-- ============================================================
-- 1. SENDING geography - where shipments start.
-- ============================================================
WITH all_legs AS (
    SELECT d.booking_id, d.origin, d.destination
    FROM csi_booking_domestic_airline d
    JOIN csi_bookings b ON b.booking_id = d.booking_id AND b.hidden = 0
    UNION ALL
    SELECT i.booking_id, i.origin, i.destination
    FROM csi_booking_inter_airline i
    JOIN csi_bookings b ON b.booking_id = i.booking_id AND b.hidden = 0
),
first_leg AS (
    SELECT DISTINCT l.booking_id, l.origin AS ap
    FROM all_legs l
    WHERE NOT EXISTS (SELECT 1 FROM all_legs x
                      WHERE x.booking_id = l.booking_id AND x.destination = l.origin)
)
SELECT m.country_name, m.alpha_3, m.us_state, m.state_name,
       m.region, m.sub_region,
       COUNT(DISTINCT f.booking_id) AS bookings
FROM first_leg f
LEFT JOIN csi_airport_metadata_new m ON m.iata_code_id = f.ap
GROUP BY m.country_name, m.alpha_3, m.us_state, m.state_name, m.region, m.sub_region
ORDER BY bookings DESC;

-- ============================================================
-- 2. RECEIVING geography - where shipments end. This is the one Rowland need.
-- ============================================================
WITH all_legs AS (
    SELECT d.booking_id, d.origin, d.destination
    FROM csi_booking_domestic_airline d
    JOIN csi_bookings b ON b.booking_id = d.booking_id AND b.hidden = 0
    UNION ALL
    SELECT i.booking_id, i.origin, i.destination
    FROM csi_booking_inter_airline i
    JOIN csi_bookings b ON b.booking_id = i.booking_id AND b.hidden = 0
),
last_leg AS (
    SELECT DISTINCT l.booking_id, l.destination AS ap
    FROM all_legs l
    WHERE NOT EXISTS (SELECT 1 FROM all_legs x
                      WHERE x.booking_id = l.booking_id AND x.origin = l.destination)
)
SELECT m.country_name, m.alpha_3, m.us_state, m.state_name,
       m.region, m.sub_region,
       COUNT(DISTINCT t.booking_id) AS bookings
FROM last_leg t
LEFT JOIN csi_airport_metadata_new m ON m.iata_code_id = t.ap
GROUP BY m.country_name, m.alpha_3, m.us_state, m.state_name, m.region, m.sub_region
ORDER BY bookings DESC;

-- ============================================================
-- 3. Bookings per year, so the above can be quoted as an annual rate rather
--    than a total over an unclear window. Rowland asked for ESTIMATED volumes.
-- ============================================================
SELECT SUBSTRING(b.registration_date, 7, 4) AS yr, COUNT(*) AS bookings
FROM csi_bookings b
WHERE b.hidden = 0
GROUP BY yr
ORDER BY yr;

-- ============================================================
-- 4. International destinations by YEAR, so the Rowland figures can be given
--    as a recent run-rate rather than a five-year average.
-- ============================================================
WITH all_legs AS (
    SELECT d.booking_id, d.origin, d.destination
    FROM csi_booking_domestic_airline d
    JOIN csi_bookings b ON b.booking_id = d.booking_id AND b.hidden = 0
    UNION ALL
    SELECT i.booking_id, i.origin, i.destination
    FROM csi_booking_inter_airline i
    JOIN csi_bookings b ON b.booking_id = i.booking_id AND b.hidden = 0
),
last_leg AS (
    SELECT DISTINCT l.booking_id, l.destination AS ap
    FROM all_legs l
    WHERE NOT EXISTS (SELECT 1 FROM all_legs x
                      WHERE x.booking_id = l.booking_id AND x.origin = l.destination)
)
SELECT SUBSTRING(b.registration_date, 7, 4) AS yr,
       m.country_name, m.alpha_3,
       COUNT(DISTINCT t.booking_id) AS bookings
FROM last_leg t
JOIN csi_bookings b ON b.booking_id = t.booking_id
LEFT JOIN csi_airport_metadata_new m ON m.iata_code_id = t.ap
WHERE COALESCE(m.country_name, '') <> 'United States'
GROUP BY yr, m.country_name, m.alpha_3
HAVING bookings >= 2
ORDER BY yr DESC, bookings DESC;
