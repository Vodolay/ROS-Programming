#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

rospy.init_node('turnstyle')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(10)
go = Twist()

go.linear.x = 0.5 #Move the robot with linear velocity 1.0 in the x-axis
go.angular.z = 0.5 #Move the robot with angular velocity 0.8

while not rospy.is_shutdown():
   pub.publish(go)
   rate.sleep()
