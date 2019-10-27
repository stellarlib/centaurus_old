from random import randint


class Tile(object):

    n = 8

    GRASS, WOODS, WATER, ROCKS, SAND, CLAY, ROAD, WALL = range(n)

    IMPASSABLE = {WALL, WATER}

    @classmethod
    def random_tile(cls):
        return randint(0, cls.n-1)

    @classmethod
    def is_passable(cls, t):
        return t not in cls.IMPASSABLE
