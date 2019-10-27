from src.map import Tile, hex_to_pixel, Hex
from src.tile import get_tile_image
from src.settings import MAP_W, MAP_H, TREE_POSITIONS, PIXEL_SCALE
import pygame
from src.color import Color
from src.sprite import TreeSprite


class MapImage(object):

    def __init__(self, game):

        self.game = game
        self.map = self.game.map
        self.surface = self.init_surface()

        self.tree_sprite = TreeSprite()

    def init_surface(self):

        surface = pygame.Surface((MAP_W, MAP_H)).convert()
        surface.fill(Color.BLACK)

        return surface

    def init_map_image(self):
        self._draw_tiles()
        self._draw_trees()

    def _draw_tiles(self):
        for point in self.map.all_points():
            self._draw_tile(point)

    def _draw_trees(self):

        points = self.map.all_of_tile(Tile.WOODS)
        points.sort(key=lambda p: p[0], reverse=True)
        for point in points:
            self._draw_tree(point)

    def _draw_tile(self, hex_coord):

        tile_image = get_tile_image(self.map.get_tile(hex_coord))
        pixel_coord = hex_to_pixel(self.game.hex_layout, Hex(*hex_coord))
        tile_image.draw(self.surface, pixel_coord)

    def _draw_tree(self, hex_coord):

        px, py = hex_to_pixel(self.game.hex_layout, Hex(*hex_coord))
        for tx, ty in TREE_POSITIONS:
            self.tree_sprite.draw(self.surface, (px + tx, py + ty))

    def draw(self, display_surface, rel_pos):
        display_surface.surface.blit(self.surface, rel_pos)

    def update(self):
        pass

    def draw_overlap_trees(self, surface, hex):

        px, py = hex_to_pixel(self.game.hex_layout, hex)
        for tx, ty in TREE_POSITIONS:
            self.tree_sprite.draw(surface, (px + tx, py + ty))
