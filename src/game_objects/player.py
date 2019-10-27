from game_object import GameObject
from src.node import SpriteNode, GameObjectNode
from src.sprite import SpriteComponent
from stellarlib.node import Node
from player_overlay import PlayerOverlay
from src.settings import PIXEL_SCALE
from src.animations import MoveAnimation


class Player(GameObject):

    ACTIONS = 3
    overlay_pos = (PIXEL_SCALE * 15, PIXEL_SCALE * 15)

    def __init__(self, game, pos):

        GameObject.__init__(self, game, 'player', pos)

        self.actions = Player.ACTIONS
        self.max_actions = Player.ACTIONS

        self.hop = 8

        self.player_overlay = PlayerOverlay(self)

    def create_node(self, parent):
        self.node = GameObjectNode(parent, self._get_screen_pos(), self.game)
        self.node.load_sprite(SpriteNode(self.node, SpriteComponent('centaur')))
        self.create_icon_overlay()

    def create_icon_overlay(self):

        overlay = Node(self.game.overlay, Player.overlay_pos)
        overlay.add_component(self.player_overlay)

    def spend_actions(self, x):
        self.actions -= x
        self.player_overlay.update_icons()

    def restore(self, x):
        self.actions += x
        self.actions = min((self.max_actions, self.actions))
        self.player_overlay.update_icons()

    def die(self):
        self.dead = True
        self.game.logic.kill_actor(self)
        print 'game over'

    def start_move(self, pos, resolve_func):

        def move_resolve():
            resolve_func()
            self.move(pos)

        MoveAnimation(self, self._get_hex_pos(pos), self.hop, move_resolve)
