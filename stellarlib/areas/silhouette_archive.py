from stellarlib.image import load_image
from silhouette import Silhouette


SHIELD_DEPTH = 2


class SilhouetteArchive(object):

    instance = None

    @classmethod
    def get_instance(cls):

        if cls.instance is None:
            cls.instance = cls()

        return cls.instance

    def __init__(self):

        self.archive = {}

    def get_silhouette(self, img_key):

        if img_key not in self.archive:
            self.archive[img_key] = self.create_silhouette(img_key)

        return self.archive[img_key]

    def create_silhouette(self, img_key):

        shield_sil = False
        if img_key.startswith('shielded_'):
            img_key = img_key[9:]
            shield_sil = True

        image = load_image(img_key)
        silhouette = Silhouette.from_surface(image.surface)

        if shield_sil:
            silhouette.extend(SHIELD_DEPTH)

        return silhouette
