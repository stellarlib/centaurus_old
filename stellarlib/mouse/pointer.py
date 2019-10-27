

class Pointer(object):

    def __init__(self, scene):

        self.scene = scene

        self.pos = None

    @property
    def game_logic(self):
        return self.scene.game_logic

    def set_pos(self, pos):
        if pos != self.pos:
            self.change_pos(pos)

    def change_pos(self, pos):
        # here we alert game logic to update pointer
        self.alert_new_pointer_position(pos)
        self.pos = pos

    def alert_new_pointer_position(self, pos):
        self.game_logic.highlighter.pointer_moved(pos)
