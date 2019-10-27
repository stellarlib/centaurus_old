from stellarlib.node import Node


class OrderedDrawNode(Node):

    def __init__(self, parent, pos=(0, 0)):

        Node.__init__(self, parent, pos)

    def draw_onto(self, dest_node):

        self.order_children()

        # draw this node's components
        rel_pos = self.transform.relative_pos(dest_node)
        map(lambda c: c.draw(dest_node.display_surface, rel_pos), self.components)

        # draw all children onto destination surface
        map(lambda n: n.draw_onto(dest_node), self.children)

    def order_children(self):
        self.children.sort(key=lambda c: c.local_pos()[1])
