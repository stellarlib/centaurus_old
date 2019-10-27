

class VectorModelArchive(object):

    instance = None

    @classmethod
    def get_instance(cls):

        if cls.instance is None:
            cls.instance = cls()

        return cls.instance

    def __init__(self):

        self.models = {}

    def add_model(self, key, model):
        self.models[key] = model

    def get_model(self, key):
        return self.models[key]
