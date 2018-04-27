import os


class Config(object):
    DEBUG = False


class Development(object):
    DEBUG = True
    SECRET_KEY = 'development-only'


class Production(object):
    DEBUG = False

    def __init__(self):
        self.SECRET_KEY = os.environ['SECRET_KEY']
