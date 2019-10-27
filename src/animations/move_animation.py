from stellarlib.animation import Lerp, QuadraticHop
from src.settings import PIXEL_SCALE
import math


class MoveAnimation(Lerp):

    MOVE_SPEED = 1.6 * PIXEL_SCALE

    def __init__(self, actor, destination, height, resolve_func):

        start = actor.node.screen_pos()
        time = self.calculate_move_time(start, destination)
        Lerp.__init__(self, actor.node, start, destination, time, snap=True)
        self.resolve_func = resolve_func

        # add hop
        QuadraticHop(actor.node.sprite, height * PIXEL_SCALE, time)

    def on_complete(self):
        self.resolve_func()

    def calculate_move_time(self, (sx, sy), (dx, dy)):

        x = abs(dx - sx)
        y = abs(dy - sy)

        dist = math.hypot(x, y)

        return int(round(dist / self.MOVE_SPEED))
