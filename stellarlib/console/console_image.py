from stellarlib.settings import SCREEN_W, SCREEN_H
import pygame
from stellarlib.color import Color


class ConsoleImage(object):

    def __init__(self, console):

        self.console = console
        self.line_builder = console.line_builder
        self.coord = 0, SCREEN_H - self.line_builder.line_height

        self.console_height = self.console.num_lines * self.line_builder.line_height
        self.scroll_coord = 0, -self.line_builder.line_height
        self.push_coord = 0, self.console_height - self.line_builder.line_height

        self.image = None
        self.buffer_image = None

        self.init_image()

    @property
    def color_back(self):
        return self.console.color_back

    @property
    def alpha(self):
        return self.console.alpha

    def init_image(self):

        self.image = pygame.Surface((SCREEN_W, self.console_height)).convert()
        r = self.image.get_rect()
        r.bottomleft = self.coord
        self.coord = r.topleft

        self.image.fill(self.color_back)
        self.image.set_alpha(self.alpha)

        self.buffer_image = pygame.Surface((SCREEN_W, self.console_height)).convert()
        self.buffer_image.fill(self.color_back)

    def draw(self, surface):
        surface.blit(self.image, self.coord)

    def scroll(self):

        self.buffer_image.fill(self.color_back)
        self.buffer_image.blit(self.image, (0, 0))
        self.image.fill(self.color_back)
        self.image.blit(self.buffer_image, self.scroll_coord)

    def add_line(self, text, color):

        line = self.line_builder.get_text_line(text, color, self.color_back)
        self.image.blit(line, self.push_coord)
