import pygame
from stellarlib.settings import PIXEL_SCALE
from particle import Particle


class ExplosionParticle(Particle):

    rect = pygame.Rect((0, 0), (PIXEL_SCALE, PIXEL_SCALE))
    duration = 14

    def __init__(self, group, coord, color_palette, weight=0):

        Particle.__init__(self, group, coord)
        self.duration = ExplosionParticle.duration - weight/2
        self.palette = color_palette
        self.base_color = self.palette.high
        self.color = self.palette.vary_color(self.base_color)

        self.mid_switch = int(self.duration * .9)
        self.low_switch = int(self.duration * .7)
        self.smoke_switch = int(self.duration * .5)

    def on_update(self):
        if self.duration < self.smoke_switch:
            self.base_color = self.palette.smoke
        elif self.duration < self.low_switch:
            self.base_color = self.palette.low
        elif self.duration < self.mid_switch:
            self.base_color = self.palette.mid

        self.color = self.palette.vary_color(self.base_color)
        self.duration -= 1

    def draw(self, surf, (rx, ry)):
        x, y = self.coord.get_tuple_int()
        ExplosionParticle.rect.topleft = rx + x, ry + y
        pygame.draw.rect(surf.surface, self.color, self.rect)

    def check_end_condition(self):
        return self.duration <= 0
