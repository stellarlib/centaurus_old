from animation import Animation
from stellarlib.vector import Vector
from math import sin, pi


class SineMotion(Animation):

    # takes the max distance from center - amplitude
    # and number of frames it takes to complete one half period - half_period
    def __init__(self, actor, amplitude, half_period=10):

        Animation.__init__(self, actor, permanent=False)
        self.vector = Vector(0, 0)
        self.amplitude = amplitude
        self.tick = 0
        self.half_period = float(half_period)
        self.period = half_period*2*pi

    def update(self):

        t = self.tick / self.half_period

        y = self.amplitude * sin(t)
        self.vector.set(0, y)

        self.tick += 1

        if self.tick > self.period:
            self.wave_complete()

    def update_vector(self, vector):

        vector.add(self.vector)

    def wave_complete(self):
        self.end()
