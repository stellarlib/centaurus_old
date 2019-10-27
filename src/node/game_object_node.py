from stellarlib.node import Node
from stellarlib.hex_tool import pixel_to_hex, Hex
from src.map.tile import Tile


class GameObjectNode(Node):

    def __init__(self, parent, pos, game):

        Node.__init__(self, parent, pos)
        self.game = game
        self.sprite = None

    def load_sprite(self, sprite_node):
        self.sprite = sprite_node

    def draw_onto(self, dest_node):

        # draw this node's components
        rel_pos = self.transform.relative_pos(dest_node)
        map(lambda c: c.draw(dest_node.display_surface, rel_pos), self.components)

        # draw all children onto destination surface
        map(lambda n: n.draw_onto(dest_node), self.children)

        self.draw_overlapping_trees(dest_node.display_surface.surface)

    def draw_overlapping_trees(self, surface):

        hex = pixel_to_hex(self.game.hex_layout, self.screen_pos())

        bl = Hex.hex_neighbour(hex, 4)
        br = Hex.hex_neighbour(hex, 5)

        for h in (bl, br):

            if self.game.map.get_tile((h.x, h.y)) == Tile.WOODS:
                self.game.map_image.image.draw_overlap_trees(surface, h)

    def set_pos(self, (x, y)):
        self.transform.base_position.set(x, y)
