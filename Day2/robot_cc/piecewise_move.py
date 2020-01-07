#!/usr/bin/env python

import time
from robot_control_class import RobotControl

rc = RobotControl()

def move_straight_x(secs):
   rc.move_straight()
   time.sleep(secs)
   rc.stop_robot()

def turn_x(secs):
   rc.cmd.angular.z = 1
   rc.publish_once_in_cmd_vel()
   time.sleep(secs)
   rc.stop_robot()

move_straight_x(3)
turn_x(1)
move_straight_x(2)
turn_x(6)
move_straight_x(6)
