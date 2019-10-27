from animation import Animation
from stellarlib.vector import Vector


class QuadraticHop(Animation):

    def __init__(self, actor, peak, duration):

        Animation.__init__(self, actor, permanent=False)

        self.duration = duration
        peak = -float(peak)
        duration = float(duration) - 1
        self.a = self.get_a(peak, duration)
        self.func = self.get_func(duration)
        self.vector = Vector()
        self.t = 0

    def get_a(self, peak, duration):

        d = duration / 2 * -(duration / 2)

        return peak / d

    def get_func(self, duration):

        def func(x):
            return self.a * x * (x - duration)

        return func

    def update(self):

        self.vector.set(0, self.func(self.t))

        self.t += 1

        if self.t > self.duration:
            self.end()

    def update_vector(self, vector):

        vector.add(self.vector)
