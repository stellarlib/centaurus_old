import pygame
from stellarlib.vector import Vector
from stellarlib.color import *
from stellarlib.settings import PIXEL_SCALE


class Sprite(object):

    @classmethod
    def from_surface(cls, surface):

        w = surface.get_width()
        h = surface.get_height()
        surface = pygame.transform.scale(surface, (w * PIXEL_SCALE, h * PIXEL_SCALE))
        surface = surface.convert()
        surface.set_colorkey(WHITE)

        sprite = cls()
        sprite.surface = surface
        sprite.color = WHITE

        return sprite

    @classmethod
    def from_mask_surface(cls, surface):

        w = surface.get_width()
        h = surface.get_height()
        surface = pygame.transform.scale(surface, (w * PIXEL_SCALE, h * PIXEL_SCALE))
        surface = surface.convert()
        surface.set_colorkey(BLACK)

        sprite = cls()
        sprite.surface = surface
        sprite.color = WHITE

        return sprite

    def __init__(self, (x, y)=(0, 0)):

        self.coord = Vector(x, y)
        self.surface = None
        self.color = None

    def draw(self, surf, rel_pos):
        surf.blit(self.surface, self.coord.get_tuple_int())

    def update(self):
        pass

    def set_alpha(self, a):

        self.surface.set_alpha(a)

    def change_color(self, new_color):

        pix_array = pygame.PixelArray(self.surface)

        pix_array.replace(self.color, new_color)
        self.color = new_color
