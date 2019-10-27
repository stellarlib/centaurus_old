from stellarlib.settings import SCREEN_W, SCREEN_H
import pygame


class PromptImage(object):

    def __init__(self, console):

        self.console = console
        self.line_builder = self.console.line_builder
        self.coord = (0, SCREEN_H)
        self.h = self.console.line_builder.line_height

        self.image = None

        self.init_image()

    @property
    def color_back(self):
        return self.console.color_back

    @property
    def def_color(self):
        return self.console.def_color

    @property
    def alpha(self):
        return self.console.alpha

    def init_image(self):

        self.image = pygame.Surface((SCREEN_W, self.h))
        r = self.image.get_rect()
        r.bottomleft = self.coord
        self.coord = r.topleft

        self.image.fill(self.color_back)
        self.image.set_alpha(self.alpha)

        self.clear()

    def draw(self, surface):
        surface.blit(self.image, self.coord)

    def keystroke(self, char, i):
        self.line_builder.draw_char(char, i, self.image, self.def_color)

    def backspace(self, i):
        self.line_builder.draw_char(' ', i, self.image, self.def_color)

    def clear(self):
        self.image.fill(self.color_back)
        self.line_builder.draw_char('>', 0, self.image, self.def_color)
