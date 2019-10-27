from stellarlib.user_interface import UINode
from stellarlib.settings import SCREEN_W, SCREEN_H


class RootUINode(UINode):

    def __init__(self, parent):

        UINode.__init__(self, 'root_ui', parent, (0, 0), SCREEN_W, SCREEN_H)
        # TODO doesn't need a click box
        self.ui_control = None

    def touch(self, mouse_pos):

        for node in self.children:
            touched = node.touch(mouse_pos)
            if touched:
                return touched

        return None
