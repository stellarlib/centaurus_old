

class Angle2D(object):

    def __init__(self, degrees=0.0):

        self.degrees = self.sanitize_degrees(degrees)

    @staticmethod
    def sanitize_degrees(degrees):

        degrees = float(degrees)

        if degrees < 0.0:
            degrees += 360.0
        elif degrees > 360.0:
            degrees -= 360.0

        return degrees

    def get_angle_difference(self, angle):

        # return positive float if turning right is nearer
        # negative float if turning left is nearer

        a = self.degrees
        b = angle.degrees

        if b < a and b < a - 180.0:
            return b - a + 360.0
        else:
            return b - a

    def set_angle(self, degrees):
        self.degrees = self.sanitize_degrees(degrees)

    def __str__(self):
        return str(self.degrees)

    def add(self, mod):
        self.degrees += mod
