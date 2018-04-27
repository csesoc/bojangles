import os

from flask import Flask

class PROD(object):
    DEBUG = False

class DEV(object):
    DEBUG = True
    SECRET_KEY = 'insecure_key_for_development'

def register_models(app):
    from . import models

def register_blueprints(app):
    from .bojangles import app as bojangles_bp
    app.register_blueprint(bojangles_bp)

def create_app():
    app = Flask(__name__, static_url_path='/static')

    # Get our environment and fail fast if we don't find one

    ENV = os.environ.get('ENV')
    if not ENV or ENV not in ['PROD', 'DEV']:
        raise Exception("Running environment must be specified and either PROD or DEV.")

    try:
        app.config.from_object(__name__+ '.{0}'.format(ENV))
    except Exception as e:
        # TODO: Better error handling than this
        raise e

    # Figure out how to do this better later
    # I.e. have this in the config class and not _always_ read it in regardless of environment

    if ENV == 'PROD':
        key = open(os.path.join(os.path.dirname(__file__), "../secrets", "flask.key")).read()

        if 'GITCRYPT' in key: 
            raise Exception("GITCRYPT detected in secret key, are you sure you unlocked the repo?")

        app.config['SECRET_KEY'] = key

    register_models(app)
    register_blueprints(app)

    return app