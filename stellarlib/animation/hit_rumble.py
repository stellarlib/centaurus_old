from animation import Animation
from stellarlib.vector import Vector
from random import choice


class HitRumble(Animation):

    def __init__(self, actor, heavy=False):

        Animation.__init__(self, actor, permanent=False)
        self.vector = Vector(0, 0)
        self.tick = 0
        self.duration = 12
        if heavy:
            self.duration += 10
        self.x_shake = choice((1, -1))
        self.y_shake = choice((1, -1))

    def update(self):

        if self.tick/3 % 2 == 0:
            self.vector.set(self.x_shake, self.y_shake)
        else:
            self.vector.set(-self.x_shake, -self.y_shake)

        self.tick += 1

        if self.tick > self.duration:
            self.is_complete()

    def update_vector(self, vector):

        vector.add(self.vector)
