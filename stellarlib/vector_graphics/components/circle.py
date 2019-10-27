from pygame.gfxdraw import filled_circle, aacircle


class Circle(object):

    def __init__(self, model, vertices, radius, color_id='main'):

        self.model = model
        self.vertices = vertices
        self.color_id = color_id
        self.radius = radius

    def draw(self, surface, points, colors, strength=1.0):

        color = colors[self.color_id]
        if color is None:
            return

        x, y = points[self.vertices[0]]
        r = int(round(self.radius * strength))
        filled_circle(surface, x, y, r, color)
        aacircle(surface, x, y, r, color)
