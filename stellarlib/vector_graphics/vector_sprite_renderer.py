from vector_model_archive import VectorModelArchive
from rotation_matrix import RotationMatrix


class VectorSpriteRenderer(object):

    @staticmethod
    def render_vector_sprite(model_key, display_surface, (x, y), rotation, scale, colors):

        surface = display_surface.surface

        vector_model = VectorModelArchive.get_instance().get_model(model_key)

        points = {v: VectorSpriteRenderer.get_adjusted_point((x, y), vector_model.vertices[v], rotation, scale)
                  for v in vector_model.vertices}

        map(lambda c: c.draw(surface, points, colors), vector_model.components)

    @staticmethod
    def get_adjusted_point((rx, ry), vector, rotation, scale):

        x, y = vector.get_mult_tuple(scale)
        x, y = RotationMatrix.rotate((x, y), rotation)

        x = int(round(x)) + rx
        y = int(round(y)) + ry

        return x, y
