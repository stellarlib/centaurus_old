from stellarlib.animation import Lerp, QuadraticHop
from src.settings import PIXEL_SCALE
import math


class ArcAnimation(Lerp):

    MOVE_SPEED = 2.0 * PIXEL_SCALE

    def __init__(self, actor, proj_node, destination, height, resolve_func):

        start = actor.node.screen_pos()
        time = self.calculate_move_time(start, destination)
        Lerp.__init__(self, proj_node, start, destination, time, snap=True)
        self.resolve_func = resolve_func

        # add hop
        QuadraticHop(proj_node, height * PIXEL_SCALE, time)

    def on_complete(self):
        self.resolve_func()

    def calculate_move_time(self, (sx, sy), (dx, dy)):

        x = abs(dx - sx)
        y = abs(dy - sy)

        dist = math.hypot(x, y)

        return int(round(dist / self.MOVE_SPEED))
