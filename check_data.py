import mysql.connector

# Connect to database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Apavan@145',
    database='bookings_db'
)

cursor = conn.cursor()

# Get all bookings
cursor.execute('SELECT * FROM bookings')
bookings = cursor.fetchall()

# Get column names
column_names = [desc[0] for desc in cursor.description]

print("=" * 100)
print(f"{'ID':<5} {'Service':<15} {'Name':<15} {'Mobile':<12} {'Issue':<20} {'Address':<30}")
print("=" * 100)

if bookings:
    for booking in bookings:
        print(f"{booking[0]:<5} {booking[1]:<15} {booking[2]:<15} {booking[3]:<12} {booking[4]:<20} {booking[5]:<30}")
    print("\n✅ Total bookings:", len(bookings))
else:
    print("❌ No bookings found!")

cursor.close()
conn.close()
