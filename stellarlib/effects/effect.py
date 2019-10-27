

class Effect(object):

    def __init__(self, group):

        self.group = group

        self.group.add(self)
        self._initialize_effect()

    def update(self):

        self._on_update()

        if self.effect_complete():
            self.end()
            self._deinitialize_effect()

    def draw(self, display_surface, rel_pos):
        pass

    def _on_update(self):
        pass

    def _initialize_effect(self):
        pass

    def _deinitialize_effect(self):
        pass

    def effect_complete(self):
        raise NotImplementedError

    def end(self):
        self.group.mark_for_removal(self)
