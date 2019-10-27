import pygame
from node import Node
from screen_display import ScreenDisplaySurface
from display_surface import DisplaySurface
from stellarlib.color import Color


class Display(Node):

    def __init__(self, parent, pos, w, h, color=Color.BLACK, refresh=True):

        Node.__init__(self, parent, pos)

        self.w = w
        self.h = h
        self.color = color

        self.display_surface = self.init_display_surface(color, refresh)

    def assign_node_type(self):
        return Node.display

    def init_display_surface(self, color, refresh):

        if self.parent is None:
            ScreenDisplaySurface.instantiate_display(self.w, self.h)
            return ScreenDisplaySurface.get_display_surface()

        else:
            return DisplaySurface(self.w, self.h, color, refresh)

    def update(self):

        self.transform.update()
        self.display_surface.update()

        # update all children
        map(lambda n: n.update(), self.children)

    def draw_onto(self, dest_node):

        # draw this node's components
        map(lambda c: c.draw(self.display_surface, (0, 0)), self.components)

        # draw children onto this display
        map(lambda n: n.draw_onto(self), self.children)

        # blit this display onto our destination node
        rel_pos = self.transform.relative_pos(dest_node)
        dest_node.blit(self.display_surface, rel_pos)

    def blit(self, display_surface, pos):

        self.display_surface.blit(display_surface.surface, pos)

    def render_to_screen(self):

        # blit the screen display onto the pygame display surface
        pygame.display.get_surface().blit(self.display_surface.surface, (0, 0))
