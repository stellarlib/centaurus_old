import pygame
from pygame.locals import *
import stellarlib.settings as settings
import sys
from stellarlib.font import FontArchive


class App(object):

    def __init__(self):

        self.current_scene = None

    def initialize(self):

        pygame.init()
        flags = []
        if settings.FULLSCREEN_MODE:
            flags.append(FULLSCREEN)
        pygame.display.set_mode((settings.SCREEN_W, settings.SCREEN_H), *flags)

        FontArchive.get_instance().create_default_font()

    def main(self):

        while self.current_scene:
            complete = self.current_scene.main()
            if complete:
                next_scene_key = self.current_scene.get_next_scene()
                self.current_scene = self.load_next_scene(next_scene_key)

        pygame.quit()
        sys.exit()

    def load_next_scene(self, next_scene):
        if next_scene == 'exit':
            return None
        else:
            return next_scene
