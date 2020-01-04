# ROS Programming

To start a Gazebo simulation with TurtleBot3 in an empty world, type

roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch

For TurtleBot3 living in a ROS world, type

roslaunch turtlebot3_gazebo turtlebot3_world.launch

To create a new ROS package, go to catkin_ws/src and type

catkin_create_pkg <package_name> <dependencies>

After that you still have to at least create a launch subdirectory and 
write a lunch file in it as well as put Python scripts in the src subdirectory.


 
