from stellarlib.hex_tool import Hex
from src.map import Tile


class StandardControl(object):

    def __init__(self, control):

        self.control = control

    def handle_click(self, pos):

        if pos == self.control.player.pos:
            pass
        elif self.is_adj(pos, self.control.player):
            if self.control.logic.occupied(pos):
                self.control.player_attacks(pos)
            elif self.is_passable(pos):
                self.control.move_player(pos)

    def is_adj(self, pos, actor):
        a = Hex(*pos)
        b = Hex(*actor.pos)
        return Hex.hex_distance(a, b) == 1

    def is_passable(self, pos):
        on_map = self.control.game.map.on_map(pos)
        tile = self.control.game.map.get_tile(pos)
        passable = Tile.is_passable(tile)
        return on_map and passable
