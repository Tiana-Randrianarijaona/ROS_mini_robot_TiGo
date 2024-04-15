#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np

bridge = CvBridge()

def image_callback(mdg):
    cv2_img = bridge.imgmsg_to_cv2(mdg, "bgr8")
    frame = np.array(cv2_img, dtype=np.uint8)
    color_image = color_detection(frame)    
    cv2.waitKey(3)

def edges_detection(frame):
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.blur(grey, (7,7))
    edges = cv2.Canny(blurred, 15.0, 30.0)
    # cv2.imshow("color", edges)
    return edges

def color_detection(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # blue_lower = np.array([90,50,50], np.uint8)
    # blue_upper = np.array([120,255,255], np.uint8)
    # lower_red = np.array([0,50,50], np.uint8)
    # upper_red = np.array([10,255,255], np.uint8)
    # lower_yellow = np.array([22, 93, 0])
    # upper_yellow = np.array([45, 255, 255])
    lower_yellow = np.array([22, 100, 0])
    upper_yellow = np.array([45, 255, 255])
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    cv2.imshow("image mask", mask)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("color", res)
    edge = edges_detection(res)
    cv2.imshow("edge", edge)
    return res

def simple_image_processing():
    rospy.init_node('image_subscriber')
    image_topic = "/image_raw"
    rospy.Subscriber(image_topic, Image, image_callback)
    rospy.spin()

if __name__ == '__main__':
    simple_image_processing()  