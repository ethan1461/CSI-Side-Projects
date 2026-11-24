-- Where CSI ships: origin and destination geography across the whole book.
--
-- Serves two asks (2026-11-24):
--   1. Counsel (Matt Glick) - highest-volume sending and receiving states and
--      countries, to scope cross-border privacy obligations.
--   2. Rowland Brothers - estimated annual volumes to the UK, Europe ex-UK,
--      Ukraine, South-East Asia, Middle East, Australia/NZ and South America,
--      so they can quote a flat rate against real traffic.
--
-- Returns AGGREGATES ONLY - counts by geography, never a shipment list.
-- CLAUDE.md §7.2: no decedent or family data is read. The deceased table carries
-- airport columns and is deliberately not joined.
--
-- Needs MySQL 8 for CTEs. Read-only.
-- Owner: pm-orchestrator · Created: 2026-11-24

-- ============================================================
-- 0. What geography does the airport table actually hold?
--    Run this first; if there is a country column, say so and I will use it
--    instead of inferring the UK and Ukraine from sub-region.
-- ============================================================
SHOW COLUMNS FROM csi_airport_metadata_new;

-- ============================================================
-- 1 & 2. Route ends per booking, then aggregated.
--
-- The first origin is the origin that is no other leg's destination; the final
-- destination is the destination that is no other leg's origin. Same connectivity
-- rule as the IMS pull - leg ids only sort within a booking and some domestic
-- flights are filed as international legs, so neither is trustworthy for ordering.
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
    SELECT l.booking_id, l.origin AS ap
    FROM all_legs l
    WHERE NOT EXISTS (SELECT 1 FROM all_legs x
                      WHERE x.booking_id = l.booking_id AND x.destination = l.origin)
),
last_leg AS (
    SELECT l.booking_id, l.destination AS ap
    FROM all_legs l
    WHERE NOT EXISTS (SELECT 1 FROM all_legs x
                      WHERE x.booking_id = l.booking_id AND x.origin = l.destination)
)

-- 1. SENDING geography
SELECT 'ORIGIN' AS end_of_route,
       c.airport_code,
       m.us_state, m.region, m.sub_region, m.intermediate_region,
       COUNT(DISTINCT f.booking_id) AS bookings
FROM first_leg f
JOIN csi_iata_codes c ON c.iata_code_id = f.ap
LEFT JOIN csi_airport_metadata_new m ON m.airport_code = c.airport_code
GROUP BY c.airport_code, m.us_state, m.region, m.sub_region, m.intermediate_region
HAVING bookings >= 5
ORDER BY bookings DESC;

-- 2. RECEIVING geography. Run separately; same CTE block above.
--    (Re-paste the WITH block, then this SELECT.)
--
-- SELECT 'DESTINATION' AS end_of_route,
--        c.airport_code,
--        m.us_state, m.region, m.sub_region, m.intermediate_region,
--        COUNT(DISTINCT t.booking_id) AS bookings
-- FROM last_leg t
-- JOIN csi_iata_codes c ON c.iata_code_id = t.ap
-- LEFT JOIN csi_airport_metadata_new m ON m.airport_code = c.airport_code
-- GROUP BY c.airport_code, m.us_state, m.region, m.sub_region, m.intermediate_region
-- HAVING bookings >= 3
-- ORDER BY bookings DESC;

-- ============================================================
-- 3. Bookings per year, so the above can be stated as an annual rate
--    rather than a total over an unclear window.
-- ============================================================
-- SELECT SUBSTRING(b.registration_date, 7, 4) AS yr, COUNT(*) AS bookings
-- FROM csi_bookings b WHERE b.hidden = 0
-- GROUP BY yr ORDER BY yr;
