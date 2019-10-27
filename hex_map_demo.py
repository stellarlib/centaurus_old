from src.game import Game
from stellarlib.app import App
from pygame.locals import *
import pygame

from stellarlib.node import Node
from stellarlib.hex_tool import *

from random import randint
import os, sys


class HexTile(object):

    images = None
    rect = None

    tiles = {
        0: 'grass',
        1: 'clay',
        2: 'woods',
        3: 'stones',
        4: 'sand',
        5: 'wall',
        6: 'road',
        7: 'water'
    }

    @classmethod
    def init(cls):

        cls.images = {k: img for k, img in [(k, cls.init_tile(cls.tiles[k])) for k in range(8)]}
        cls.rect = cls.images[0].get_rect()

    @classmethod
    def init_tile(cls, tile):
        img = pygame.image.load(os.path.join('assets', 'hex', tile + '.png'))
        img = pygame.transform.scale(img, (40, 40))
        img = img.convert()
        img.set_colorkey((255, 255, 255))

        return img

    def __init__(self, i):
        if HexTile.images is None:
            HexTile.init()
        self.i = i

    def update(self):
        pass

    def draw(self, display_surface, rel_pos):

        HexTile.rect.center = rel_pos
        display_surface.surface.blit(HexTile.images[self.i], HexTile.rect)



class Demo(Game):

    def __init__(self, app):

        Game.__init__(self, app)
        SIZE = 12 * 2
        self.hex_layout = Layout(pointy_layout, Point(SIZE+1, SIZE), Point(250, 250))

    def on_start(self):

        screen = self.scene_tree.screen_node

        radius = 5
        for x in range(-radius, radius+1):

            y1 = max(-radius, -x-radius)
            y2 = min(radius, -x+radius)
            for y in range(y1, y2+1):
                self.make_hex_node(x, y, screen)

    def make_hex_node(self, ix, iy, screen):

        x, y = hex_to_pixel(self.hex_layout, Hex(ix, iy))
        n = Node(screen, (x, y))
        n.add_component(HexTile(randint(0, 7)))

    def handle_input(self):

        for event in pygame.event.get():
            if event.type == QUIT:
                self.exit_trigger = True

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.exit_trigger = True

                elif event.key == K_SLASH:
                    self.screen_shot()

                elif event.key == K_BACKQUOTE:
                    self.toggle_console()

            elif event.type == MOUSEBUTTONDOWN:
                self.print_hex(pygame.mouse.get_pos())

            else:
                self.mouse.handle_input(event)

            self.console.handle_input(event)

    def print_hex(self, (mx, my)):

        hex = pixel_to_hex(self.hex_layout, (mx, my))
        print hex.x, hex.y


if __name__ == '__main__':

    app = App()
    app.initialize()
    demo = Demo(app)

    app.current_scene = demo
    app.main()
    sys.exit()
