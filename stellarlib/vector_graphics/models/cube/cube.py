from stellarlib.vector_graphics.model_3D.model_3D import VectorModel3D
from stellarlib.vector.vector_3 import Vector3
from stellarlib.vector_graphics.components.polygon import Polygon
from stellarlib.vector_graphics.components.line_sequence import LineSequence


class CubeModel(VectorModel3D):

    def __init__(self, n, m):

        color_id = 'main'
        vertices, components = self.load_model(n, m, color_id)

        VectorModel3D.__init__(self, vertices, components)

    def load_model(self, n, m, color):

        vertices = {
            'a': Vector3(1, 1, 1),
            'b': Vector3(-1, 1, 1),
            'c': Vector3(-1, -1, 1),
            'd': Vector3(1, -1, 1),

            'e': Vector3(1, 1, -1),
            'f': Vector3(-1, 1, -1),
            'g': Vector3(-1, -1, -1),
            'h': Vector3(1, -1, -1),
        }

        return vertices, [LineSequence(self, ('a', 'b', 'c', 'd'), color, closed=True),
                          LineSequence(self, ('e', 'f', 'g', 'h'), (255, 0, 0), closed=True),
                          LineSequence(self, ('a', 'e', 'h', 'd'), (255, 255, 0), closed=True),
                          LineSequence(self, ('c', 'g', 'f', 'b'), (0, 255, 255), closed=True)
                          ]
