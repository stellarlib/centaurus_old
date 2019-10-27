from ... import UINode
from stellarlib.user_interface._ui_components import BasicFrame


class MenuButtonNode(UINode):

    def __init__(self, element_id, parent, pos):

        # get image from text and get w h from that

        w = 80
        h = 20

        UINode.__init__(self, element_id, parent, pos, w, h)

        self.add_component(BasicFrame(self, (255, 0, 0)))

