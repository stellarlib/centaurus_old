from stellarlib.group import Group
from node import Node


class EffectsNode(Node):

    def __init__(self, parent, pos):

        Node.__init__(self, parent, pos)
        self.effects = Group()
        self.add_component(self.effects)
