from ... import UIModel


class MenuButtonModel(UIModel):

    def __init__(self, ui_control, element_id, *args, **kwargs):
        UIModel.__init__(self, ui_control, element_id)
        self.parent_menu = kwargs['parent_menu']

    def on_left_click(self):
        self.parent_menu.click(self.element_id)
