

class HexMap(object):

    def __init__(self):

        self._map = {}

    def get_tile(self, coord):
        return self._map.get(coord)

    def add_tile(self, coord, tile):
        self._map[coord] = tile

    def on_map(self, coord):
        return coord in self._map

    def all_points(self):
        for point in self._map.iterkeys():
            yield point

    def all_of_tile(self, tile):
        return filter(lambda t: self.get_tile(t) == tile, self.all_points())

    def all_except(self, not_tile):
        return filter(lambda t: self.get_tile(t) != not_tile, self.all_points())
