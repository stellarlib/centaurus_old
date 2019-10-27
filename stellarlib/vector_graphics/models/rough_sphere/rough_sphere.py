from stellarlib.vector_graphics.model_3D.model_3D import VectorModel3D
from stellarlib.vector import Vector
from stellarlib.vector.vector_3 import Vector3
from stellarlib.vector_graphics.components.polygon import Polygon
from stellarlib.vector_graphics.components.line_sequence import LineSequence
from stellarlib.vector_graphics.components.line_sequence_3d import LineSequence3D
from stellarlib.vector_graphics.components.point import Point
from math import cos, radians, sin, pi


class RoughSphereModel(VectorModel3D):

    def __init__(self, n, m, diameter):

        assert m > 1 and m %2 != 0

        self.color_id = 'main'
        vertices, components = self.load_model(n, m, float(diameter))

        VectorModel3D.__init__(self, vertices, components)

    def load_model(self, n, m, diameter):

        radius = diameter/2
        layers = m/2
        discs = []

        for layer in range(layers):
            discs.append(self.make_disc(n, m, layer, radius))

        for layer in range(1, layers):
            discs.append(self.mirror_disc(discs[layer]))

        vertices = {}
        components = []

        for v, c in discs:
            vertices.update(v)
            components.extend(c)

        self.create_top_and_bottom_vertices(radius, vertices)

        lines = self.get_vertical_lines(n, m)
        components.extend(lines)

        return vertices, components

    def make_disc(self, n, m, layer, radius):

        vertices = {}
        components = []
        seq = []

        scale, disc_y = self.get_disc_pos(radius, layer, m)
        face_angle = 360.0 / n

        for i in range(n):

            angle = i * face_angle
            v = Vector.from_angle(angle, scale)

            x = v.x
            y = disc_y
            z = v.y

            disc_id = (i, layer)
            vertices[disc_id] = Vector3(x, y, z)
            seq.append(disc_id)

        components.append(LineSequence(self, seq, self.color_id, closed=True))

        return vertices, components

    def get_disc_pos(self, diameter, layer, m):

        face_angle = 360.0 / (m * 2)
        disc_angle = face_angle * layer
        v = Vector.from_angle(disc_angle, diameter)
        return v.x, v.y

    def mirror_disc(self, disc):

        vertices = {}
        components = []
        seq = []

        d_vertices = disc[0]

        for disc_id in sorted(d_vertices.keys()):

            old_vertex = d_vertices[disc_id]
            flipped_vertex = Vector3(old_vertex)
            flipped_vertex.y = flipped_vertex.y * -1

            new_disc_id = disc_id[0], -disc_id[1]
            vertices[new_disc_id] = flipped_vertex
            seq.append(new_disc_id)

        components.append(LineSequence3D(self, seq, self.color_id, closed=True))

        return vertices, components

    def get_vertical_lines(self, n, m):

        lines = []

        for x in range(n):

            seq = ['top']

            for layer in range(-m/2+2, m/2):
                seq.append((x, layer))

            seq.append('bot')
            lines.append(LineSequence3D(self, seq, self.color_id, closed=False))

        return lines

    def create_top_and_bottom_vertices(self, radius, vertices):
        top = Vector3(0, -radius, 0)
        bot = Vector3(0, radius, 0)
        vertices.update({'top': top, 'bot': bot})
