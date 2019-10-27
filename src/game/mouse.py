import stellarlib.mouse
from src.map import pixel_to_hex
import pygame


class Mouse(stellarlib.mouse.Mouse):

    def left_mouse_button_down(self):

        hex_coord = pixel_to_hex(self.scene.hex_layout, pygame.mouse.get_pos())

        self.scene.logic.player_control.handle_click(hex_coord.to_tuple())
