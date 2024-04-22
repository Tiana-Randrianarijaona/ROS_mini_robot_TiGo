#!/usr/bin/env python
import serial
import time
import rospy
from std_msgs.msg import Float32MultiArray

class KickerNode():
    def __init__(self,topicToSubscribe = '/kicker_trigger'):
        self.ArduinoPort = '/dev/ttyUSB0'
        self.string_to_send  = "Tigo"     
        # Set up serial connection
        self.ser = serial.Serial(self.ArduinoPort, 9600)  # Replace 'COM7' by '/dev/ttyUSB0' on Ubuntu   
        time.sleep(2)  # Allow some time for the serial connection to initialize
        rospy.init_node('image_subscriber')        
        self.topicToSubscribe = topicToSubscribe
        self.subscriber = rospy.Subscriber(self.topicToSubscribe, Float32MultiArray, self.callback)
    
    def callback(self,msg):    
        print(f"Just received the msg {msg.data}")        
        # Send the string
        self.ser.write(self.string_to_send.encode())
        print("Trigger signal sent.")        

    def shutDown(self):
        # Close serial connection
        self.ser.close()

if __name__ == '__main__':    
    try:
        kickerNode = KickerNode() 
        rospy.spin()
    except:
        pass
    finally:
        kickerNode.shutDown()
