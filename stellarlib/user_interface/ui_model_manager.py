from event_listening.broadcaster import Broadcaster


class UIModelManager(object):

    def __init__(self, ui_control):

        self.ui_control = ui_control
        self.click_broadcaster = Broadcaster()
        self.movement_broadcaster = Broadcaster()
        self.models = {}

    def broadcast_movement(self):
        self.movement_broadcaster.broadcast()

    def broadcast_click(self):
        self.click_broadcaster.broadcast()

    def add_model(self, model):

        element_id = model.element_id
        self.models[element_id] = model

    def get_model(self, element_id):

        return self.models.get(element_id, None)

    def remove_model(self, element_id):

        model = self.models[element_id]
        if model.click_listener:
            model.click_listener.unsubscribe()
        if model.movement_listener:
            model.movement_listener.unsubscribe()
        del self.models[element_id]
