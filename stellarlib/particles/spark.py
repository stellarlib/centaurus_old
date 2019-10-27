from particle import Particle
import pygame
from random import choice


class Spark(Particle):

    def __init__(self, group, (x, y), d=60):

        Particle.__init__(self, group, (x, y))
        self.color = (0, 200, 200)
        self.rect = pygame.Rect((x, y), (2,2))
        self.duration = d

    def on_update(self):
        self.color = choice(((0, 200, 200), (0, 150, 200), (255,255,255)))
        self.duration -= 1

    def draw(self, surf):
        pygame.draw.rect(surf, self.color, self.rect)

    def check_end_condition(self):
        return self.duration <= 0
