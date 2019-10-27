from animation import Animation
from stellarlib.vector import Vector


class Lerp(Animation):

    # takes in destination position, and smoothly transitions to it then stops
    def __init__(self, actor, start, dest, time, snap=False):

        Animation.__init__(self, actor, permanent=False)
        self.position = Vector(0, 0)
        self.vector = Vector(dest)
        self.vector.sub(Vector(start))
        self.vector.div(time)

        self.tick = 0
        self.time = time
        self.snap = snap

    def update(self):
        self.position.add(self.vector)
        self.tick += 1

        if self.snap and self.tick == self.time:
            self.permanent = True
        if self.tick > self.time:
            self.end()

    def update_vector(self, vector):

        vector.add(self.position)
