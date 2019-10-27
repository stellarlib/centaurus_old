

class MessageCenter(object):

    instance = None

    @classmethod
    def get_instance(cls):

        if cls.instance is None:
            cls.instance = cls()

        return cls.instance

    def __init__(self):

        self.scene = None

    def bind_scene(self, scene):
        self.scene = scene

