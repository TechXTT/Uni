from flask import Flask, render_template, request, jsonify, url_for
import os
import random
import datetime
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

app = Flask(__name__)

# Directory to save plots
PLOT_DIR = 'static/plots'

# Ensure the plot directory exists
os.makedirs(PLOT_DIR, exist_ok=True)

# Store sensor data
sensor_data = []

# Home route to display sensor data and the graph
@app.route('/')
def index():
    plot_url = url_for('static', filename='plots/sensor_plot.png')
    return render_template('index.html', sensor_data=sensor_data, plot_url=plot_url)

# Route to handle sensor data sent via POST
@app.route('/post_data', methods=['POST'])
def post_data():
    data = request.json
    sensor_data.append(data)
    # Create a new graph after each data update
    create_sensor_plot()
    return jsonify({"status": "Data received"}), 200

# Simulate random sensor data
@app.route('/generate_fake_data')
def generate_fake_data():
    now = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    data = {
        "sensor_id": "1",
        "timestamp": now,
        "temperature": round(random.uniform(15, 40), 2),
        "humidity": round(random.uniform(0, 100), 2),
        "light_level": round(random.uniform(0, 1000), 2)
    }
    sensor_data.append(data)
    create_sensor_plot()
    return jsonify(data)

# Function to create sensor plot
def create_sensor_plot():
    if not sensor_data:
        return
    
    # Extract data for plotting
    timestamps = [data['timestamp'] for data in sensor_data]
    temperatures = [float(data['temperature']) for data in sensor_data]
    humidities = [float(data['humidity']) for data in sensor_data]
    light_levels = [float(data['light_level']) for data in sensor_data]

    plt.figure(figsize=(10, 6))
    
    # Plot temperature, humidity, and light level over time
    plt.plot(timestamps, temperatures, label='Temperature (℃)', color='r', marker='o')
    plt.plot(timestamps, humidities, label='Humidity (%)', color='b', marker='x')
    plt.plot(timestamps, light_levels, label='Light Level (W/m²)', color='g', marker='s')

    # Formatting the plot
    plt.xlabel('Timestamp')
    plt.xticks(rotation=45, ha="right")  # Rotate x-axis labels
    plt.ylabel('Value')
    plt.title('Greenhouse Sensor Data Over Time')
    plt.legend(loc='upper left')
    plt.tight_layout()
    
    # Save the plot
    plt.savefig(os.path.join(PLOT_DIR, 'sensor_plot.png'))
    plt.close()

if __name__ == '__main__':
    app.run(debug=True)