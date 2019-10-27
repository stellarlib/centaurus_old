from stellarlib.vector_graphics.vector_model import VectorModel
from stellarlib.vector_graphics.components.line_sequence import LineSequence
from stellarlib.vector_graphics.components.polygon import Polygon
from stellarlib.vector.vector_tools import *


class DiamondSelector(VectorModel):

    # cut corner dims
    cut_off_gap = .075
    corner_length = .15

    # bevel inset dims
    base_inset = .35
    rect_inset = .1
    bevel_angle = 60
    bevel_height = .04

    # hash mark dims
    spacing = .04
    h_width = .005
    h_height = .05

    def __init__(self, side):

        self.color_id = 'main'
        vertices, components = self.create_vector_components(side)

        VectorModel.__init__(self, vertices, components)

    def create_vector_components(self, side):

        # corners of equilateral triangle
        inner_side = side * cos(radians(45))

        shape = {
            'a': Vector(0, -inner_side),
            'b': Vector(inner_side, 0),
            'c': Vector(0, inner_side),
            'd': Vector(-inner_side, 0)
        }

        vertices = {}
        components = []

        self.create_cut_corners(shape, vertices, components)
        self.create_edge_pieces(shape, vertices, components, side)

        return vertices, components

    def create_cut_corners(self, shape, vertices, components):

        corners = cut_off_corners_of_shape(shape, DiamondSelector.cut_off_gap, DiamondSelector.corner_length)

        for c_vertices, c_sequence in corners:
            vertices.update(c_vertices)
            components.append(LineSequence(self, c_sequence, self.color_id))

    def create_edge_pieces(self, shape, vertices, components, side):

        self.create_beveled_insets(shape, vertices, components, side)
        self.create_hash_marks(shape, vertices, components, side)

    def create_beveled_insets(self, shape, vertices, components, side):

        cls = DiamondSelector
        base_inset = cls.base_inset
        rect_inset = cls.rect_inset
        bevel_angle = cls.bevel_angle
        bevel_height = cls.bevel_height * side

        edges = (('b', 'a'), ('d', 'c'))

        key = 'bevel'

        for a, b in edges:

            k = '.'.join((key, str(a), str(b)))
            v, seq = get_beveled_line_inset(k, shape[a], shape[b], base_inset,
                                            rect_inset, bevel_angle, bevel_height)

            vertices.update(v)

            components.append(LineSequence(self, [seq[0], seq[-1]], self.color_id))
            components.append(Polygon(self, seq[1:-1], self.color_id))

    def create_hash_marks(self, shape, vertices, components, side):

        cls = DiamondSelector
        spacing = cls.spacing
        width = cls.h_width * side
        height = cls.h_height * side

        edges = (('a', 'd'), ('b', 'c'))

        key = 'hash'

        for a, b in edges:

            k = '.'.join((key, str(a), str(b)))
            hashes = get_pair_hash_marks(k, shape[a], shape[b], spacing, width, height)

            for v, seq in hashes:

                vertices.update(v)

                components.append(Polygon(self, seq, self.color_id))
