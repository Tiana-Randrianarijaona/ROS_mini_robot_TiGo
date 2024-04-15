#!/usr/bin/env python3
#coding=utf-8

import rospy
from geometry_msgs.msg import Twist

def publish_cmd_vel():
    rospy.init_node('test_publish', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)  # 10Hz
    while not rospy.is_shutdown():
        twist_msg = Twist()
        twist_msg.linear.x = 0.1  # Example linear velocity
        twist_msg.angular.z = 0.1  # Example angular velocity
        pub.publish(twist_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_cmd_vel()
    except rospy.ROSInterruptException:
        pass
