import serial
import time


class KickerNode():
    def __init__(self):
        self.port = '/dev/ttyUSB0'
        self.string_to_send  = "Tigo"
        # Set up serial connection
        self.ser = serial.Serial('COM7', 9600)  # Replace 'COM7' by '/dev/ttyUSB0' on Ubuntu
        time.sleep(2)  # Allow some time for the serial connection to initialize
    
    def callback(self):
        # Send the string
        self.ser.write(self.string_to_send.encode())
        print("Trigger signal sent.")
        # Close serial connection
        self.ser.close()
