

class NodeComponent(object):

    def __init__(self):
        pass

    def update(self):
        raise NotImplementedError

    def draw(self, display_surface, rel_pos):
        raise NotImplementedError
