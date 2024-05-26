#!/usr/bin/env python3

import rospy  # import rospy
from geometry_msgs.msg import Twist   # import Twist message
from math import atan2, sqrt  # import the mathematical functions atan2 and sqrt from the python module called math
import sys
from std_msgs.msg import Float32MultiArray, Bool
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
        self.kickerPub = rospy.Publisher('/kicking_decision', Bool, queue_size = 10)
        self.ballSub = rospy.Subscriber('/ball_data', Float32MultiArray, self.ball_callback)     
        self.goalSub = rospy.Subscriber('/goal_data', Float32MultiArray, self.goal_callback)           
        self.vel = Twist()    
        self.kickingDecision = Bool()    
        rate = rospy.Rate(10)        

    def ball_callback(self,msg):  
        self.ballNavigator.pose_callback(msg)
        if self.ballNavigator.hasNotCaughtTheBall:            
            self.pub.publish(self.ballNavigator.vel)
            
        
    def goal_callback(self,msg) :
        if not (self.ballNavigator.hasNotCaughtTheBall):            
            self.goalNavigator.pose_callback(msg)
            self.notifyKickerNode(self.goalNavigator.isReadyToKick)
            print(f"IsReadyToKick = {self.goalNavigator.isReadyToKick}")
            self.pub.publish(self.goalNavigator.vel)

    def notifyKickerNode(self,kickingDecision):
        self.kickingDecision.data = kickingDecision
        self.kickerPub.publish(self.kickingDecision)
if __name__ == '__main__':
    try:
        Navigation()
        rospy.spin()    
    except rospy.ROSInterruptException:
        pass
