from stellarlib.transform import Transform
from transform_dot import TransformDot


class Node(object):

    base = 0
    display = 1
    ui = 2

    def __init__(self, parent, pos=(0, 0)):

        self.parent = parent
        if self.parent:
            self.parent.add_child(self)
        self.children = []

        self.node_type = self.assign_node_type()
        self.display_surface = None

        self.transform = Transform(self, pos)

        self.components = []

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def strand_node(self):
        """ Call to take node and all children out of the Scene Tree """
        self.parent.remove_child(self)

    def add_component(self, component):
        self.components.append(component)

    def remove_component(self, component):
        self.components.remove(component)

    def add_components(self, components):
        map(lambda c: self.add_component(c), components)

    def assign_node_type(self):
        return Node.base

    def local_pos(self):
        return self.transform.local_pos()

    def screen_pos(self):
        return self.transform.screen_pos()

    def relative_pos(self, node):
        return self.transform.relative_pos(node)

    def node_is_parent(self, node):

        if self.parent is None:
            return False
        elif node is self.parent:
            return True
        else:
            return self.parent.node_is_parent(node)

    def update(self):

        # update transform
        self.transform.update()

        # update components
        map(lambda c: c.update(), self.components)

        # update all children
        map(lambda n: n.update(), self.children)

    def draw_onto(self, dest_node):

        # draw this node's components
        rel_pos = self.transform.relative_pos(dest_node)
        map(lambda c: c.draw(dest_node.display_surface, rel_pos), self.components)

        # draw all children onto destination surface
        map(lambda n: n.draw_onto(dest_node), self.children)

    @property
    def destination_surface(self):

        if self.parent is None:
            return self.display_surface
        elif self.parent.node_type == Node.display:
            return self.parent.display_surface
        else:
            return self.parent.destination_surface

    def show_dot(self):
        self.components.append(TransformDot(self))
