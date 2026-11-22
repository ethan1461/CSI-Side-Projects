-- Run this FIRST. Confirms the bill-to table's column names before the main pull,
-- and shows how the ten origin homes' 2026 bookings split by who was billed.
-- If the SHOW COLUMNS output does not contain booking_id and shipper_id,
-- stop and send it over - the main query's join will need changing.

SHOW COLUMNS FROM csi_new_shipper_to_invoice;

SELECT
    COALESCE(nsti.shipper_id, s.shipper_funeral_home_id) AS billed_to_id,
    COUNT(DISTINCT b.booking_id)                         AS bookings_2026
FROM csi_bookings b
JOIN csi_booking_shipper_information s
       ON s.booking_id = b.booking_id
LEFT JOIN csi_new_shipper_to_invoice nsti
       ON nsti.booking_id = b.booking_id
WHERE b.hidden = 0
  AND s.shipper_funeral_home_id IN
      (2798, 16315, 2771, 17358, 2996, 2799, 9393, 12568, 3063, 17257, 3104, 2773)
  AND STR_TO_DATE(b.registration_date, '%m/%d/%Y') >= '2026-01-01'
GROUP BY billed_to_id
ORDER BY bookings_2026 DESC;
