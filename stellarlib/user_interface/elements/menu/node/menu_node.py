from ... import UINode
from stellarlib.user_interface._ui_components import BasicFrame
from stellarlib.user_interface.elements.menu_button.node.menu_button_node import MenuButtonNode


class MenuNode(UINode):

    def __init__(self, element_id, parent, pos, model=None):

        w = 100
        h = 100

        UINode.__init__(self, element_id, parent, pos, w, h, model)

        self.add_component(BasicFrame(self, (255, 0, 0)))

        self.add_menu_buttons()

    def add_menu_buttons(self):

        i = 0
        for el_id in self.model.button_list:

            button = MenuButtonNode(el_id, self, (0, 0))
            self.position_button(button, i)
            i += 1

    def position_button(self, button, i):

        x = 5
        y = 5 + 22 * i

        button.transform.base_position.set(x, y)


