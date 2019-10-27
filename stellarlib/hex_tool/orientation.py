# hex_tool module adapted from code from redblobgames.com
# by Amit Patel
# available under MIT License or Apace according to homepage

from math import sqrt


class Orientation(object):

    def __init__(self, f0, f1, f2, f3, b0, b1, b2, b3, start_angle):

        self.f0 = f0
        self.f1 = f1
        self.f2 = f2
        self.f3 = f3
        self.b0 = b0
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.start_angle = start_angle


pointy_layout = Orientation(sqrt(3.0),       sqrt(3.0) / 2.0, 0.0,      3.0 / 2.0,
                            sqrt(3.0) / 3.0, -1.0 / 3.0,      0.0,      2.0 / 3.0,
                            0.5)

flat_layout = Orientation(3.0 / 2.0, 0.0, sqrt(3.0) / 2.0,  sqrt(3.0),
                          2.0 / 3.0, 0.0, -1.0 / 3.0,       sqrt(3.0) / 3.0,
                          0.0)
