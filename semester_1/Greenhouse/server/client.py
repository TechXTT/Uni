# client.py
import requests
import serial
import datetime
import time
import json

# Change COM port and baudrate as per your Arduino connection
ser = serial.Serial('/dev/cu.usbserial-110', 9600, timeout=1)

def get_sensor_data():
    
    # If using actual Arduino, uncomment the serial part
    ser.write(b'GetSensorData')
    data = ser.readline().decode().strip()
    # data is in the format: {"sensor_id": "1", "temperature": 23, "humidity": 45, "light_level": 512} 
    
    data = json.loads(data)
    data['timestamp'] = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    return data

def post_data_to_server(data):
    url = "http://127.0.0.1:5000/post_data"  # Flask server URL
    response = requests.post(url, json=data, timeout=5)
    print(response.json())

if __name__ == '__main__':
    while True:
        sensor_data = get_sensor_data()
        post_data_to_server(sensor_data)
        time.sleep(10)  # Delay for 60 seconds