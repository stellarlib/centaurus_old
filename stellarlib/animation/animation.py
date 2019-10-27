import stellarlib.transform
import stellarlib.node


class Animation(object):

    def __init__(self, actor, permanent=True):

        if isinstance(actor, stellarlib.transform.Transform):
            self.animation_group = actor.animations
        elif isinstance(actor, stellarlib.node.Node):
            self.animation_group = actor.transform.animations
        else:
            raise TypeError("Expected Node or Transform object as actor argument.")

        self.animation_group.add(self)
        self.permanent = permanent  # marks whether it affects base_vector or position vector of transform
        self.paused = False
        self.looping = False

    def update(self):
        raise NotImplementedError

    def update_vector(self, vector):
        raise NotImplementedError

    def is_complete(self):
        self.end()

    def end(self):
        self.animation_group.mark_for_removal(self)
        self.on_complete()

    def on_complete(self):
        pass
