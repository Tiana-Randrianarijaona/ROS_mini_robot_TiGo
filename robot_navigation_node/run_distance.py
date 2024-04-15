# encoding:utf-8
import XRMiddleware
import time
xrrobot = XRMiddleware._XRMiddleWare_('/dev/xrbase',115200,db = 0)
print('driver board start upload data')
xrrobot.Init()
time.sleep(0.5)
print('clear odom ')#Clear the odometer
xrrobot.ClrOdom()
time.sleep(0.5)
#TO DO : this script moves the robot to a specific direction. Problem: When distance reached, it disengaged the previous speed and starts to move slowly. It does not stop once the position is reached
step_group = list() # Motion step List
step_group.append([0.5 ,0 , 3]) # Add a movement step to move 1m in the positive direction of X axis and 1m in the positive Y direction at the same time
# step_group.append([1.0 ,1.0 , 0]) # Add a movement step to move 1m in the positive direction of X axis and 1m in the positive Y direction at the same time
# step_group.append([-1.0 , 0 , 0]) # Add a motion step to move 1m in the negative direction of X axis
# step_group.append([1.0 ,-1.0 , 0]) # Add a movement step to move 1m in the positive direction of X axis and 1m in the negative direction of Y axis at the same time
# step_group.append([-1.0 , 0 , 0]) # 1mAdd a motion step to move 1m in the negative direction of X axis

linear_tolerance = 0.1 # Allowable error of motion line mileage
angular_tolerance = 0.2 # Allowable error of motion angle
linear_speed = 0.3 # Linear velocity of motion
angular_speed = 1.0 # Angular velocity of motion
x_speed = 0.0
y_speed = 0.0
yaw_speed = 0.0
odom = xrrobot.GetOdom()

for current_step in step_group: # Control the robot to perform the motion steps step by step
    print("Current Step: ",current_step)
    current_goal_x = odom[0]+current_step[0]
    current_goal_y = odom[1]+current_step[1]
    current_goal_yaw = odom[2]+current_step[2]

    while True:
        x_speed = ((current_goal_x - odom[0])>0 and 1 or -1)*((abs(current_goal_x - odom[0]) > linear_tolerance) and linear_speed or 0)
        #Through the odometer to realize the closed-loop control of the motion mileage
        y_speed = ((current_goal_y - odom[1])>0 and 1 or -1)*((abs(current_goal_y - odom[1]) > linear_tolerance) and linear_speed or 0)
        yaw_speed = ((current_goal_yaw - odom[2])>0 and 1 or -1)*((abs(current_goal_yaw - odom[2]) > angular_tolerance) and angular_speed or 0)
        xrrobot.SetVelocity(x_speed,y_speed,yaw_speed)
        odom = xrrobot.GetOdom()
        time.sleep(0.04)
        if((x_speed == 0) and (y_speed == 0) and (yaw_speed == 0)):
            xrrobot.SetVelocity(0,0,0)
            time.sleep(1)
            break

print("All Step Reached!")
xrrobot.Deinit()
xrrobot.release()
time.sleep(1)
pass