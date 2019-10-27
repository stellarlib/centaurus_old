from ... import UIModel
from stellarlib.user_interface.elements.menu_button.model.menu_button_model import MenuButtonModel


class MenuModel(UIModel):

    """
    Models a menu with button elements that can be clicked. Implement State Machine functionality
    tied to the string element ids of the buttons

    Requires keyword arg buttons = [ ] - list of string element ids. Order is important.

    """

    def __init__(self, ui_control, element_id, model=None, *args, **kwargs):

        UIModel.__init__(self, ui_control, element_id, model)
        self.button_list = self._create_button_element_ids(kwargs['buttons'])
        self._create_menu_button_models()

    def _create_button_element_ids(self, buttons):

        return ['-'.join((self.element_id, b)) for b in buttons]

    def _create_menu_button_models(self):

        for button_id in self.button_list:
            self.ui_control.make_ui_model(MenuButtonModel, button_id, parent_menu=self)

    def click(self, button_id):
        print button_id + ' sub element was clicked'
