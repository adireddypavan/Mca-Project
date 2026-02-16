-- ✅ Create Database
CREATE DATABASE IF NOT EXISTS bookings_db;

-- ✅ Use the Database
USE bookings_db;

-- ✅ Create Table
CREATE TABLE IF NOT EXISTS bookings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    service VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    mobile VARCHAR(15) NOT NULL,
    issue TEXT NOT NULL,
    address TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ✅ Insert Sample Data (Optional)
INSERT INTO bookings (service, name, mobile, issue, address)
VALUES (
    'AC Repair',
    'Pavan',
    '8500152121',
    'AC not cooling',
    'Kadapa, Andhra Pradesh'
);

-- ✅ View All Data
SELECT * FROM bookings;

-- ✅ Additional Useful Queries:

-- View table structure
DESCRIBE bookings;

-- Count total bookings
SELECT COUNT(*) AS total_bookings FROM bookings;

-- View bookings by service type
SELECT service, COUNT(*) AS count FROM bookings GROUP BY service;

-- View recent bookings (last 10)
SELECT * FROM bookings ORDER BY created_at DESC LIMIT 10;

-- Delete all data (be careful with this!)
-- DELETE FROM bookings;

-- Drop table (be careful with this!)
-- DROP TABLE bookings;

-- Drop database (be careful with this!)
-- DROP DATABASE bookings_db;
