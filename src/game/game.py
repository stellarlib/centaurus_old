from stellarlib.scene import Scene
from stellarlib.node import Node
from src.map.map_node import MapNode
from src.node import OrderedDrawNode
from src.tile.tile_dict import init_tiles
from src.map import init_hex_layout, HexMap, make_hex, Tile
from logic import Logic
from mouse import Mouse
import pygame
from pygame.locals import *
from src.settings import SCREEN_W, SCREEN_H


class Game(Scene):

    def __init__(self, app):

        Scene.__init__(self, app)
        self.hex_layout = None
        self.map = HexMap()
        self.map_image = None
        self.game_objects = None
        self.overlay = None

        self.logic = Logic(self)

    def load_mouse(self):
        return Mouse(self)

    def on_start(self):
        init_tiles()
        self.hex_layout = init_hex_layout()
        self.init_map()
        self.logic.init()

    def init_map(self):

        from random import randint
        for coord in make_hex(4):

            t = Tile.WOODS
            if randint(0, 1) == 0:
                t = Tile.GRASS
            elif randint(0, 5) == 0:
                t = Tile.WALL

            self.map.add_tile(coord, t)

        self.map_image.init_map_image()

    def populate_scene_tree(self, screen):

        self.map_image = MapNode(screen, self)
        self.game_objects = OrderedDrawNode(self.map_image)
        self.overlay = Node(self.map_image)

    def _get_screen_dim(self):
        return SCREEN_W, SCREEN_H

    def on_update(self):
        self.logic.update()

    def handle_input(self):

        for event in pygame.event.get():
            if event.type == QUIT:
                self.exit_trigger = True

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.exit_trigger = True

                elif event.key == K_SLASH:
                    self.screen_shot()

                # elif event.key == K_BACKQUOTE:
                #     self.toggle_console()

                # shortcut keys
                elif event.key == K_SPACE:
                    self.logic.player_control.manual_turn_end()
                elif event.key == K_z:
                    self.logic.player_control.manual_switch_mode('throw')
                elif event.key == K_x:
                    self.logic.player_control.manual_switch_mode('jump')
                elif event.key == K_c:
                    self.logic.player_control.manual_switch_mode('charge')

                elif event.key == K_BACKQUOTE:
                    print 'break'

            else:
                self.mouse.handle_input(event)

            self.console.handle_input(event)
