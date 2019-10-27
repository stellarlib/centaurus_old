import pygame


class Line(object):

    def __init__(self, model, start, end, color_id='main', width=1):

        self.model = model
        self.start = start
        self.end = end

        self.color_id = color_id
        self.width = width

    def draw(self, surface, points, colors):

        color = colors[self.color_id]
        if color is None:
            return

        pygame.draw.aaline(surface, color, points[self.start], points[self.end], self.width)
