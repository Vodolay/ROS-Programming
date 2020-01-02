#This class holds a rhombus

import numpy as np

class Rhombus:
  def __init__(self, x, y, theta):
    self.x = x
    self.y = y
    self.theta = theta

  def area(self):
    area = self.x * self.y * np.sin(self.theta)
    return area

  def perimeter(self):
    perimeter = 2*self.x + 2*self.y
    return perimeter

  def rescale(self, k):
    self.x = k*self.x
    self.y = k*self.y
