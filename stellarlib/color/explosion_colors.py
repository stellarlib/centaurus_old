from random import randint


class ExplosionColors(object):

    variance = 50

    def __init__(self):

        self.high = (250, 20, 0)
        self.mid = (200, 150, 5)
        self.low = (240, 240, 10)
        self.smoke = (60, 40, 40)

    def vary_color(self, (r, g, b)):

        r = self.vary(r)
        g = self.vary(g)
        b = self.vary(b)

        return r, g, b

    def vary(self, c):

        c += randint(-ExplosionColors.variance, ExplosionColors.variance)
        c = min((max(c, 0), 255))

        return c
