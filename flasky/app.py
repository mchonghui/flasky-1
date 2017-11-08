from flask import Flask

from flask_bootstrap  import Bootstrap
from flasky.blueprints.page import page
from flask_moment import Moment


def create_app(settings_override=None):
    #Create a Flask application using the app factory pattern.

    app = Flask(__name__, instance_relative_config=True) #look for instance module at the same level as main module flasky

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    if settings_override: app.config.update(settings_override)

    app.register_blueprint(page)
    bootstrap = Bootstrap(app)
    moment = Moment(app)

    return app
