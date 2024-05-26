#!/usr/bin/env python
import requests
import time
import rospy
from std_msgs.msg import Float32MultiArray, Bool

class KickerNode():
    def __init__(self,topicToSubscribe = '/kicking_decision'):
        self.Esp32Ip = '10.5.5.117'      
        self.url = f"http://{self.Esp32Ip}/trigger"     
        time.sleep(2)  # Allow some time for the serial connection to initialize
        rospy.init_node('image_subscriber')        
        self.topicToSubscribe = topicToSubscribe
        self.subscriber = rospy.Subscriber(self.topicToSubscribe, Bool, self.callback)
    
    def callback(self,msg):    
        # print(f"Just received the msg {msg.data}") 
        if(msg.data):
            print("KICKER ON")
        else:
            print("WAITING TO KICK")        

        # Send the string
        # response = requests.get(self.url)
        # print(response.text)
        # print("Trigger signal sent.")        



if __name__ == '__main__':    
    try:
        kickerNode = KickerNode() 
        rospy.spin()
    except:
        pass
