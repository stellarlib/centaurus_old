from ..vector_model import VectorModel
from stellarlib.vector import Vector
from ..components.polygon import Polygon


class ShipModel(VectorModel):

    def __init__(self, color):

        vertices = {
            'a': Vector(0, -5),
            'b': Vector(2.7, 1),
            'd': Vector(-2.7, 1),
            'c': Vector(0, 2)
        }

        components = [Polygon(self, ('a', 'b', 'c', 'd'), color, width=2)]

        VectorModel.__init__(self, vertices, components)

