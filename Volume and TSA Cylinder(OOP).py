from math import pi


class Cylinder:

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        vol = pi * self.radius * self.radius * self.height
        return "Volume = " + str(vol)

    def surface_area(self):
        tsa = 2 * pi * self.radius * self.height + 2 * pi * self.radius * self.radius
        return "Area = " + str(tsa)


c = Cylinder(2, 3)
print(c.volume())
print(c.surface_area())


