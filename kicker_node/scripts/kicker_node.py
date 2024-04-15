import serial
import time

# Set up serial connection
ser = serial.Serial('COM7', 9600)  # Replace '/dev/ttyUSB0' with the appropriate serial port
time.sleep(2)  # Allow some time for the serial connection to initialize

# Send trigger signal
# ser.write(b'T   ')  # Sending 'T' as the trigger signal
string_to_send = "Tigo"
# Send the string
ser.write(string_to_send.encode())
print("Trigger signal sent.")

# Close serial connection
ser.close()
