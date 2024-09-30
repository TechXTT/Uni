import matplotlib.pyplot as plt

# Sample data
days = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7']
sensor1_temp = [22.5, 23.0, 21.8, 22.1, 23.2, 22.9, 22.7]
sensor1_humidity = [60, 62, 61, 63, 64, 65, 64]

sensor2_temp = [21.2, 21.5, 21.0, 21.8, 22.0, 21.6, 21.7]
sensor2_humidity = [58, 60, 59, 61, 62, 63, 60]

# Plot Temperature for both sensors
plt.figure(figsize=(10,5))
plt.plot(days, sensor1_temp, label='Sensor 1 Temperature', color='r')
plt.plot(days, sensor2_temp, label='Sensor 2 Temperature', color='b')
plt.xlabel('Days')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Over One Week')
plt.legend()
plt.show()

# Plot Humidity for both sensors
plt.figure(figsize=(10,5))
plt.plot(days, sensor1_humidity, label='Sensor 1 Humidity', color='g')
plt.plot(days, sensor2_humidity, label='Sensor 2 Humidity', color='c')
plt.xlabel('Days')
plt.ylabel('Humidity (%)')
plt.title('Humidity Over One Week')
plt.legend()
plt.show()