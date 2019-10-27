from animation import Animation
from stellarlib.vector import Vector


class Orbit(Animation):

    # takes in radius of rotation, start angle, speed
    def __init__(self, actor, radius, duration, start_angle=0, clockwise=True):

        Animation.__init__(self, actor, permanent=False)

        self.position = Vector(radius, 0)
        self.angle = float(start_angle)
        self.radius = radius
        self.duration = duration
        self.incr = 360.0 / self.duration

        if not clockwise:
            self.incr *= -1

    def update(self):
        self.position.set_at_angle(self.angle)
        self.angle += self.incr

    def update_vector(self, vector):

        vector.add(self.position)
