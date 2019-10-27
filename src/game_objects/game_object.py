from src.sprite import SpriteComponent
from src.node import SpriteNode, GameObjectNode
from src.map import hex_to_pixel, Hex
from src.settings import PIXEL_SCALE


class GameObject(object):

    ACTOR_OFFSET = PIXEL_SCALE * 5

    def __init__(self, game, name, pos):

        self.game = game
        self.name = name
        self.pos = pos
        self.node = None

        self.dead = False

    @property
    def alive(self):
        return not self.dead

    def init(self, parent):
        self.create_node(parent)

    def create_node(self, parent):
        self.node = GameObjectNode(parent, self._get_screen_pos(), self.game)
        self.node.load_sprite(SpriteNode(self.node, SpriteComponent(self.name)))

    def _get_screen_pos(self):
        return self._get_hex_pos(self.pos)

    def _get_hex_pos(self, pos):
        px, py = hex_to_pixel(self.game.hex_layout, Hex(*pos))
        py -= GameObject.ACTOR_OFFSET
        return px, py

    # API
    def place(self, pos):
        self.pos = pos
        self.node.set_pos(self._get_screen_pos())

    def move(self, pos):
        self.place(pos)

    def die(self):
        self.dead = True
        self.game.logic.kill_actor(self)
        self.on_death()

    def hit(self, n):
        self.die()

    def melee_attack(self, foe):
        foe.hit(1)

    def range_attack(self, foe):
        foe.hit(2)

    def on_death(self):
        pass

    def will_die(self, n):
        return True
