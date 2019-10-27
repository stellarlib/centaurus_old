from stellarlib.node import Node
from stellarlib.user_interface._ui_components import ClickBox


class UINode(Node):

    def __init__(self, element_id, parent, pos, w, h, model=None):

        self.element_id = element_id
        self.model = model
        Node.__init__(self, parent, pos)
        self.click_box = ClickBox(self, w, h)
        self._hidden = False

    @property
    def hidden(self):
        return self._hidden

    def assign_node_type(self):
        return Node.ui

    def touch(self, mouse_pos):

        if not self.hidden:
            if self.click_box.mouse_is_over(mouse_pos):

                for node in self.children:
                    touched = node.touch(mouse_pos)
                    if touched:
                        return touched

                return self.element_id

        return None

    def get_root_ui(self):

        if self.element_id == 'root_ui':
            return self
        else:
            return self.parent.get_root_ui()

    def find_node(self, element_id):

        if element_id == self.element_id:
            return self
        else:
            for child in self.children:
                child_find = child.find_node(element_id)
                if child_find is not None:
                    return child_find
            return None

    # TODO hide and reveal entire UINode
    # don't draw or allow touch when hidden

    def hide(self):
        self._hidden = True

    def show(self):
        self._hidden = False

    # TODO This is bad - find alternative to overwriting here
    def update(self):

        if not self.hidden:

            # update transform
            self.transform.update()

            # update components
            map(lambda c: c.update(), self.components)

            # update all children
            map(lambda n: n.update(), self.children)

    def draw_onto(self, dest_node):

        if not self.hidden:

            # draw this node's components
            rel_pos = self.transform.relative_pos(dest_node)
            map(lambda c: c.draw(dest_node.display_surface, rel_pos), self.components)

            # draw all children onto destination surface
            map(lambda n: n.draw_onto(dest_node), self.children)
