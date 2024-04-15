# encoding:utf-8
import XRMiddleware
import time

xrrobot = XRMiddleware._XRMiddleWare_('/dev/xrbase',115200)
print('driver board start upload data')
xrrobot.Init()
time.sleep(0.5)
while True:
    try:
        print('SetWheelSpeed w1:100,w2:100,w3:100,w4:100,')
        xrrobot.SetWheelSpeed(100, 100, 100,100)
        time.sleep(0.5)
        xrrobot.SetWheelSpeed(100, 100, 100,100)
        time.sleep(0.5)
        xrrobot.SetWheelSpeed(100, 100, 100,100)
        time.sleep(0.5)
        wheelspeed = xrrobot.GetWheelSpeed()
        print(wheelspeed)
        break
        # print('SetWheelSpeed w1:-100,w2:-100,w3:-100,w4:-100,')
        # xrrobot.SetWheelSpeed(-100, -100, -100, -100)
        # time.sleep(0.5)
        # xrrobot.SetWheelSpeed(-100, -100, -100, -100)
        # time.sleep(0.5)
        # xrrobot.SetWheelSpeed(-100, -100, -100, -100)
        # time.sleep(0.5)
        # wheelspeed = xrrobot.GetWheelSpeed()
        # print(wheelspeed)
    except:
        xrrobot.Deinit()
        xrrobot.release()
        time.sleep(1)
        print("abnormal,release port")