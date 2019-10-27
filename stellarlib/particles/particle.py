from stellarlib.vector import Vector


class Particle(object):

    def __init__(self, group, (x, y)):

        self.coord = Vector(x, y)
        self.group = group
        self.group.add(self)

    def update(self):
        self.on_update()
        if self.check_end_condition():
            self.end()
            self.deinitialize()

    def draw(self, surf, (rx, ry)):
        pass

    def on_update(self):
        pass

    def check_end_condition(self):
        return True

    def end(self):
        self.group.mark_for_removal(self)

    def deinitialize(self):
        pass
