from stellarlib.font import FontRenderer
from stellarlib.color import Color
import pygame
from stellarlib.settings import PIXEL_SCALE


class CharImage(object):

    h = 12 * PIXEL_SCALE
    w = 8 * PIXEL_SCALE

    def __init__(self, char, color_back):

        self.color = Color.WHITE
        self.image = self._init_image(char, color_back)

    def _init_image(self, char, color_back):

        font = FontRenderer()
        return font.create_fitted_text(char, self.color, CharImage.w, CharImage.h, color_back=color_back)

    def draw(self, surface, i, color):

        if color != self.color:
            self.recolor(color)
        surface.blit(self.image, (i*CharImage.w, 0))

    def recolor(self, new_color):

        px_array = pygame.PixelArray(self.image)
        px_array.replace(self.color, new_color)
        self.color = new_color
