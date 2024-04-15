# encoding:utf-8
import XRMiddleware
import time
xrrobot = XRMiddleware._XRMiddleWare_('/dev/xrbase',115200,db = 0)
print('driver board start upload data')
xrrobot.Init()
time.sleep(0.5)
time_count = 0
while(time_count < 20): # Each loop delayed 0.05s, loop 40times, that is run 2s
    xrrobot.SetVelocity(0.5,0.5,2) # Call the speed setting interface to directly control the chassis three-axis speed. Namely (X axis velocity (m/s), Y axis velocity (m/s), Yaw axis angular velocity (rad/s))
    time_count = time_count+1 # Running at 0.5m/s for 2s, the robot moves about 1m
    time.sleep(0.05)
xrrobot.SetVelocity(0,0,0) # Set the three-axis speed of the robot to 0 and stop the robot
time.sleep(1)
xrrobot.Deinit()
xrrobot.release()
time.sleep(1)
pass