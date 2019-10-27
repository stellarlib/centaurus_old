from src.icon import IconSequence
from src.icon.icons import *


class PlayerOverlay(object):

    def __init__(self, player):
        self.player = player
        self.icon_sequence = IconSequence(self.get_icons())

    def draw(self, display_surface, rel_pos):
        self.icon_sequence.draw(display_surface.surface, rel_pos)

    def update(self):

        pass

    def get_icons(self):

        full = self.player.actions
        empty = self.player.max_actions - full

        icons = []
        for i in range(full):
            icons.append(ACTION_FULL)
        for i in range(empty):
            icons.append(ACTION_EMPTY)

        return icons

    def update_icons(self):

        self.icon_sequence.icons = self.get_icons()
