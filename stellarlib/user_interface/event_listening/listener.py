

class Listener(object):

    def __init__(self, ping_func):
        self.broadcaster = None
        self.ping_func = ping_func

    def ping(self):
        self.ping_func()

    def subscribe(self, broadcaster):
        self.broadcaster = broadcaster
        self.broadcaster.add_listener(self)

    def unsubscribe(self):
        self.broadcaster.remove_listener(self)
