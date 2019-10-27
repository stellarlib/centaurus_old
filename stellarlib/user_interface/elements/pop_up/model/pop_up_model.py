from ... import UIModel


class PopUpModel(UIModel):

    def __init__(self, ui_control, element_id, *args, **kwargs):
        UIModel.__init__(self, ui_control, element_id, movement_listen=True)

    def on_movement(self):
        #self.close_node()
        #self.close_model()
        pass