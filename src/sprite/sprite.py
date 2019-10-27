import os
import pygame
from src.settings import PIXEL_SCALE
from src.color import Color


class Sprite(object):

    sprite_path = os.path.join('assets', 'sprites')
    colorkey = Color.SPRITE_COLORKEY

    def __init__(self, name):
        self._surface = self._load_surface(name)
        self._rect = self._surface.get_rect()

    def draw(self, surface, pos):
        self._set_pos(pos)
        surface.blit(self._surface, self._rect)

    def _load_surface(self, name):

        path = self._load_path(name)
        surface = pygame.image.load(path)

        w = surface.get_width() * PIXEL_SCALE
        h = surface.get_height() * PIXEL_SCALE

        surface = pygame.transform.scale(surface, (w, h))
        surface.set_colorkey(Sprite.colorkey)
        surface = surface.convert()

        return surface

    def _set_pos(self, pos):

        self._rect.center = pos

    def _load_path(self, name):
        fname = ''.join((name, '.png'))
        path = os.path.join(Sprite.sprite_path, fname)
        return path

    def replace_color(self, old, new):

        pix_array = pygame.PixelArray(self._surface)
        pix_array.replace(old, new)

    def mask(self, mask_color):

        pix_array = pygame.PixelArray(self._surface)

        back_color = self._surface.map_rgb(Color.SPRITE_COLORKEY)

        for x in range(pix_array.shape[0]):
            for y in range(pix_array.shape[1]):
                if pix_array[x, y] != back_color:
                    pix_array[x, y] = mask_color
