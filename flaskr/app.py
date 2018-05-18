from flask import Flask
from .bojangles import app as bojangles_bp
from .api import app as api_bp


def register_models(app):
    from . import models


def register_blueprints(app):
    app.register_blueprint(bojangles_bp)
    app.register_blueprint(api_bp, url_prefix='/api')


def create_app(config):
    app = Flask(__name__, static_url_path='/static')
    app.config.from_object(config)

    register_models(app)
    register_blueprints(app)

    return app
