from flask import Flask

from flask_bootstrap  import Bootstrap
from .blueprints.page import page
from .blueprints.auth import auth
from flask_moment import Moment
from .extensions import (db, login_manager)
from flask_login import LoginManager


def create_app(settings_override=None):
    #Create a Flask application using the app factory pattern.

    app = Flask(__name__, instance_relative_config=True) #look for instance module at the same level as main module flasky

    #configs
    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)
    if settings_override: app.config.update(settings_override)

    #blueprints
    app.register_blueprint(page)
    app.register_blueprint(auth)

    #others
    bootstrap = Bootstrap(app)
    moment = Moment(app)
    
    #integrates app to other objects and initiates
    extensions(app)

    return app

def extensions(app):
    """
    Register 0 or more extensions (mutates the app passed in).
    :param app: Flask application instance
    :return: None
    """
    db.init_app(app)
    login_manager.init_app(app)

    return None