import os

from config.env import BASE_DIR, ABS_PATH


STATIC_PATH = 'static/images'


def get_image_context():
    return ['{0}/{1}'.format(STATIC_PATH, elem) for elem in sorted(
        os.listdir(ABS_PATH(BASE_DIR, STATIC_PATH)))]
