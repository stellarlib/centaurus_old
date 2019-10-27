from stellarlib.node import Node
from src.animations import ArcAnimation
from src.settings import PIXEL_SCALE
from components.arrow_component import ArrowComponent


class ProjectileNode(Node):

    def __init__(self, actor, target_pos, on_hit):

        origin = actor._get_screen_pos()

        Node.__init__(self, actor.game.game_objects, origin)
        on_hit = self.get_hit_func(on_hit)
        ArcAnimation(actor, self, target_pos, self.get_peak(origin, target_pos), on_hit)

        self.sprite = ArrowComponent(self)
        self.add_component(self.sprite)

    def get_hit_func(self, on_hit):

        def resolve():
            on_hit()
            self.strand_node()

        return resolve

    def get_peak(self, origin, dest):

        return PIXEL_SCALE * 5
