import pygame


class Point(object):

    def __init__(self, model, point, width, color_id='main'):

        self.model = model
        self.point = point

        self.color_id = color_id
        self.width = width

    def draw(self, surface, points, colors):

        color = colors[self.color_id]
        if color is None:
            return

        pygame.draw.circle(surface, color, points[self.point], self.width)
