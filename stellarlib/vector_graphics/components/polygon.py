import pygame
from pygame.gfxdraw import aapolygon, filled_polygon


class Polygon(object):

    def __init__(self, model, vertices, color_id='main'):

        self.model = model
        self.vertices = vertices
        self.color_id = color_id

    def draw(self, surface, points, colors):

        color = colors[self.color_id]
        if color is None:
            return
        vertices = [points[v] for v in self.vertices]

        # pygame.draw
        # pygame.draw.polygon(surface, self.color, vertices, self.width)

        # pygame.gfxdraw
        aapolygon(surface, vertices, color)
        filled_polygon(surface, vertices, color)
