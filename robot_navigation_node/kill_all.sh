#!/bin/bash
###
 # @Author: Ceoifung
 # @Date: 2022-06-06 11:20:00
 # @LastEditTime: 2022-06-06 11:22:01
 # @LastEditors: Ceoifung
 # @Description: 
 # XiaoRGEEK All Rights Reserved, Powered by Ceoifung
### 
source /opt/xrapp/script/init_env.sh
#source /home/xrrobot/.bashrc
killall -9 roscore
killall -9 rosmaster
rosnode kill -a
sleep 5
kill -9 `ps -ef| grep noetic | awk '{print $2}'`
kill -9 `ps -ef| grep catkin_ws |awk '{print $2}'`
wait
echo True
exit 0
