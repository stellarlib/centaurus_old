# hex_tool module adapted from code from redblobgames.com
# by Amit Patel
# available under MIT License or Apace according to homepage

from hex import Hex


class FractionalHex(object):

    def __init__(self, x, y, z):

        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def hex_round(self):

        x = int(round(self.x))
        y = int(round(self.y))
        z = int(round(self.z))

        x_diff = abs(x - self.x)
        y_diff = abs(y - self.y)
        z_diff = abs(z - self.z)

        if x_diff > y_diff and x_diff > z_diff:
            x = -y-z
        elif y_diff > z_diff:
            y = -x-z
        else:
            z = -x-y

        return Hex(x, y)
