from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import mysql.connector
import datetime
import re

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def create_database():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Apavan@145'
    )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS bookings_db")
    conn.commit()
    cursor.close()
    conn.close()

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Apavan@145',
        database='bookings_db'
    )

def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS bookings (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        service VARCHAR(255) NOT NULL,
                        name VARCHAR(255) NOT NULL,
                        mobile VARCHAR(15) NOT NULL,
                        issue TEXT NOT NULL,
                        address TEXT NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )''')
    conn.commit()
    cursor.close()
    conn.close()

create_database()  # Create database first
create_table()  # Create table on startup

@app.route('/')
def index():
    return send_file('auth.html')


@app.route('/home')
def home():
    return send_file('index.html')


@app.route('/auth')
def auth_page():
    return send_file('auth.html')

@app.route('/book-service', methods=['POST'])
def book_service():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    service = data.get('service')
    name = data.get('name')
    mobile = data.get('mobile')
    issue = data.get('issue')
    address = data.get('address')

    if not all([service, name, mobile, issue, address]):
        return jsonify({'error': 'All fields are required'}), 400

    if not re.match(r'^[6-9]\d{9}$', mobile):
        return jsonify({'error': 'Invalid mobile number. Must be 10 digits starting with 6-9'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO bookings (service, name, mobile, issue, address) VALUES (%s, %s, %s, %s, %s)',
                   (service, name, mobile, issue, address))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Booking successful'}), 201

@app.route('/bookings', methods=['GET'])
def get_bookings():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM bookings')
    bookings = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(bookings)

if __name__ == '__main__':
    app.run(debug=True)