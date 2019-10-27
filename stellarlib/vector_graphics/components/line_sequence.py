import pygame


class LineSequence(object):

    def __init__(self, model, vertices, color_id='main', closed=False):

        self.model = model
        self.vertices = vertices
        self.color_id = color_id
        self.closed = closed

    def draw(self, surface, points, colors):

        color = colors[self.color_id]
        if color is None:
            return

        vertices = [points[v] for v in self.vertices]
        pygame.draw.aalines(surface, color, self.closed, vertices)
