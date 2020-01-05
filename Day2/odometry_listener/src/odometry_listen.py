#! /usr/bin/env python

import rospy
from nav_msgs.msg import Odometry

def writer(msg):
   print(msg.pose)

rospy.init_node('odom_listen')
sub = rospy.Subscriber('/odom', Odometry, writer)
rospy.spin()

 

