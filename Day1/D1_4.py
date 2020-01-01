#This class computes areas and perimeters based on a shape

import sys
from D1_3 import Rhombus

class Geometry:
  def __init__(self, shape):
    self.shape = shape

  def shape_area(self):
    if shape == 'Rhombus':
      romb = Rhombus(1.1, 2.1, 0.23)
      return romb.area()
    elif shape == 'Circle':
      return 'WARNING: Circles are under development' 
    else:
      return 'WARNING: Can not compute areas for such extravagant shapes'

  def shape_perimeter(self):
    if shape == 'Rhombus':
      romb = Rhombus(1.1, 2.1, 0.23)
      return romb.perimeter()
    elif shape == 'Circle':
      return 'WARNING: Circles are under development'
    else:
      return 'WARNING: Can not compute perimeters for such extravagant shapes'

if __name__ == "__main__":
  shape = str(sys.argv[1])
  geo = Geometry(shape)
  print("This is a {}".format(shape))
  print("The area is: {}".format(geo.shape_area()))
  print("The perimeter is: {}".format(geo.shape_perimeter()))
