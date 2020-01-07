#!/usr/bin/env python

import sys
from robot_control_class import RobotControl

rc = RobotControl()

if str(sys.argv[1]) == 'full':
   a = rc.get_laser_full()
   print("All 360 values: {}".format(a))

elif str(sys.argv[1]) == 'single':
   ray_n = int(sys.argv[2])
   if ray_n >= 0 and ray_n < 360:
      a = rc.get_laser(ray_n)
      print("The distance along ray {} is {}".format(ray_n, a))
   else:
      print("Invalid ray number")

elif str(sys.argv[1]) == 'four_dirs':
   front = rc.get_laser(0)
   right = rc.get_laser(89)
   back = rc.get_laser(179)
   left = rc.get_laser(359)
   print("The distances are: front - {}, right - {}, back - {}, left - {}".format(front, right, back, left))

else:
   print("VERBOTEN first command line argument")   


