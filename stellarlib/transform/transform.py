from stellarlib.vector import Vector
from stellarlib.animation import AnimationGroup


class Transform(object):

    def __init__(self, node, (x, y)):

        self.node = node
        self.base_position = Vector(x, y)
        self.position = Vector(x, y)

        self.animations = AnimationGroup()

    def update(self):

        # run all animations
        self.animations.update()

        self.calculate_current_position()

    def calculate_current_position(self):

        # make permanent changes to transform vector
        self.animations.update_base_vector(self.base_position)

        # reset position to base position
        self.position.match(self.base_position)

        # make temporary changes
        self.animations.update_position_vector(self.position)

    # return tuple of position relative to parent node
    def local_pos(self):

        return self.position.get_tuple_int()

    # return tuple of position relative to screen
    def screen_pos(self):

        if self.node.parent:
            return self.position.get_add_tuple(self.node.parent.transform.screen_pos_vector(), integer=True)
        else:
            return self.position.get_tuple_int()

    # return tuple of position relative to node in parent hierarchy
    def relative_pos(self, node):

        if node is self.node:
            return self.local_pos()

        if not self.node.node_is_parent(node):
            raise ValueError(self.__str__() + ' has no relative position to ' + node.__str__())

        if node is self.node.parent:
            return self.position.get_tuple_int()
        else:
            return self.position.get_add_tuple(self.node.parent.transform.relative_pos_vector(node), integer=True)

    # recursive methods to search hierarchy - return Vectors instead of tuples for better addition
    def screen_pos_vector(self):

        if self.node.parent:
            return Vector(self.position.get_add_tuple(self.node.parent.transform.screen_pos_vector()))
        else:
            return Vector(self.position.get_tuple_int())

    def relative_pos_vector(self, node):

        if node is self.node.parent:
            return Vector(self.position.get_tuple_int())
        else:
            return Vector(self.position.get_add_tuple(self.node.parent.transform.screen_pos_vector()))
