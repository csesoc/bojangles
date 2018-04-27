from flask import Flask

class ConfigClass(object):
    DEBUG = True

def register_models(app):
    from . import models

def register_blueprints(app):
    from .basic import app as basic_bp
    app.register_blueprint(basic_bp)

def create_app():
    app = Flask(__name__)
    app.config.from_object(__name__ + '.ConfigClass')

    register_models(app)
    register_blueprints(app)

    return app


