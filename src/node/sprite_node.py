from stellarlib.node import Node


class SpriteNode(Node):

    def __init__(self, parent, sprite):

        Node.__init__(self, parent)
        self.sprite = sprite
        self.add_component(sprite)
