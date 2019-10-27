from silhouette_archive import SilhouetteArchive
from silhouette import Silhouette


def load_silhouette(image_key):

    archive = SilhouetteArchive.get_instance()
    return archive.get_silhouette(image_key)
