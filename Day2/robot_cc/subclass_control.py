#!/usr/bin/env python

from robot_control_class import RobotControl

class SquareMotion(RobotControl):
   def __init__(self, speed, time):
      super(SquareMotion, self).__init__()
      self.speed = speed
      self.time = time
      self.turn_time = 1.9 #Estimate for 90 degree rotation given the speed

   def do_square(self):
      for i in range(4):
         self.move_straight_time('forward', self.speed, self.time)
         self.turn('clockwise', self.speed, self.turn_time)

sub_con = SquareMotion(1.3, 2)	
sub_con.do_square()  


