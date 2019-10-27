import pygame
from stellarlib.color import Color


class TransparentBox(object):

    alpha = 180

    def __init__(self, ui_node):
        self.surface = pygame.Surface((ui_node.click_box.w, ui_node.click_box.h))
        self.rect = self.surface.get_rect()

        self.surface.fill(Color.PANEL_BACK)
        self.surface.set_alpha(TransparentBox.alpha)

    def update(self):
        pass

    def draw(self, display_surface, rel_pos):
        display_surface.surface.blit(self.surface, rel_pos)
