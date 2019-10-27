from map_image import MapImage
from stellarlib.node import Node


class MapNode(Node):

    def __init__(self, parent, map):

        Node.__init__(self, parent)
        self.image = MapImage(map)
        self.add_component(self.image)

    def init_map_image(self):
        self.image.init_map_image()

