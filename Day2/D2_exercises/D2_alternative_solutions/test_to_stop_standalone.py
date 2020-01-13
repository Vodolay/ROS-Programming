#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

# Move the robot forward with LIN_SPEED and print minimum of laser distances
# When the laser returns a minimum distance less than STOP_DIST, stop the robot

LIN_SPEED = 0.2
STOP_DIST = 0.3

def laser_callback(msg):
    global stopping, is_stopped
    laser_ranges = msg.ranges
    min_dist = min(laser_ranges)
    min_dir = laser_ranges.index(min_dist)
    if stopping:
        print("Final distance: {:.3f} in direction {}".format(min_dist, min_dir))
        is_stopped = True
        return
    print("Minimum distance: {:.3f} in direction {}".format(min_dist, min_dir))
    if min_dist < STOP_DIST:
        print("Stopping")
        pub.publish(stop)
        stopping = True

# workaround to "establish connection"
# see https://answers.ros.org/question/9665/test-for-when-a-rospy-publisher-become-available/
# not ideal though: may not work if "rostopic echo /cmd_vel" is running along with gazebo / the real robot
rospy.init_node('move_TB3')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
while (not rospy.is_shutdown()) and (pub.get_num_connections() < 1):
    pass

go = Twist()
go.linear.x = LIN_SPEED
pub.publish(go)

stopping = False
is_stopped = False

stop = Twist()

laser_subscriber = rospy.Subscriber('/scan', LaserScan, laser_callback)

while (not rospy.is_shutdown()) and (not is_stopped):
    pass

