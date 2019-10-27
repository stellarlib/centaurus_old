from image import Image
from stellarlib.color import Color


class ShipImage(Image):

    def __init__(self, image):

        Image.__init__(self)

        self.surface = image.surface.copy()
        self.preprocess_image()
        self.init_image(self.surface, scaled_up=True)

    def preprocess_image(self):

        # color over the hard point markers
        self.recolor(Color.SHIP_WEAPON_HARDPOINT, Color.BLACK)
        self.recolor(Color.SHIP_WEAPON_FLOATING_HARDPOINT, Color.WHITE)
        self.recolor(Color.SHIP_LAUNCH_HARDPOINT, Color.BLACK)

    def get_at(self, (x, y)):
        color = self.surface.get_at((x, y))

        return color[:3]
