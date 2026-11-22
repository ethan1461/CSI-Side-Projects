-- Everything still needed to price the 286 IMS Army shipments. Read-only.
-- Four results. D is the one that is genuinely missing; A-C are lookups.
--
-- CLAUDE.md §7.2 - no decedent or family data. D reads only the booking's
-- shipment TYPE (casket / ashes / infant / combo), never the deceased table.

-- ============================================================
-- A. Carrier zones for the 83 airports in the extract.
--    Each carrier has its own column; a Delta "NE" is not a United "NE".
-- ============================================================
SELECT airport_code, us_state,
       american_region, delta_region, southwest_zone, united_region
FROM csi_airport_metadata_new
WHERE airport_code IN (
 'ABQ','ALB','ATL','AUS','BDL','BHM','BNA','BOI','BOS','BUF','BWI','CLE','CLT','CMH',
 'CVG','DAL','DCA','DEN','DFW','DSM','DTW','ELP','EWR','FAR','FAT','FLL','GRR','GSO',
 'GSP','GUM','HNL','IAH','IND','IST','ITO','JAX','JFK','LAS','LAX','LGA','LIT','MAF',
 'MCI','MCO','MDT','MDW','MEM','MIA','MKE','MSP','MSY','MYR','NIM','OKC','OMA','ONT',
 'ORD','ORF','PDX','PHL','PHX','PIT','PNS','RDU','RIC','ROC','RSW','SAN','SAT','SAV',
 'SDF','SEA','SFO','SJC','SJU','SLC','SMF','SPN','STL','TPA','TUL','TUS','TYS')
ORDER BY airport_code;

-- ============================================================
-- B. State-level regions. Needed for American's Hawaii and Puerto Rico
--    rates, which are stored by state rather than zone-to-zone.
-- ============================================================
SELECT * FROM csi_rate_domestic_regions_new ORDER BY state;

-- ============================================================
-- C. The published rates for the four majors, WITH shipment type and the
--    active flag the CSV export dropped.
-- ============================================================
SELECT r.rate_id, r.airline, r.origin_type, r.origin,
       r.destination_type, r.destination, r.rate_type,
       r.published_rate, r.shipment_rate_type_id, t.name AS shipment_type,
       r.included_weight, r.weight_unit, r.flat_overage_surcharge,
       r.is_active, r.effective_as_of
FROM csi_rates_new r
LEFT JOIN csi_shipment_rate_types t
       ON t.id = r.shipment_rate_type_id          -- adjust if the PK is named differently
WHERE r.airline IN ('American Airlines','Delta Airlines',
                    'Southwest Airlines','United Airlines')
  AND r.is_active = 1
ORDER BY r.airline, r.origin, r.destination, r.shipment_rate_type_id;

-- ============================================================
-- D. THE MISSING PIECE: shipment type per booking, for the 286.
--    Without this every shipment could be priced three ways.
--    If shipment_rate_type_id is not on csi_bookings, run
--      SELECT table_name, column_name FROM information_schema.columns
--      WHERE table_schema = DATABASE()
--        AND (column_name LIKE '%shipment_rate_type%'
--          OR column_name LIKE '%shipment_type%');
--    and send that instead.
-- ============================================================
SELECT b.booking_id, b.shipment_rate_type_id, t.name AS shipment_type
FROM csi_bookings b
LEFT JOIN csi_shipment_rate_types t
       ON t.id = b.shipment_rate_type_id
JOIN csi_booking_shipper_information s ON s.booking_id = b.booking_id
LEFT JOIN csi_new_shipper_to_invoice nsti ON nsti.booking_id = b.booking_id
WHERE b.hidden = 0
  AND s.shipper_funeral_home_id IN
      (2798, 16315, 2771, 17358, 2996, 2799, 9393, 12568, 3063, 17257, 3104, 2773)
  AND STR_TO_DATE(b.registration_date, '%m/%d/%Y') >= '2026-01-01'
  AND COALESCE(nsti.shipper_id, s.shipper_funeral_home_id) = 2767
ORDER BY b.booking_id;
