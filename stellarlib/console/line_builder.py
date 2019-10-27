from char_image import CharImage
from stellarlib.settings import SCREEN_W
import pygame


class LineBuilder(object):

    line_height = CharImage.h

    def __init__(self, console):

        self.console = console

        self.image_dict = self._init_image_dict()
        self.line_image = self._init_line_image()

    def _init_image_dict(self):

        image_dict = {}

        for char in self.console._keys.values():

            image_dict[char] = CharImage(char, self.console.color_back)

        for char in self.console._shift_keys.values():
            image_dict[char] = CharImage(char, self.console.color_back)

        return image_dict

    def _init_line_image(self):

        return pygame.Surface((SCREEN_W, self.line_height)).convert()

    def draw_char(self, char, i, surface, color):

        self.image_dict[char].draw(surface, i, color)

    def get_text_line(self, text, color, color_back):

        self.line_image.fill(color_back)

        i = 0
        for c in text:
            self.draw_char(c, i, self.line_image, color)
            i += 1

        return self.line_image
