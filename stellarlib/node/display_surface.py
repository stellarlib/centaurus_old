import pygame
from stellarlib.color import Color
from random import randint


class DisplaySurface(object):

    def __init__(self, w, h, color=Color.BLACK, refresh=False, colorkey=False):

        self.color = color
        self.surface = pygame.Surface((w, h)).convert()
        self.surface.fill(self.color)

        if colorkey:
            self.surface.set_colorkey(self.color)

        self.refresh = refresh

    def update(self):
        if self.refresh:
            #self.color = (randint(0,255), randint(0,255), randint(0,255))
            self.clear()

    def clear(self):
        self.surface.fill(self.color)

    def blit(self, surface, pos):
        self.surface.blit(surface, pos)
