import os


class Config(object):
    DEBUG = False


class Development(Config):
    DEBUG = True
    SECRET_KEY = 'development-only'
    CLASSUTIL_PATH = 'api/specialisation/db.json'


class Production(Config):
    DEBUG = False

    def __init__(self):
        self.SECRET_KEY = os.environ['SECRET_KEY']
