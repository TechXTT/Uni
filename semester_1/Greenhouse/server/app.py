from flask import Flask, render_template, jsonify, request
import sqlite3

app = Flask(__name__)

DATABASE = 'sensor_data.db'

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sensor_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sensor_id TEXT,
                timestamp TEXT,
                temperature REAL,
                humidity REAL,
                light_level REAL
            )
        ''')
        conn.commit()

init_db()

def get_sensor_data():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT sensor_id, timestamp, temperature, humidity, light_level FROM sensor_data')
        rows = cursor.fetchall()
        sensor_data = [
            {
                "sensor_id": row[0],
                "timestamp": row[1],
                "temperature": row[2],
                "humidity": row[3],
                "light_level": row[4]
            }
            for row in rows
        ]
    return sensor_data

def save_sensor_data(data):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO sensor_data (sensor_id, timestamp, temperature, humidity, light_level)
            VALUES (?, ?, ?, ?, ?)
        ''', (data['sensor_id'], data['timestamp'], data['temperature'], data['humidity'], data['light_level']))
        conn.commit()

# Route to serve the main dashboard
@app.route('/')
def index():
    return render_template('index.html')

# API endpoint to get sensor data as JSON
@app.route('/api/sensor_data')
def sensor_data():
    data = get_sensor_data()
    return jsonify(data)

@app.route('/post_data', methods=['POST'])
def post_data():
    data = request.json
    save_sensor_data(data)
    return jsonify({"status": "Data received"}), 200


if __name__ == '__main__':
    app.run(debug=True)