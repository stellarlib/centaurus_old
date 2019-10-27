import pygame
from stellarlib.sprite import Sprite
from stellarlib.color import Color
from stellarlib.map_tools import all_points, in_bounds, get_edge
from stellarlib.flood_fill import flood_fill


class Silhouette(object):

    @classmethod
    def from_surface(cls, surface):

        w = surface.get_width()
        h = surface.get_height()

        sil = cls(w, h)

        pix_array = pygame.PixelArray(surface)

        for x, y in all_points(sil):
            sil.write_cell(x, y, pix_array[x, y] != surface.map_rgb(Color.WHITE))

        sil.compute_edge()

        return sil

    def __init__(self, w, h):

        self.w = w
        self.h = h

        self.data = [False] * self.w * self.h
        self.edge = []

    def get_cell(self, x, y):
        return self.data[self.get_index(x, y)]

    def write_cell(self, x, y, value):
        self.data[self.get_index(x, y)] = value

    def get_index(self, x, y):
        offset = y * self.w
        return x % self.w + offset

    def impacted(self, (x, y)):
        return in_bounds(self, (x, y)) and self.get_cell(x, y)

    def show(self):

        for y in range(self.h):
            l = []
            for x in range(self.w):
                if self.get_cell(x, y):
                    v = 'x'
                else:
                    v = ' '
                l.append(v)
            l = ''.join(l)
            print l

    def get_mask(self):

        surface = pygame.Surface((self.w, self.h)).convert()
        surface.fill(Color.BLACK)

        pix_array = pygame.PixelArray(surface)

        for x, y in all_points(self):

            if self.get_cell(x, y):
                pix_array[x, y] = Color.WHITE

        return Sprite.from_mask_surface(surface)

    def extend(self, n=2):

        start_edge = filter(lambda (x, y): self.get_cell(x, y), all_points(self))
        extended = flood_fill(start_edge, lambda x: in_bounds(self, x), n)
        new_points = extended.difference(start_edge)

        map(lambda (x, y): self.write_cell(x, y, True), new_points)

        self.compute_edge()

    def compute_edge(self):

        start_edge = filter(lambda (x, y): self.get_cell(x, y), all_points(self))
        self.edge = get_edge(start_edge)

    def get_edge_mask(self):

        surface = pygame.Surface((self.w, self.h)).convert()
        surface.fill(Color.BLACK)

        pix_array = pygame.PixelArray(surface)

        for x, y in self.edge:

            pix_array[x, y] = Color.WHITE

        return Sprite.from_mask_surface(surface)

