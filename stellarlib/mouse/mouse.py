import pygame
from pygame.locals import *


class Mouse(object):

    LEFT = 1
    RIGHT = 3

    HOVER_DELAY = 30

    def __init__(self, scene):

        self.scene = scene
        self.hover_tick = 0
        self.hovering = False
        self.moved = False

    def update(self):

        if self.moved:
            self._cancel_hover()
        elif self.hovering:
            self._continue_hover()
        else:
            self.hover_tick += 1
            if self.hover_tick > Mouse.HOVER_DELAY:
                self._start_hover()

        self.moved = False
        self.on_update()

    def handle_input(self, event):

        if event.type == MOUSEBUTTONDOWN:
            if event.button == Mouse.LEFT:
                self.left_mouse_button_down()
            elif event.button == Mouse.RIGHT:
                self.right_mouse_button_down()

        elif event.type == MOUSEBUTTONUP:
            if event.button == Mouse.LEFT:
                self.left_mouse_button_up()
            elif event.button == Mouse.RIGHT:
                self.right_mouse_button_up()

        elif event.type == MOUSEMOTION:
            self.moved = True
            self.mouse_motion()

    def left_mouse_button_down(self):
        pass

    def right_mouse_button_down(self):
        pass

    def left_mouse_button_up(self):
        pass

    def right_mouse_button_up(self):
        pass

    def mouse_motion(self):
        pass

    def start_hover(self):
        pass

    def continue_hover(self):
        pass

    def end_hover(self):
        pass

    def _start_hover(self):
        self.hovering = True
        self.start_hover()

    def _continue_hover(self):
        self.continue_hover()

    def _cancel_hover(self):

        self.hover_tick = 0
        if self.hovering:
            self.hovering = False

        self.end_hover()

    def on_update(self):
        pass
