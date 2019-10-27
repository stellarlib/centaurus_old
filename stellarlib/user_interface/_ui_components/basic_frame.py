import pygame
from stellarlib.color import Color


class BasicFrame(object):

    def __init__(self, ui_node, color):
        self.color = color
        self.rect = pygame.Rect((0, 0), (ui_node.click_box.w, ui_node.click_box.h))

    def update(self):
        pass

    def draw(self, display_surface, rel_pos):
        self.rect.topleft = rel_pos
        pygame.draw.rect(display_surface.surface, Color.PANEL_BACK, self.rect, 0)
        pygame.draw.rect(display_surface.surface, self.color, self.rect, 1)
