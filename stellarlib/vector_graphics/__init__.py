from vector_model_archive import VectorModelArchive
from vector_sprite import VectorSprite
from model_3D import VectorSprite3D
import models.selectors as selectors
import models.rough_sphere as rough_sphere


def create_model(key, model):

    archive = VectorModelArchive.get_instance()
    archive.add_model(key, model)


def confirm_model(key):

    archive = VectorModelArchive.get_instance()
    return key in archive.models
