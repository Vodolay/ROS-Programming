#!/usr/bin/env python

import sys
from robot_control_class import RobotControl

rc = RobotControl()

all_dist = rc.get_laser_full()
min_dist = min(all_dist)

while min_dist > 0.3:
   rc.move_straight()
   all_dist = rc.get_laser_full()
   min_dist = min(all_dist)
   print("The minimal distance to an object is {}".format(min_dist))

rc.stop_robot()

print("The final minimal distance is {}".format(min_dist))   


