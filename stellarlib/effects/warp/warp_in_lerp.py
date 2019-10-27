from stellarlib.settings import PIXEL_SCALE
from stellarlib.lerp.lerp import lerp


class WarpInLerp(object):

    def __init__(self, warp_effect, interval):

        self.warp_effect = warp_effect

        self.tick = 0
        self.duration = float(self.warp_effect.sprite_length * interval)

        w = (self.warp_effect.silhouette.w / 2) * PIXEL_SCALE
        h = (self.warp_effect.silhouette.h / 2) * PIXEL_SCALE
        sprite_len = self.warp_effect.sprite_length * PIXEL_SCALE

        self.end = -w
        self.start = -w + sprite_len
        if self.warp_effect.x_flip:
            self.start = -sprite_len -w

        self.x = 0
        self.y = -h

    def run(self):

        t = self.tick / self.duration

        if t > 1.0:
            pass
        else:
            self.x = int(lerp(self.start, self.end, t))

        self.tick += 1

    def get_coord(self, (rx, ry)):

        x = self.x + rx
        y = self.y + ry
        return x, y
