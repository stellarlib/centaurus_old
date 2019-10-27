import pygame
from stellarlib.settings import PIXEL_SCALE
from particle import Particle
from random import randint


class ShieldFlash(Particle):

    rect = pygame.Rect((0, 0), (PIXEL_SCALE, PIXEL_SCALE))
    color_variance = 15

    def __init__(self, group, coord, color_palette):

        Particle.__init__(self, group, coord)
        self.duration = 10
        self.palette = color_palette
        self.color = self.palette.high

        self.mid_switch = int(self.duration * .8)
        self.low_switch = self.duration / 2

    def on_update(self):
        self.duration -= 1
        if self.duration < self.low_switch:
            self.color = self.palette.low
        elif self.duration < self.mid_switch:
            self.color = self.palette.mid

        self.vary_color()

    def draw(self, display_surface, (rx, ry)):
        x, y = self.coord.get_tuple_int()
        ShieldFlash.rect.topleft = rx + x, ry + y
        pygame.draw.rect(display_surface.surface, self.color, self.rect)

    def check_end_condition(self):
        return self.duration <= 0

    def vary_color(self):

        v = ShieldFlash.color_variance

        r, g, b = self.color
        r += randint(-v, v)
        g += randint(-v, v)
        b += randint(-v, v)

        r = max(min((r, 255)), 0)
        g = max(min((g, 255)), 0)
        b = max(min((b, 255)), 0)
        self.color = r, g, b
