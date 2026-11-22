-- IMS Army lane pull — the ten origin funeral homes Paul Prikos listed 2026-11-20.
--
-- Returns ONE ROW PER FLIGHT LEG. The lane (first leg's origin, last leg's
-- destination) is assembled downstream, so this query assumes nothing about leg
-- ordering and needs no window functions.
--
-- REVISED 2026-11-22 (Ethan): filtered to shipments CSI BILLED TO IMS.
--   The first version returned everything from the ten origin homes. Paul wants
--   only the shipments IMS paid for, which is a much smaller set - those homes
--   also ship direct with CSI and through other partners.
--   Bill-to rule: COALESCE(csi_new_shipper_to_invoice.shipper_id,
--                          csi_booking_shipper_information.shipper_funeral_home_id)
--   IMS = funeral_home_id 2767 (International Mortuary Shipping, LLC, Spartanburg SC).
--
-- Run:  mysql -h <host> -u csi_read_only -p erp_production < ims-army-lanes.sql > ims-army-lanes.tsv
--
-- CLAUDE.md §7.2 — this query selects NO decedent or family data.
--   * csi_booking_deceased_information is deliberately NOT joined, although it
--     carries airport_origin / airport_destination. It holds decedent records.
--   * From csi_booking_shipper_information only booking_id and
--     shipper_funeral_home_id are read. Every other column in that table is the
--     funeral home's contact detail.
--   * Nothing here returns a name, address, phone or email.
--
-- Owner: pm-orchestrator · Created: 2026-11-22 · Read-only.

SELECT
    b.booking_id,
    b.registration_date,                 -- TEXT, MM/DD/YYYY. Parsed downstream.
    s.shipper_funeral_home_id            AS funeral_home_id,
    COALESCE(nsti.shipper_id,
             s.shipper_funeral_home_id)  AS billed_to_id,
    'domestic'                           AS leg_type,
    d.booking_domestic_airline_id        AS leg_seq,
    d.airline                            AS airline,
    d.flight                             AS flight,
    o.airport_code                       AS origin_airport,
    t.airport_code                       AS destination_airport
FROM csi_bookings b
JOIN csi_booking_shipper_information s
       ON s.booking_id = b.booking_id
JOIN csi_booking_domestic_airline d
       ON d.booking_id = b.booking_id
LEFT JOIN csi_new_shipper_to_invoice nsti
       ON nsti.booking_id = b.booking_id
LEFT JOIN csi_iata_codes o
       ON o.iata_code_id = d.origin
LEFT JOIN csi_iata_codes t
       ON t.iata_code_id = d.destination
WHERE b.hidden = 0
  AND s.shipper_funeral_home_id IN
      (2798, 16315, 2771, 17358, 2996, 2799, 9393, 12568, 3063, 17257, 3104, 2773)
  AND STR_TO_DATE(b.registration_date, '%m/%d/%Y') >= '2026-01-01'
  AND COALESCE(nsti.shipper_id, s.shipper_funeral_home_id) = 2767   -- billed to IMS

UNION ALL

SELECT
    b.booking_id,
    b.registration_date,
    s.shipper_funeral_home_id            AS funeral_home_id,
    COALESCE(nsti.shipper_id,
             s.shipper_funeral_home_id)  AS billed_to_id,
    'international'                      AS leg_type,
    i.booking_inter_airline_id           AS leg_seq,
    i.airline                            AS airline,
    i.flight                             AS flight,
    o.airport_code                       AS origin_airport,
    t.airport_code                       AS destination_airport
FROM csi_bookings b
JOIN csi_booking_shipper_information s
       ON s.booking_id = b.booking_id
JOIN csi_booking_inter_airline i
       ON i.booking_id = b.booking_id
LEFT JOIN csi_new_shipper_to_invoice nsti
       ON nsti.booking_id = b.booking_id
LEFT JOIN csi_iata_codes o
       ON o.iata_code_id = i.origin
LEFT JOIN csi_iata_codes t
       ON t.iata_code_id = i.destination
WHERE b.hidden = 0
  AND s.shipper_funeral_home_id IN
      (2798, 16315, 2771, 17358, 2996, 2799, 9393, 12568, 3063, 17257, 3104, 2773)
  AND STR_TO_DATE(b.registration_date, '%m/%d/%Y') >= '2026-01-01'
  AND COALESCE(nsti.shipper_id, s.shipper_funeral_home_id) = 2767   -- billed to IMS

ORDER BY booking_id, leg_type, leg_seq;
