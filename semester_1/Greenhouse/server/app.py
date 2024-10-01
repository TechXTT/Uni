from flask import Flask, render_template, request, jsonify, url_for
import os
import random
import datetime
import sqlite3
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

app = Flask(__name__)

# Directory to save plots
PLOT_DIR = 'static/plots'

# Ensure the plot directory exists
os.makedirs(PLOT_DIR, exist_ok=True)

# Initialize the database
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

# Home route to display sensor data and the graphs
@app.route('/')
def index():
    sensor_data = get_sensor_data()
    # Get a list of unique sensor IDs
    sensor_ids = list(set([data['sensor_id'] for data in sensor_data]))
    plot_urls = [url_for('static', filename=f'plots/sensor_{sensor_id}_plot.png') for sensor_id in sensor_ids]
    plot_list = list(zip(sensor_ids, plot_urls))
    return render_template('index.html', sensor_data=sensor_data, plot_urls=plot_list)

@app.route('/sensor')
def sensor():
    sensor_id = request.args.get('id')
    sensor_data = get_sensor_data()
    sensor_specific_data = [data for data in sensor_data if data['sensor_id'] == sensor_id]
    plot_url = url_for('static', filename=f'plots/sensor_{sensor_id}_plot.png')
    return render_template('sensor.html', sensor_id=sensor_id, sensor_data=sensor_specific_data, plot_url=plot_url)

# Route to handle sensor data sent via POST
@app.route('/post_data', methods=['POST'])
def post_data():
    data = request.json
    save_sensor_data(data)
    create_sensor_plots()  # Create separate plots for each sensor
    return jsonify({"status": "Data received"}), 200

# Simulate random sensor data
@app.route('/generate_fake_data')
def generate_fake_data():
    now = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    data = {
        "sensor_id": str(random.randint(1, 3)),  # Random sensor ID between 1 and 3
        "timestamp": now,
        "temperature": round(random.uniform(15, 40), 2),
        "humidity": round(random.uniform(0, 100), 2),
        "light_level": round(random.uniform(0, 1000), 2)
    }
    save_sensor_data(data)
    create_sensor_plots()
    return jsonify(data)

# Function to save sensor data to the database
def save_sensor_data(data):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO sensor_data (sensor_id, timestamp, temperature, humidity, light_level)
            VALUES (?, ?, ?, ?, ?)
        ''', (data['sensor_id'], data['timestamp'], data['temperature'], data['humidity'], data['light_level']))
        conn.commit()

# Function to get sensor data from the database
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

# Function to create plots for each sensor
def create_sensor_plots():
    sensor_data = get_sensor_data()
    if not sensor_data:
        return
    
    # Get a list of unique sensor IDs
    sensor_ids = list(set([data['sensor_id'] for data in sensor_data]))
    
    for sensor_id in sensor_ids:
        # Filter data for each sensor
        sensor_specific_data = [data for data in sensor_data if data['sensor_id'] == sensor_id]
        
        # Extract data for plotting
        timestamps = [data['timestamp'] for data in sensor_specific_data]
        temperatures = [float(data['temperature']) for data in sensor_specific_data]
        humidities = [float(data['humidity']) for data in sensor_specific_data]
        light_levels = [float(data['light_level']) for data in sensor_specific_data]

        plt.figure(figsize=(10, 6))
        
        # Plot temperature, humidity, and light level over time for this sensor
        plt.plot(timestamps, temperatures, label='Temperature (℃)', color='r', marker='o')
        plt.plot(timestamps, humidities, label='Humidity (%)', color='b', marker='x')
        plt.plot(timestamps, light_levels, label='Light Level (W/m²)', color='g', marker='s')

        # Formatting the plot
        plt.xlabel('Timestamp')
        plt.xticks(rotation=45, ha="right")  # Rotate x-axis labels
        plt.ylabel('Value')
        plt.title(f'Sensor {sensor_id} Data Over Time')
        plt.legend(loc='upper left')
        plt.tight_layout()

        # Save the plot with a unique filename for this sensor
        plot_filename = f'sensor_{sensor_id}_plot.png'
        plt.savefig(os.path.join(PLOT_DIR, plot_filename))
        plt.close()

if __name__ == '__main__':
    app.run(debug=True)