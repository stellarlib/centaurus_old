from image import Image


class ImageArchive(object):

    instance = None

    @classmethod
    def get_instance(cls):

        if cls.instance is None:
            cls.instance = cls()
        return cls.instance

    def __init__(self):

        self.archive = {}

    def get_image(self, img_key):

        if img_key not in self.archive:
            self.archive[img_key] = self.load_image(img_key)

        return self.archive[img_key]

    def load_image(self, img_key):

        return Image.from_file(img_key)


def load_image(img_key):
    archive = ImageArchive.get_instance()
    return archive.get_image(img_key)
