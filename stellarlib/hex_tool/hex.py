# hex_tool module adapted from code from redblobgames.com
# by Amit Patel
# available under MIT License or Apace according to homepage


class Hex(object):

    def __init__(self, x, y):

        self.x = int(x)
        self.y = int(y)
        self.z = -x -y

    def __eq__(self, hex):
        return self.x == hex.x and self.y == hex.y and self.z == hex.z

    def __ne__(self, hex):
        return not self == hex

    def to_tuple(self):
        return self.x, self.y

    @staticmethod
    def hex_add(a, b):
        return Hex(a.x + b.x, a.y + b.y)

    @staticmethod
    def hex_sub(a, b):
        return Hex(a.x - b.x, a.y - b.y)

    @staticmethod
    def hex_mult(a, scalar):
        return Hex(a.x * scalar, a.y * scalar)

    @staticmethod
    def hex_length(hex):
        return int((abs(hex.x) + abs(hex.y) + abs(hex.z)) / 2.0)

    @staticmethod
    def hex_distance(a, b):
        return Hex.hex_length(Hex.hex_sub(a, b))

    @staticmethod
    def hex_direction(d):

        if 0 <= d < 6:
            ValueError('hex directions are 0 - 5')

        return hex_directions[d]

    @staticmethod
    def hex_neighbour(hex, d):

        return Hex.hex_add(hex, Hex.hex_direction(d))

    @staticmethod
    def get_hex_neighbours(hex):
        neighbours = []
        for d in range(6):
            neighbours.append(Hex.hex_neighbour(hex, d))
        return neighbours


hex_directions = Hex(1, 0),  Hex(1, -1), Hex(0, -1), Hex(-1, 0), Hex(-1, 1), Hex(0, 1)
