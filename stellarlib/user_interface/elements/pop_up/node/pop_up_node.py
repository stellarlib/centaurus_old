from ... import UINode
from stellarlib.user_interface._ui_components import BasicFrame


class PopUpNode(UINode):

    def __init__(self, element_id, parent, pos, model=None):

        # get image from text and get w h from that

        w = 100
        h = 100

        UINode.__init__(self, element_id, parent, pos, w, h, model)

        self.add_component(BasicFrame(self, (255, 0, 0)))

