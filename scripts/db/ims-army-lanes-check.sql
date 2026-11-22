-- Sanity check to run alongside ims-army-lanes.sql.
-- Bookings per funeral home, and how many carry no leg at all.
-- No decedent or contact data (CLAUDE.md §7.2).

SELECT
    s.shipper_funeral_home_id                                    AS funeral_home_id,
    COUNT(DISTINCT b.booking_id)                                 AS bookings_2026,
    COUNT(DISTINCT CASE WHEN d.booking_id IS NOT NULL
                        THEN b.booking_id END)                   AS with_domestic_leg,
    COUNT(DISTINCT CASE WHEN i.booking_id IS NOT NULL
                        THEN b.booking_id END)                   AS with_inter_leg,
    COUNT(DISTINCT CASE WHEN d.booking_id IS NULL
                         AND i.booking_id IS NULL
                        THEN b.booking_id END)                   AS no_leg_recorded
FROM csi_bookings b
JOIN csi_booking_shipper_information s
       ON s.booking_id = b.booking_id
LEFT JOIN csi_booking_domestic_airline d ON d.booking_id = b.booking_id
LEFT JOIN csi_booking_inter_airline    i ON i.booking_id = b.booking_id
WHERE b.hidden = 0
  AND s.shipper_funeral_home_id IN
      (2798, 16315, 2771, 17358, 2996, 2799, 9393, 12568, 3063, 17257, 3104, 2773)
  AND STR_TO_DATE(b.registration_date, '%m/%d/%Y') >= '2026-01-01'
GROUP BY s.shipper_funeral_home_id
ORDER BY bookings_2026 DESC;
