from src.icon.icon_sprite import IconSprite
from src.icon.icons import *
from src.settings import PIXEL_SCALE


class IconSequence(object):

    icon_sprites = None

    @classmethod
    def init(cls):

        cls.icon_sprites = {ACTION_FULL: IconSprite('action_full'),
                            ACTION_EMPTY: IconSprite('action_empty')}

    def __init__(self, icons, spacing=PIXEL_SCALE*21):

        if IconSequence.icon_sprites is None:
            IconSequence.init()

        self.icons = icons
        self.spacing = spacing

    def draw(self, surface, (x, y)):

        for i in range(len(self.icons)):
            self.draw_icon(surface, (x, y), i)

    def draw_icon(self, surface, (x, y), i):

        icon = IconSequence.icon_sprites.get(self.icons[i])
        x += i * self.spacing
        icon.draw(surface, (x, y))
