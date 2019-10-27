from stellarlib.node import Display


class SceneTree(object):

    def __init__(self, app, (sw, sh)):

        self.app = app

        self.screen_node = Display(None, (0, 0), sw, sh)

        self.tree = [self.screen_node]

        self.screen_surface = self.screen_node.display_surface.surface

    def update(self):

        map(lambda n: n.update(), self.tree)

    def draw(self):

        # draw all nodes and children onto our screen display surface
        map(lambda n: n.draw_onto(self.screen_node), self.tree)

        self.screen_node.render_to_screen()
