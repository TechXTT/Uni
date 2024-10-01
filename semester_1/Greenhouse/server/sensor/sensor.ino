#include <DHT11.h>

// LDR sensor connected to an analog pin
int LDRPin = A2;  // Pin where the LDR is connected
int SensorId = 2;

void setup() {
  Serial.begin(9600);  // Start serial communication at 9600 baud
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readString();
    
    if (command == "GetSensorData") {
      getSensorData();
    } else {
      Serial.println("{\"sensor_id\": " + String(SensorId) + ", \"error\": \"Invalid command. "+ command + "\"}");
    }
  }
}

void getSensorData() {
  
  // Read temperature and humidity from DHT11 sensor
  float temperature = DHT11.getTemperature(); // Celsius by default
  float humidity = DHT11.getHumidity();

  // Read light intensity from the LDR (0-1023)
  int lightLevel = analogRead(LDRPin);

  // Check if the readings are valid
  if (isnan(temperature) || isnan(humidity)) {
    Serial.println("{\"sensor_id\": " + String(SensorId) + ", \"error\": \"Failed to read from DHT sensor.\"}");
  } else {
    Serial.println("{\"sensor_id\": " + String(SensorId) + ", \"temperature\": " + String(temperature) + ", \"humidity\": " + String(humidity) + ", \"light_level\": " + String(lightLevel) + "}");
  }
}