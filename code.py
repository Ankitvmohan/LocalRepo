import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def formula(self):
        return (math.pi * (self.radius** 2))


shape = Circle(10)
print(round(shape.formula(), 3))