#This class holds a circle

import numpy as np

class Circle:
  def __init__(self, radius):
    self.radius = radius

  def area(self):
    area = np.pi * self.radius**2
    return area

  def perimeter(self):
    perimeter = 2 * np.pi * self.radius
    return perimeter

  def rescale(self, k):
    self.radius = k*self.radius
