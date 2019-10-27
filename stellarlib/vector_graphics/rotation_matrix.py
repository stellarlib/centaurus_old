from math import sin, cos, radians


class RotationMatrix(object):

    @staticmethod
    def rotate((vx, vy), angle):

        th = radians(angle)

        x = vx * cos(th) - vy * sin(th)
        y = vx * sin(th) + vy * cos(th)

        return x, y
