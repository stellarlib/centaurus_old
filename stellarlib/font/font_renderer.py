import pygame
from font_archive import FontArchive
from stellarlib.settings import PIXEL_SCALE
from stellarlib.color import Color


class FontRenderer(object):

    def __init__(self, font_key=None):

        self.font = FontArchive.get_instance().get_font(font_key)
        self.x_padding = PIXEL_SCALE * 2
        self.y_padding = PIXEL_SCALE * 2

    def create_text_image(self, text, color, color_back, scale_up=True):

        font_image = self.font.render(text, False, color)

        adjusted = pygame.Surface((font_image.get_width(), font_image.get_height() - 1)).convert()
        adjusted.fill(color_back)
        adjusted.blit(font_image, (0, -1))

        w = adjusted.get_width()
        h = adjusted.get_height()

        if scale_up:
            return pygame.transform.scale(adjusted, (w * PIXEL_SCALE, h * PIXEL_SCALE))
        else:
            return adjusted

    def create_padded_text(self, text, color, color_back=Color.BLACK, colorkey=False):

        text = self.create_text_image(text, color, color_back)

        w = text.get_width()
        h = text.get_height()

        final_w = w + self.x_padding * 2
        final_h = h + self.y_padding * 2

        final_coord = self.x_padding, 0

        final_image = pygame.Surface((final_w, final_h)).convert()
        final_image.fill(color_back)
        final_image.blit(text, final_coord)

        if colorkey:
            final_image.set_colorkey(color_back)

        return final_image

    def create_fitted_text(self, text, color, w, h, scale_up=False, color_back=Color.BLACK, colorkey=False):

        text = self.create_text_image(text, color, color_back, scale_up=scale_up)

        tw = text.get_width()
        th = text.get_height()

        if tw > w or th > h:
            raise Exception("cannot fit text into container smaller than it's basic one.")

        inner_coord = ((w - tw) / 2, (h - th) / 2)

        final_image = pygame.Surface((w, h)).convert()
        final_image.fill(color_back)
        final_image.blit(text, inner_coord)

        if colorkey:
            final_image.set_colorkey(color_back)

        return final_image
