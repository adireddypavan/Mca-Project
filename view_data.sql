-- View all bookings with formatted output
SELECT * FROM bookings;

-- View with count
SELECT 
    id,
    service,
    name,
    mobile,
    issue,
    address,
    created_at
FROM bookings
ORDER BY created_at DESC;

-- Summary statistics
SELECT 
    COUNT(*) as total_bookings,
    COUNT(DISTINCT service) as unique_services,
    MIN(created_at) as first_booking,
    MAX(created_at) as last_booking
FROM bookings;

-- Bookings grouped by service
SELECT 
    service,
    COUNT(*) as count
FROM bookings
GROUP BY service
ORDER BY count DESC;
