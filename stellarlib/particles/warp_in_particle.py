from particle import Particle
from stellarlib.lerp.lerp import lerp_color
from stellarlib.color import Color
from stellarlib.settings import PIXEL_SCALE
import pygame
from random import randint


class WarpInParticle(Particle):

    rect = pygame.Rect((0, 0), (PIXEL_SCALE, PIXEL_SCALE))
    lifespan = 30

    def __init__(self, group, (x, y), final_color, start_color=Color.WHITE):

        Particle.__init__(self, group, (x, y))
        self.color = start_color
        self.start_color = start_color
        self.final_color = final_color

        self.tick = 0
        r = (10 + randint(-2, 2)) / 10.0
        self.duration = float(int(WarpInParticle.lifespan * r))

    def on_update(self):
        self.tick += 1

        self.lerp_color()

    def draw(self, surf, (rx, ry)):

        x, y = self.coord.get_tuple_int()
        WarpInParticle.rect.topleft = rx + x, ry + y
        pygame.draw.rect(surf, self.color, self.rect)

    def check_end_condition(self):
        return self.tick > self.duration

    def lerp_color(self):

        t = self.tick / self.duration

        self.color = lerp_color(self.start_color, self.final_color, t)
