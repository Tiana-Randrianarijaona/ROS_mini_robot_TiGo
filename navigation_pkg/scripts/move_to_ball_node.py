#!/usr/bin/env python3

import rospy  # import rospy
from turtlesim.msg import Pose   # import Pose message 
from geometry_msgs.msg import Twist   # import Twist message
from math import atan2, sqrt  # import the mathematical functions atan2 and sqrt from the python module called math
import sys
from std_msgs.msg import Float32MultiArray

global pub
def pose_callback(msg):
    global pub
    distance = msg.data[0]
    print(f"Distance = {str(distance)}")
    vel = Twist()
    if distance == 0.:        
        vel.angular.z = 1.0 
        pub.publish(vel)
    # elif case_number == 2:
    #     print("Case 2")
    # elif case_number == 3:
    #     print("Case 3")

def move_to_ball_node():
    global pub
    # Initialise the node
    rospy.init_node('move_to_ball_node', anonymous=False)

    # Create a subscriber to the raw_odom topic    
    sub = rospy.Subscriber('/ball_data', Float32MultiArray, pose_callback)

    # Create a publisher to the robot's velocity command
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)
    rate = rospy.Rate(10)
    rospy.spin()
    # rate = rospy.Rate(10) # 10hz
 
    # vel = Twist() # creates a Twist object named vel
    
if __name__ == '__main__':
    try:
        move_to_ball_node()

    except rospy.ROSInterruptException:
        pass
