

class BeamColors(object):

    def __init__(self, base_color):

        self.high = self.lerp_color(base_color, 255, .99)
        self.mid = base_color
        self.low = self.lerp_color(base_color, 0, .2)

    def lerp_color(self, (r, g, b), dest, weight):

        r = self.lerp_shade(r, dest, weight)
        g = self.lerp_shade(g, dest, weight)
        b = self.lerp_shade(b, dest, weight)

        return r, g, b

    def lerp_shade(self, c, dest, weight):

        diff = dest - c
        weighted_diff = int(weight * diff)

        return c + weighted_diff
