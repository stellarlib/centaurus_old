from vector_sprite_renderer import VectorSpriteRenderer
from stellarlib.node.node_component import NodeComponent
from stellarlib.color import Color


class VectorSprite(NodeComponent):

    def __init__(self, model_key, scale=1.0, rotation=0.0, main_color=Color.WHITE):

        NodeComponent.__init__(self)

        self.vector_model_key = model_key

        self.rotation = rotation
        self.scale = scale

        self.colors = {'main': main_color}

    def update(self):
        pass

    def draw(self, display_surface, rel_point):

        VectorSpriteRenderer.render_vector_sprite(self.vector_model_key, display_surface, rel_point,
                                                  self.rotation, self.scale, self.colors)

    def load_color_component(self, color):

        self.colors = color
