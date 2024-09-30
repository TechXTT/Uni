# Write code to control Rich Shield sensors on the Arduino using Python code on the laptop by defining
# and implementing your own protocol i.e. a set of text messages like: GetTemperature, GetHumidity,
# GetBrightness, SwitchOnHeater (the red LED) and SwitchOffHeater.

import serial

def print_menu():
    print("Welcome to the Rich Shield Sensor Control System!")
    print("Press 'G' to get temperature.")
    print("Press 'H' to get humidity.")
    print("Press 'B' to get brightness.")
    print("Press 'O' to switch on heater.")
    print("Press 'F' to switch off heater.")
    print("Press 'Q' to quit.")

def main():
    ser = serial.Serial('/dev/cu.usbserial-1230', 9600, timeout=1)
    while True:
        print_menu()
        choice = input("Enter choice: ")
        if choice == "G":
            ser.write(b'GetTemperature')
            print(ser.readline().decode().strip())
        elif choice == "H":
            ser.write(b'GetHumidity')
            print(ser.readline().decode().strip())
        elif choice == "B":
            ser.write(b'GetBrightness')
            print(ser.readline().decode().strip())
        elif choice == "O":
            ser.write(b'SwitchOnHeater')
            print(ser.readline().decode().strip())
        elif choice == "F":
            ser.write(b'SwitchOffHeater')
            print(ser.readline().decode().strip())
        elif choice == "Q":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()