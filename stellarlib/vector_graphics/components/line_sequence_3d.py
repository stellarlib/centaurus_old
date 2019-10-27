from line_sequence import LineSequence
import pygame


class LineSequence3D(LineSequence):

    def __init__(self, model, vertices, color_id='main', closed=False):

        LineSequence.__init__(self, model, vertices, color_id, closed)

    def draw(self, surface, points, colors):

        color = colors[self.color_id]
        if color is None:
            return

        vertices = self.visible_vertices(points)
        pygame.draw.aalines(surface, color, self.closed, vertices)

    def visible_vertices(self, points):

        return [points[v] for v in self.vertices]
