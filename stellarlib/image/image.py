import pygame
from stellarlib.settings import PIXEL_SCALE
from stellarlib.color import Color


class Image(object):

    @classmethod
    def from_file(cls, fname):

        image = cls()
        image.init_image(image.load_file_surface(fname))

        return image

    @classmethod
    def from_image(cls, image):

        new_image = cls()
        surface = image.surface.copy()
        new_image.init_image(surface, scaled_up=True)

        return new_image

    def __init__(self):

        self.surface = None
        self.rect = None

    @staticmethod
    def load_file_surface(fname):
        return pygame.image.load('assets\\' + fname + '.png')

    def init_image(self, surface, scaled_up=False):

        self.surface = surface

        if scaled_up:
            self.scale_up(PIXEL_SCALE)
        self.prepare_image()

    @property
    def width(self):
        return self.surface.get_width()

    @property
    def height(self):
        return self.surface.get_height()

    def draw(self, surface, pos):

        self.rect.center = pos
        surface.blit(self.surface, self.rect)

    def flip(self, horizontal_flip=False, vertical_flip=False):

        self.surface = pygame.transform.flip(self.surface, horizontal_flip, vertical_flip)

    def scale_up(self, scale):

        self.surface = pygame.transform.scale(self.surface, (self.width * scale, self.height * scale))

    def prepare_image(self):

        self.surface = self.surface.convert()
        self.surface.set_colorkey(Color.WHITE)
        self.rect = self.surface.get_rect()

    def recolor(self, old_color, new_color):

        pix_array = pygame.PixelArray(self.surface)
        pix_array.replace(old_color, new_color)

    def update(self):

        pass
