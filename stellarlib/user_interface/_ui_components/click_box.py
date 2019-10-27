

class ClickBox(object):

    def __init__(self, node, w, h):

        self.node = node
        self.w = w
        self.h = h

    def mouse_is_over(self, (x, y)):
        sx, sy = self.node.screen_pos()
        return sx <= x < self.w + sx and sy <= y < self.h + sy
