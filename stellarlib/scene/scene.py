import pygame
from pygame.locals import *
import stellarlib.settings as settings
from stellarlib.scene_tree import SceneTree
from stellarlib.node import EffectsNode, Node
from stellarlib.user_interface import RootUINode, UIControl
from stellarlib.messaging import MessageCenter
from stellarlib.mouse import Mouse
from stellarlib.console import Console


class Scene(object):

    FPS = settings.FPS

    def __init__(self, app):

        self.app = app
        self.message_center = MessageCenter.get_instance()

        self.exit_trigger = False
        self.clock = pygame.time.Clock()
        self.mouse = self.load_mouse()
        self.console = self.load_console()

        self.ui_control = self.load_ui_control()

        self.scene_tree = None
        self.effects_node = None
        self.ui_root_node = None
        self.console_node = None

    @property
    def running(self):
        return not self.exit_trigger

    def initialize(self):

        self.message_center.bind_scene(self)
        self.initialize_scene_tree()
        self.on_start()

    def load_mouse(self):
        return Mouse(self)

    def load_console(self):
        return Console()

    def load_ui_control(self):
        return UIControl(self)

    def on_start(self):
        pass

    def on_complete(self):
        print 'scene_complete'
        pass

    def initialize_scene_tree(self):
        self.scene_tree = SceneTree(self, self._get_screen_dim())
        screen = self.scene_tree.screen_node
        # game_objects first
        self.populate_scene_tree(screen)
        self.effects_node = EffectsNode(screen, (0, 0))
        self.ui_root_node = RootUINode(screen)
        self.console_node = Node(screen, (0, 0))
        self.console_node.add_component(self.console)

        self.ui_control.bind(self.ui_root_node)

    def populate_scene_tree(self, screen):
        pass

    def _get_screen_dim(self):
        return settings.SCREEN_W, settings.SCREEN_H

    def main(self):

        self.initialize()

        while self.running:

            self.handle_input()
            self.update()
            self.draw_display()
            self.tick_frame()
            self.refresh_display()
            # if self.clock.get_fps() < 55:
            #     print self.clock.get_fps()

        self.on_complete()

        return True

    def tick_frame(self):
        self.clock.tick(Scene.FPS)

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

            else:
                self.mouse.handle_input(event)

            self.console.handle_input(event)

    def draw_display(self):

        self.scene_tree.draw()

    def refresh_display(self):

        pygame.display.update()

    def update(self):

        self.scene_tree.update()
        self.mouse.update()
        self.on_update()

    def on_update(self):
        pass

    def screen_shot(self):

        print 'screen shot'
        screen = self.scene_tree.screen_surface
        pygame.image.save(screen, 'screenshot.png')

    def get_next_scene(self):
        return 'exit'

    def toggle_console(self):

        if self.console.shown:
            self.console.hide()
        else:
            self.console.show()
