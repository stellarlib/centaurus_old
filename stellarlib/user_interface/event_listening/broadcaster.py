

class Broadcaster(object):

    def __init__(self):
        self.listeners = []

    def broadcast(self):
        map(lambda x: x.ping(), self.listeners)

    def add_listener(self, listener):
        self.listeners.append(listener)

    def remove_listener(self, listener):
        self.listeners.remove(listener)
