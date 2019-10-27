from tile import Tile
from hex_map import HexMap
from stellarlib.hex_tool import *
from src.settings import TILE_SIZE, HEX_ORIGIN
from shape import make_hex


def init_hex_layout():

    return Layout(pointy_layout, Point(*TILE_SIZE), Point(*HEX_ORIGIN))
