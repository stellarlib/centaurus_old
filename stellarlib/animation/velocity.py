from animation import Animation
from stellarlib.vector import Vector


class Velocity(Animation):

    # takes a direction vector and moves it's actor by it every frame
    def __init__(self, actor, vec):

        Animation.__init__(self, actor)

        self.vector = Vector(vec)

    def bind_vector(self, vec):
        self.vector = vec

    def update(self):
        pass

    def update_vector(self, vector):

        vector.add(self.vector)
