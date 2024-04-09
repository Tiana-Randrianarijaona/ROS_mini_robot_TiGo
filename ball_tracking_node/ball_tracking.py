# USAGE
# python ball_tracking.py --video ball_tracking_example.mp4
# python ball_tracking.py

# import the necessary packages
from collections import deque
from imutils.video import VideoStream
import numpy as np
import cv2
import imutils
import time
from TrackerHelper import TrackerHelper

class Tracker():
	def __init__(self,
			  trackerHelper = TrackerHelper(real_ball_radius=5., focal_length=277.),
			  yellowLower = (20, 100, 100),
			  yellowUpper = (30, 255, 255)):		
		# trackerHelper = TrackerHelper(real_ball_radius=5., focal_length=277.)
		self.trackerHelper = trackerHelper

		# define the lower and upper boundaries of the "green"
		# ball in the HSV color space, then initialize the
		# list of tracked points
		# greenLower = (29, 86, 6)
		# greenUpper = (64, 255, 255)
		self.yellowLower = yellowLower
		self.yellowUpper = yellowUpper
		self.buffer = 64
		self.pts = deque(maxlen=self.buffer)


		# allow the camera or video file to warm up
		time.sleep(2.0)

	def callBack(self, frame_from_image_topic):

		# grab the current frame
		frame = frame_from_image_topic

		# resize the frame, blur it, and convert it to the HSV
		# color space
		frame = imutils.resize(frame, width=600)
		blurred = cv2.GaussianBlur(frame, (11, 11), 0)
		hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

		# construct a mask for the color "green", then perform
		# a series of dilations and erosions to remove any small
		# blobs left in the mask
		mask = cv2.inRange(hsv, self.yellowLower, self.yellowUpper)
		mask = cv2.erode(mask, None, iterations=2)
		mask = cv2.dilate(mask, None, iterations=2)

		# find contours in the mask and initialize the current
		# (x, y) center of the ball
		cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
			cv2.CHAIN_APPROX_SIMPLE)
		cnts = imutils.grab_contours(cnts)
		center = None

		# only proceed if at least one contour was found
		if len(cnts) > 0:
			# find the largest contour in the mask, then use
			# it to compute the minimum enclosing circle and
			# centroid
			c = max(cnts, key=cv2.contourArea)
			((x, y), radius) = cv2.minEnclosingCircle(c)
			M = cv2.moments(c)
			center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

			# only proceed if the radius meets a minimum size
			if radius > 10:
				# draw the circle and centroid on the frame,
				# then update the list of tracked points
				cv2.circle(frame, (int(x), int(y)), int(radius),
					(0, 255, 255), 2)
				cv2.circle(frame, center, 5, (0, 0, 255), -1)
			# trackerHelper.setFocalLength(30.,radius)
			# print(f"focal_length = {trackerHelper.focal_length}")
			# distance = trackerHelper.getDistance(radius)
			print(f"(x,y) = ({x},{y})")
			# trackerHelper.getCoordinates(radius,x)
			# print(f"Distance = {distance}")

		# update the points queue
		self.pts.appendleft(center)

		# loop over the set of tracked points
		for i in range(1, len(self.pts)):
			# if either of the tracked points are None, ignore
			# them
			if self.pts[i - 1] is None or self.pts[i] is None:
				continue

			# otherwise, compute the thickness of the line and
			# draw the connecting lines
			thickness = int(np.sqrt(self.buffer / float(i + 1)) * 2.5)
			cv2.line(frame, self.pts[i - 1], self.pts[i], (0, 0, 255), thickness)

		# show the frame to our screen
		cv2.imshow("Ball detection", frame)
		key = cv2.waitKey(1) & 0xFF
