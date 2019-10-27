import pygame


class TransformDot(object):

    def __init__(self, node):
        self.node = node

    def draw(self, display_surface, (x, y)):
        pygame.draw.circle(display_surface.surface, (255, 255, 255), (x, y), 2)

    def update(self):
        pass
