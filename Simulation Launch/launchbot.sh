#!/bin/bash
#gnome-terminal -e "roscore"
#sleep 3
gnome-terminal -e "roslaunch turtlebot3_gazebo turtlebot3_world.launch"
sleep 3
gnome-terminal -e "roslaunch turtlebot3_bringup turtlebot3_remote.launch"
sleep 3
gnome-terminal -e "rosrun rviz rviz -d `rospack find turtlebot3_description`/rviz/model.rviz"
