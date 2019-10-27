import pygame
from stellarlib.settings import PIXEL_SCALE


class FontArchive(object):

    instance = None

    @classmethod
    def get_instance(cls):

        if cls.instance is None:
            cls.instance = cls()

        return cls.instance

    def __init__(self):

        self.archive = {}

    def create_font(self, font_key, font_name, size):

        self.archive[font_key] = pygame.font.Font(''.join(('assets\\font\\', font_name, '.ttf')), size)

    def get_font(self, key):
        return self.archive[key]

    def create_default_font(self):

        self.create_font(None, 'visitor2', 12 * PIXEL_SCALE)
