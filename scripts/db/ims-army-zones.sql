-- What is needed to price the IMS Army shipments.
--
-- The published rate card prices the four US majors ZONE to ZONE (zone 1..7, plus
-- NE / Midwest / Central / HW / AK), not airport to airport. Without the zone
-- definitions none of the 286 shipments can be priced. Read-only.

-- A. Where are the zone definitions? Which airport / state / city maps to which zone.
SELECT table_name, column_name, data_type
FROM information_schema.columns
WHERE table_schema = DATABASE()
  AND (column_name LIKE '%zone%' OR table_name LIKE '%zone%')
ORDER BY table_name, column_name;

-- B. What does the rate table hold that the CSV export dropped?
--    Same zone pair appears twice at different published rates (e.g. Southwest
--    zone 1 -> zone 1 at both 244.38 and 653.44) with nothing in the export to
--    tell them apart. Something - service type, weight band, effective date -
--    distinguishes them and is not in the file.
SHOW COLUMNS FROM csi_rates_new;

-- C. The two Southwest zone 1 -> 1 rows in full, so the discriminator is visible.
SELECT * FROM csi_rates_new
WHERE airline LIKE '%Southwest%'
  AND origin = '1' AND destination = '1'
LIMIT 10;
