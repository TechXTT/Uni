#include <DHT.h>

// # Write code to control Rich Shield sensors on the Arduino using Python code on the laptop by defining
// # and implementing your own protocol i.e. a set of text messages like: GetTemperature, GetHumidity,
// # GetBrightness, SwitchOnHeater (the red LED) and SwitchOffHeater.

// import serial

// def print_menu():
//     print("Welcome to the Rich Shield Sensor Control System!")
//     print("Press 'G' to get temperature.")
//     print("Press 'H' to get humidity.")
//     print("Press 'B' to get brightness.")
//     print("Press 'O' to switch on heater.")
//     print("Press 'F' to switch off heater.")
//     print("Press 'Q' to quit.")

// def main():
//     ser = serial.Serial('/dev/cu.usbserial-1230', 9600, timeout=1)
//     while True:
//         print_menu()
//         choice = input("Enter choice: ")
//         if choice == "G":
//             ser.write(b'GetTemperature')
//             print(ser.readline().decode().strip())
//         elif choice == "H":
//             ser.write(b'GetHumidity')
//             print(ser.readline().decode().strip())
//         elif choice == "B":
//             ser.write(b'GetBrightness')
//             print(ser.readline().decode().strip())
//         elif choice == "O":
//             ser.write(b'SwitchOnHeater')
//             print(ser.readline().decode().strip())
//         elif choice == "F":
//             ser.write(b'SwitchOffHeater')
//             print(ser.readline().decode().strip())
//         elif choice == "Q":
//             break
//         else:
//             print("Invalid choice. Please try again.")

// if __name__ == "__main__":
//     main()

// LED1 (yellow): D7
// LED2 (blue): D6
// LED3 (green): D5
// LED4 (red): D4
// Buzzer: D3
// LDR (light sensor): A2
// TM1637 Segment display with 4 characters and decimal points: D10 (CLK from TM1637), D11 (DIN  from TM1637)
// Two push buttons: K1 on D9, K2 on D8
// NTC (temperature sensor): A1
// Potentiometer: A0
// Voltage sensor (voltage divider): A3
// DHT11 Sensor: D12
// IR receiver: D2
// 24C02 EEPROM: I2C pins (standard SCK and SDA pins)

int led1 = 7;
int led2 = 6;
int led3 = 5;
int led4 = 4;

int buzzer = 3;
int ldr = A2;
int tm1637_clk = 10;
int tm1637_din = 11;
int button1 = 9;
int button2 = 8;
int ntc = A1;
int pot = A0;
int voltage = A3;
int dht11 = 12;
int ir = 2;

#include <TM1637Display.h>
#include <Wire.h>
#include <EEPROM.h>

#define DHTTYPE DHT11 // DHT 11
DHT dht(dht11, DHTTYPE);


TM1637Display display(tm1637_clk, tm1637_din);

void setup() {
  Serial.begin(9600);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  pinMode(buzzer, OUTPUT);
  pinMode(button1, INPUT);
  pinMode(button2, INPUT);
  pinMode(ir, INPUT);
  dht.begin();
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readString();
    if (command == "GetTemperature") {
      Serial.println(getTemperature());
    } else if (command == "GetHumidity") {
      Serial.println(getHumidity());
    } else if (command == "GetBrightness") {
      Serial.println(getBrightness());
    } else if (command == "SwitchOnHeater") {
      switchOnHeater();
      Serial.println("Heater switched on.");
    } else if (command == "SwitchOffHeater") {
      switchOffHeater();
      Serial.println("Heater switched off.");
    } else {
      Serial.println("Invalid command.");
    }
  }
}

float getTemperature() {
  return dht.readTemperature();
}

float getHumidity() {
  return dht.readHumidity();
}

int getBrightness() {
  return analogRead(ldr);
}

void switchOnHeater() {
  digitalWrite(led4, HIGH);
}

void switchOffHeater() {
  digitalWrite(led4, LOW);
}