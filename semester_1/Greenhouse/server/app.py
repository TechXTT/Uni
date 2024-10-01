from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

DATABASE = 'sensor_data.db'

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

# Route to serve the main dashboard
@app.route('/')
def index():
    return render_template('index.html')

# API endpoint to get sensor data as JSON
@app.route('/api/sensor_data')
def sensor_data():
    data = get_sensor_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)