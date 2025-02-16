import serial
import time
import os
import pandas as pd

# Set your correct serial port
serial_port = "/dev/tty.usbmodem1101"  
baud_rate = 9600  # Match the baud rate in your Arduino code

# Open serial connection
ser = serial.Serial(serial_port, baud_rate, timeout=1)
time.sleep(2)  # Allow time for the connection to establish

# Path to Google Drive (or any location)
file_path = "/Users/abby/Google Drive/My Drive/sensor_data.csv"

# Check if the CSV file exists, if not, create it with headers
if not os.path.exists(file_path):
    df = pd.DataFrame(columns=["timestamp", "value"])
    df.to_csv(file_path, index=False)

# Open the CSV file dynamically for updating
while True:
    try:
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').strip()
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

            # Print to terminal
            print(f"{timestamp}: {data}")

            # Append new data
            df = pd.DataFrame([[timestamp, data]], columns=["timestamp", "value"])
            df.to_csv(file_path, mode="a", header=False, index=False)

            time.sleep(0.1)  # Adjust based on sensor update rate

    except KeyboardInterrupt:
        print("Stopped by user.")
        break
