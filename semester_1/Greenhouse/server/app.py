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

def get_sensor_ids():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT DISTINCT sensor_id FROM sensor_data')
        rows = cursor.fetchall()
        sensor_ids = [row[0] for row in rows]
    return sensor_ids

# Route to serve the main dashboard
@app.route('/')
def index():
    sensord_ids = get_sensor_ids()
    return render_template('index.html', sensor_ids=sensord_ids)

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

@app.route('/sensor/<sensor_id>')
def show_sensor_data(sensor_id):
    # Get sensor-specific data
    sensor_data = get_sensor_data_for_sensor(sensor_id)
    
    # Prepare data for Chart.js (temperature, humidity, light level, and timestamps)
    timestamps = [entry['timestamp'] for entry in sensor_data]
    temperatures = [entry['temperature'] for entry in sensor_data]
    humidities = [entry['humidity'] for entry in sensor_data]
    light_levels = [entry['light_level'] for entry in sensor_data]

    return render_template('sensor_page.html', 
                           sensor_id=sensor_id, 
                           sensor_data=sensor_data,
                           timestamps=timestamps,
                           temperatures=temperatures,
                           humidities=humidities,
                           light_levels=light_levels)

# Function to filter data for a specific sensor
def get_sensor_data_for_sensor(sensor_id):
    # This function would filter your data and return only the entries for this specific sensor
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT sensor_id, timestamp, temperature, humidity, light_level FROM sensor_data WHERE sensor_id=?', (sensor_id,))
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


if __name__ == '__main__':
    app.run(debug=True)