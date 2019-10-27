from stellarlib.vector_graphics.vector_model import VectorModel
from stellarlib.vector_graphics.components.line_sequence import LineSequence
from stellarlib.vector_graphics.components.polygon import Polygon
from stellarlib.vector.vector_tools import *


class TriangleSelector(VectorModel):

    cut_off_gap = .1
    corner_length = .1

    base_inset = .35
    rect_inset = .1
    bevel_angle = 60
    bevel_height = .02

    def __init__(self, side):

        self.color_id = 'main'
        vertices, components = self.create_vector_components(side)

        VectorModel.__init__(self, vertices, components)

    def create_vector_components(self, side):

        # corners of equilateral triangle
        inner_side = (side / 2.0) * cos(radians(30))

        # our basic shape. not actually used directly, just as a frame.
        shape = {
            'a': Vector.from_angle(-30, inner_side),
            'b': Vector.from_angle(-150, inner_side),
            'c': Vector(0, inner_side)
        }

        vertices = {}
        components = []

        self.create_cut_corners(shape, vertices, components)
        self.create_edge_pieces(shape, vertices, components, side)

        return vertices, components

    def create_cut_corners(self, shape, vertices, components):

        corners = cut_off_corners_of_shape(shape, TriangleSelector.cut_off_gap, TriangleSelector.corner_length)

        for c_vertices, c_sequence in corners:
            vertices.update(c_vertices)
            components.append(LineSequence(self, c_sequence, self.color_id))

    def create_edge_pieces(self, shape, vertices, components, side):

        cls = TriangleSelector
        base_inset = cls.base_inset
        rect_inset = cls.rect_inset
        bevel_angle = cls.bevel_angle
        bevel_height = cls.bevel_height * side

        names = get_vertex_names(shape)
        edges = get_edge_sequences(names)

        key = 'bevel'

        for a, b in edges:

            k = ''.join((key, str((a, b))))
            v, seq = get_beveled_line_inset(k, shape[a], shape[b], base_inset,
                                            rect_inset, bevel_angle, bevel_height)

            vertices.update(v)

            components.append(LineSequence(self, [seq[0], seq[-1]], self.color_id))
            components.append(Polygon(self, seq[1:-1], self.color_id))
