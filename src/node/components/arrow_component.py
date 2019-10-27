from stellarlib import Vector
import pygame
from src.color import Color
from src.settings import PIXEL_SCALE


class ArrowComponent(object):

    ARROW_LEN = PIXEL_SCALE * 6

    def __init__(self, node):

        self.node = node
        self.last_pos = Vector()
        self.current_pos = Vector()
        self.tail = None

    def update(self):
        self.last_pos.match(self.current_pos)
        self.current_pos.set(*self.node.screen_pos())
        self.update_tail()

    def draw(self, display_surface, rel_pos):

        if self.tail:
            self.draw_arrow(display_surface.surface)

    def update_tail(self):

        tail = Vector()
        tail.match(self.current_pos)
        tail.sub(self.last_pos)
        if tail.x == 0.0 and tail.y == 0.0:
            self.tail = None
        else:
            self.tail = tail.get_unit_vector()
            self.tail.mult(ArrowComponent.ARROW_LEN)
            self.tail.add(self.current_pos)

    def draw_arrow(self, surface):

        sx, sy = self.current_pos.get_tuple_int()
        ex, ey = self.tail.get_tuple_int()

        pygame.draw.line(surface, Color.PURE_WHITE, (sx, sy), (ex, ey), PIXEL_SCALE)
