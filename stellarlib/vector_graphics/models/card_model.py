from ..vector_model import VectorModel
from stellarlib.vector import Vector
from ..components.line import Line
from ..components.polygon import Polygon


class CardModel(VectorModel):

    def __init__(self, card_width, card_height, x_margin, top_y_margin, bot_y_margin, back_color, border_color, border_width):

        vertices = self.load_vertices(card_width, card_height, x_margin, top_y_margin, bot_y_margin)

        edges = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
        inner_edges = [''.join((e, '_inner')) for e in edges]

        components = [
            # Polygon(self, ('a', 'b', 'd'), back_color),
            # Polygon(self, ('b', 'c', 'd'), back_color),
            # Polygon(self, ('e', 'f', 'h'), back_color),
            # Polygon(self, ('f', 'g', 'h'), back_color),
            # Polygon(self, ('a', 'e', 'h'), back_color),
            # Polygon(self, ('a', 'd', 'e'), back_color),
            Polygon(self, edges, back_color),
            Polygon(self, edges, border_color, border_width),
            Polygon(self, inner_edges, border_color, border_width),
            # Line(self, 'a', 'b', border_color, border_width),
            # Line(self, 'b', 'c', border_color, border_width),
            # Line(self, 'c', 'd', border_color, border_width),
            # Line(self, 'd', 'e', border_color, border_width),
            # Line(self, 'e', 'f', border_color, border_width),
            # Line(self, 'f', 'g', border_color, border_width),
            # Line(self, 'g', 'h', border_color, border_width),
            # Line(self, 'h', 'a', border_color, border_width)
        ]

        VectorModel.__init__(self, vertices, components)

    def load_vertices(self, card_width, card_height, x_margin, top_y_margin, bot_y_margin):

        cw = card_width/2
        ch = card_height/2

        vertices = {
            'a': Vector(-cw, -ch + top_y_margin),
            'b': Vector(-cw + x_margin, -ch),
            'c': Vector(cw - x_margin, -ch),
            'd': Vector(cw, -ch + top_y_margin),
            'e': Vector(cw, ch - bot_y_margin),
            'f': Vector(cw - x_margin, ch),
            'g': Vector(-cw + x_margin, ch),
            'h': Vector(-cw, ch - bot_y_margin),
        }

        inner_vertices = {}

        for v in vertices:
            v2 = Vector(vertices[v].get_mult_tuple(.95))
            v2_key = ''.join((v, '_inner'))
            inner_vertices[v2_key] = v2

        vertices.update(inner_vertices)

        return vertices
