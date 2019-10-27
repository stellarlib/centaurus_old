from stellarlib.group import Group


class AnimationGroup(Group):

    def __init__(self):

        Group.__init__(self)

    def update_base_vector(self, vector):

        map(lambda ani: ani.update_vector(vector), filter(lambda a: a.permanent, self.elements))

    def update_position_vector(self, vector):

        map(lambda ani: ani.update_vector(vector), filter(lambda a: not a.permanent, self.elements))

    # override draw method - can't draw animations
    def draw(self, surf):
        pass

    def clear_remove_queue(self):

        for el in self.to_be_removed:
            self.elements.remove(el)

        del self.to_be_removed[:]

