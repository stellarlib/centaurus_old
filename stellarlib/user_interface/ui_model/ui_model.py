from ..event_listening.listener import Listener


class UIModel(object):

    CLICK_LISTEN_FLAG = 'click_listen'
    MOVEMENT_LISTEN_FLAG = 'movement_listen'

    def __init__(self, ui_control, element_id, *args, **kwargs):

        self.ui_control = ui_control
        self.element_id = element_id

        self.click_listener = self._init_click_listener(**kwargs)
        self.movement_listener = self._init_movement_listener(**kwargs)

    def _init_click_listener(self, **kwargs):

        if kwargs.get(UIModel.CLICK_LISTEN_FLAG, False):
            listener = Listener(self.on_any_click)
            listener.subscribe(self.ui_control.model_manager.click_broadcaster)
            return listener
        else:
            return None

    def _init_movement_listener(self, **kwargs):

        if kwargs.get(UIModel.MOVEMENT_LISTEN_FLAG, False):
            listener = Listener(self.on_movement)
            listener.subscribe(self.ui_control.model_manager.movement_broadcaster)
            return listener
        else:
            return None

    def on_left_click(self):
        print ''.join((self.element_id, ' model left clicked'))

    def on_right_click(self):
        print ''.join((self.element_id, ' model right clicked'))

    def on_hover_start(self):
        """ Behaviour for when mouse starts to hover over this element. """
        pass

    def on_any_click(self):
        """ Called by the click listener when ui control broadcasts any click event """
        pass

    def on_movement(self):
        """ Called by the move listener when ui control broadcasts any mouse movement"""
        pass

    def get_node(self):
        return self.ui_control.find_node(self.element_id)

    def close_node(self):

        self.get_node().strand_node()

    def close_model(self):

        self.ui_control.remove_ui_model(self.element_id)
