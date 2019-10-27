from stellarlib.vector_graphics.vector_model_archive import VectorModelArchive
from rotation_matrix_3D import RotationMatrix3D


class VectorSpriteRenderer3D(object):

    @staticmethod
    def render_vector_sprite(model_key, display_surface, (x, y), rotation, scale, colors):

        surface = display_surface.surface

        vector_model = VectorModelArchive.get_instance().get_model(model_key)

        points = {v: VectorSpriteRenderer3D.get_adjusted_point((x, y), vector_model.vertices[v], rotation, scale)
                  for v in vector_model.vertices}

        # TODO filter out components that are fully obscured behind the model
        map(lambda c: c.draw(surface, points, colors), vector_model.components)

    @staticmethod
    def get_adjusted_point((rx, ry), vector, rotation, scale):

        x, y, z = vector.get_mult_tuple(scale)
        x, y, z = RotationMatrix3D.rotate((x, y, z), rotation)

        z += 30.0

        px, py = VectorSpriteRenderer3D.project_points_2D(x, y, z)

        x = px + rx
        y = py + ry

        return x, y

    @staticmethod
    def project_points_2D(x, y, z):

        # half display width and height
        sw = 200.0
        sh = 200.0

        px = (x / z) * sw + sw
        py = (y / z) * sh + sh

        return int(round(px)), int(round(py))
