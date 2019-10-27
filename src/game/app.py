import stellarlib.app.app as sla
import pygame
from pygame.locals import FULLSCREEN
import src.settings as settings
from stellarlib.font import FontArchive


class App(sla.App):

    def __init__(self):
        sla.App.__init__(self)

    def initialize(self):

        pygame.init()
        flags = []
        if settings.FULLSCREEN_MODE:
            flags.append(FULLSCREEN)
        pygame.display.set_mode((settings.SCREEN_W, settings.SCREEN_H), *flags)

        FontArchive.get_instance().create_font(None, 'QUICGB__', 4 * settings.PIXEL_SCALE)
