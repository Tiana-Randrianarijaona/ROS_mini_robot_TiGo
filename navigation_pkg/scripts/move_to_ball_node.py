#!/usr/bin/env python3

import rospy  # import rospy
from geometry_msgs.msg import Twist   # import Twist message
from math import atan2, sqrt  # import the mathematical functions atan2 and sqrt from the python module called math
import sys
from std_msgs.msg import Float32MultiArray

class NavigationToBall():
    def __init__(self):
        rospy.init_node('move_to_ball_node', anonymous=False)        
        self.sub = rospy.Subscriber('/ball_data', Float32MultiArray, self.pose_callback)        
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)
        self.vel = Twist()
        self.distance = 0
        rate = rospy.Rate(10)
        self.distanceTreshold = 13.
        self.xTreshold = 3.

    def pose_callback(self,msg):        
        self.distance = msg.data[0]
        self.x = abs(msg.data[2])
        move = ""
        print(f"Distance = {str(self.distance)}, x = {str(self.x)}")        
        if (self.distance == 0.0 and self.x == 0.0) or (self.distance > self.distanceTreshold and self.x > self.xTreshold):        
            self.selfRotate(0.3)
            move = "rotation"
        elif (self.distance <= self.distanceTreshold and self.distance > 0.0) and (self.x < self.xTreshold and self.x > 0.0):
            self.stopRobot()
            move = "stop"
        elif self.distance > self.distanceTreshold and (self.x < self.xTreshold and self.x > 0.0):
            self.moveForward(0.1)
            move = "forward"
        print(f"Distance = {str(self.distance)}, x = {str(self.x)}, move = {move}")   
    
    def selfRotate(self,angularSpeed):
        self.vel.angular.z = angularSpeed
        self.vel.linear.x = 0
        self.pub.publish(self.vel)

    def stopRobot(self):
        self.vel.angular.z = 0
        self.vel.linear.x = 0
        self.pub.publish(self.vel)
    
    def moveForward(self,linearSpeed):
        self.vel.angular.z = 0
        self.vel.linear.x = linearSpeed
        self.pub.publish(self.vel)
if __name__ == '__main__':
    try:
        NavigationToBall()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
