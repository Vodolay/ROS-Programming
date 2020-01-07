#!/usr/bin/env python

import sys
from robot_control_class import RobotControl

rc = RobotControl()

dist = rc.get_laser(0)

while dist > 1:
   rc.move_straight()
   dist = rc.get_laser(0)
   print("The distance to a wall is {}".format(dist))

rc.stop_robot()

print("The final distance is {}".format(dist))   


