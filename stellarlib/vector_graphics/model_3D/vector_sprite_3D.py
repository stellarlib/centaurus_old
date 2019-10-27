from vector_sprite_renderer_3D import VectorSpriteRenderer3D
from stellarlib.node.node_component import NodeComponent
from stellarlib.color import Color


class VectorSprite3D(NodeComponent):

    def __init__(self, model_key, scale=1.0, main_color=Color.WHITE):

        NodeComponent.__init__(self)

        self.vector_model_key = model_key

        self.rotation = 0.0
        self.scale = scale

        self.colors = {'main': main_color}

    def update(self):
        pass

    def draw(self, display_surface, rel_point):

        VectorSpriteRenderer3D.render_vector_sprite(self.vector_model_key, display_surface, rel_point,
                                                    self.rotation, self.scale, self.colors)

