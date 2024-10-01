import requests
import serial
import datetime
import time
import json

# Configure the serial connection (adjust COM port if needed)
ser = serial.Serial('/dev/cu.usbserial-1230', 9600, timeout=1)

def get_sensor_data():
    ser.flushInput()  # Clear the serial input buffer
    ser.write(b'GetSensorData')  # Send command to Arduino
    time.sleep(1)  # Give Arduino time to respond

    data = ser.readline().decode().strip()  # Read the data
    if data:
        print("Raw data from Arduino:", data)
        try:
            # Attempt to load the data as JSON
            json_data = json.loads(data)
            json_data['timestamp'] = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
            return json_data
        except json.JSONDecodeError:
            print("Error decoding JSON:", data)
            return None
    else:
        print("No data received from Arduino.")
        return None

def post_data_to_server(data):
    url = "http://127.0.0.1:5000/post_data"  # Flask server URL
    try:
        response = requests.post(url, json=data, timeout=5)
        print("Server response:", response.json())
    except requests.RequestException as e:
        print("Error posting data to server:", e)

if __name__ == '__main__':
    while True:
        sensor_data = get_sensor_data()
        if sensor_data:
            print("Sensor Data:", sensor_data)
            post_data_to_server(sensor_data)
        time.sleep(30)  # Delay for 10 seconds