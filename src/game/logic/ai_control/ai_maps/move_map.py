

class MoveMap(object):

    def __init__(self, logic):
        self.logic = logic
        self.map = logic.game.map

        self._map = {}

    def init(self):
        for foe in self.logic.foes():
            self._map[foe] = foe.pos

    def clear(self):
        self._map.clear()

    def available_moves(self, moves):
        blocked = set(self._map.values())
        return filter(lambda m: m not in blocked, moves)

    def move(self, actor, pos):
        del self._map[actor]
        self._map[actor] = pos
