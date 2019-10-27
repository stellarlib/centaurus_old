# hex_tool module adapted from code from redblobgames.com
# by Amit Patel
# available under MIT License or Apace according to homepage

from hex import Hex
from fractional_hex import FractionalHex
from layout import Layout
from orientation import pointy_layout, flat_layout
from point import Point


def hex_to_pixel(layout, hex):

    M = layout.orientation
    x = (M.f0 * hex.x + M.f1 * hex.y) * layout.size.x
    y = (M.f2 * hex.x + M.f3 * hex.y) * layout.size.y

    return int(x + layout.origin.x), int(y + layout.origin.y)


def pixel_to_hex(layout, (px, py)):

    M = layout.orientation
    pt = Point((px - layout.origin.x) / float(layout.size.x),
               (py - layout.origin.y) / float(layout.size.y))
    x = M.b0 * pt.x + M.b1 * pt.y
    y = M.b2 * pt.x + M.b3 * pt.y

    return FractionalHex(x, y, -x-y).hex_round()
