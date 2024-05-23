#!/usr/bin/env python3

import rospy  # import rospy
from geometry_msgs.msg import Twist   # import Twist message
from math import atan2, sqrt  # import the mathematical functions atan2 and sqrt from the python module called math
import sys
from std_msgs.msg import Float32MultiArray
import sys
import os
# sys.path.append(os.path.abspath("../include"))
from include.BallNavigation import BallNavigation
from include.GoalNavigation import GoalNavigation

class Navigation():
    def __init__(self):
        rospy.init_node('navigation_node', anonymous=False)        
        self.ballNavigator = BallNavigation()
        self.goalNavigator = GoalNavigation()
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)
        self.ballSub = rospy.Subscriber('/ball_data', Float32MultiArray, self.ball_callback)     
        self.goalSub = rospy.Subscriber('/goal_data', Float32MultiArray, self.goal_callback)           
        self.vel = Twist()        
        rate = rospy.Rate(10)        

    def ball_callback(self,msg):  
        self.ballNavigator.pose_callback(msg)
        if self.ballNavigator.hasNotCaughtTheBall:            
            self.pub.publish(self.ballNavigator.vel)
        
    def goal_callback(self,msg) :
        if not (self.ballNavigator.hasNotCaughtTheBall):            
            self.goalNavigator.pose_callback(msg)
            self.pub.publish(self.goalNavigator.vel)
if __name__ == '__main__':
    try:
        Navigation()
        rospy.spin()    
    except rospy.ROSInterruptException:
        pass
