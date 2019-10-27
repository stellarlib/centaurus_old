from stellarlib.hex_tool import hex_to_pixel, Hex
from src.icon import IconSprite
from src.color import Color


class MarkDrawer(object):

    FLASH_RATE = 6
    A = 0
    B = 1

    def __init__(self, logic):
        self.logic = logic
        self._marks = []
        self.tick = 0
        self.state = MarkDrawer.A

        self.icons = self.init_icons()

    def init_icons(self):

        icons = {
            MarkDrawer.A: IconSprite('target'),
            MarkDrawer.B: IconSprite('target')
        }

        icons[MarkDrawer.B].replace_color(Color.RED, Color.WHITE)

        return icons

    def init(self):
        self.logic.game.overlay.add_component(self)

    @property
    def mark_map(self):
        return self.logic.ai_control.unit_control.mark_map

    def update(self):
        self.tick += 1
        if self.tick == MarkDrawer.FLASH_RATE:
            self.tick = 0
            self.flash()

    def flash(self):
        if self.state == MarkDrawer.A:
            self.state = MarkDrawer.B
        else:
            self.state = MarkDrawer.A

    def update_marks(self):
        del self._marks[:]
        self._marks.extend(self.mark_map._map)

    def draw(self, display_surface, rel_pos):

        for pos in self._marks:
            self.draw_mark(display_surface.surface, rel_pos, pos)

    def draw_mark(self, surface, (rx, ry), pos):

        px, py = hex_to_pixel(self.logic.game.hex_layout, Hex(*pos))

        x = rx + px
        y = ry + py

        icon = self.icons[self.state]
        icon.draw(surface, (x, y))
