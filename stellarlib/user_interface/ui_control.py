from ui_node_manager import UINodeManager
from ui_model_manager import UIModelManager
from ui_element_factory import UIElementFactory


class UIControl(object):

    def __init__(self, scene):
        self.scene = scene
        self.node_manager = UINodeManager(self)
        self.model_manager = UIModelManager(self)
        self.element_factory = UIElementFactory(self)

    def bind(self, root_node):
        self.node_manager.bind(root_node)

    def mouse_motion(self):
        # broadcast a mouse motion event
        # close tool tip panels
        # slide draggable elements
        self.model_manager.broadcast_movement()

    def mouse_clicked(self):
        # broadcast a general click event
        # close one click panels
        self.model_manager.broadcast_click()

    def left_click(self, mouse_pos):

        clicked_el_id = self.node_manager.touch_ui(mouse_pos)  # returns element id of highest level clicked element view

        clicked_model = self.model_manager.get_model(clicked_el_id)
        if clicked_model is not None:
            clicked_model.on_left_click()

        self.mouse_clicked()  # broadcast a click event for clearing pop ups etc.

        return clicked_el_id is not None  # inform mouse object that ui blocked click or not

    def right_click(self, mouse_pos):

        clicked_el_id = self.node_manager.touch_ui(mouse_pos)  # returns element id of highest level clicked element view

        clicked_model = self.model_manager.get_model(clicked_el_id)
        if clicked_model is not None:
            clicked_model.on_right_click()

        self.mouse_clicked()  # broadcast a click event for clearing pop ups etc.

        return clicked_el_id is not None  # inform mouse object that ui blocked click or not

    def mouse_hover_start(self, mouse_pos):

        focused_el_id = self.node_manager.touch_ui(mouse_pos)

        touched_model = self.model_manager.get_model(focused_el_id)
        if touched_model is not None:
            touched_model.on_hover_start()

        # TODO if I want hovering over the battlescape to be blocked by UI elements, insert here

    def find_node(self, element_id):
        """ Returns ui node with matching element id if it exists in hierarchy. Otherwise returns None. """
        return self.node_manager.find_node(element_id)

    def make_ui_model(self, constructor, element_id, *args, **kwargs):

        model = constructor(self, element_id, *args, **kwargs)
        self.model_manager.add_model(model)

    def remove_ui_model(self, element_id):

        self.model_manager.remove_model(element_id)
