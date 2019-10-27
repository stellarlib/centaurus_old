

class UINodeManager(object):

    def __init__(self, ui_control):

        self.ui_control = ui_control
        self.ui_root_node = None

    def bind(self, root_node):
        self.ui_root_node = root_node
        root_node.ui_control = self.ui_control

    def touch_ui(self, mouse_pos):

        return self.ui_root_node.touch(mouse_pos)

    def find_node(self, element_id):

        return self.ui_root_node.find_node(element_id)
