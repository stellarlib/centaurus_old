from src.sprite.sprite import Sprite
import os


class IconSprite(Sprite):

    icon_path = os.path.join('assets', 'icons')

    def __init__(self, icon):

        Sprite.__init__(self, icon)

    def _load_path(self, name):
        fname = ''.join((name, '.png'))
        path = os.path.join(IconSprite.icon_path, fname)
        return path
