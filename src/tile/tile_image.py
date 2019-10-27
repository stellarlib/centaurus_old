import os
import pygame
from src.settings import TILE_W, TILE_H
from src.color import Color


class TileImage(object):

    tile_path = os.path.join('assets', 'hex')

    def __init__(self, tile):

        self._surface = self._load_surface(tile)
        self._rect = self._surface.get_rect()

    def _load_surface(self, tile):

        filename = ''.join((tile, '.png'))
        path = os.path.join(TileImage.tile_path, filename)

        surface = pygame.image.load(path)
        surface = pygame.transform.scale(surface, (TILE_W, TILE_H))
        surface.set_colorkey(Color.PURE_WHITE)
        surface = surface.convert()

        return surface

    def draw(self, surface, pos):

        self._rect.center = pos
        surface.blit(self._surface, self._rect)
