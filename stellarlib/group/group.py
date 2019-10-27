

class Group(object):

    def __init__(self):

        self.elements = []
        self.to_be_removed = []

    def update(self):
        map(lambda x: x.update(), self.elements)
        if self.to_be_removed:
            self.clear_remove_queue()

    def draw(self, surf, rel_point):
        map(lambda x: x.draw(surf, rel_point), self.elements)

    def add(self, el):
        self.elements.append(el)

    def mark_for_removal(self, el):
        self.to_be_removed.append(el)

    def clear_remove_queue(self):

        for el in self.to_be_removed:
            self.elements.remove(el)

        del self.to_be_removed[:]

    def empty(self):
        return not self.elements
