import os
from flask import Flask, render_template
from app.models import User, PostHome, PostCar

def create_app(config_object):
    """
    Application factory function creates app using configuration
    taken as an object from config.py
    """
    # initialize app and load config from object in config.py
    app = Flask(__name__)
    app.config.from_object(config_object)

    # import and initialize extensions with application instance
    from app.models import db, login_manager
    db.init_app(app)
    login_manager.init_app(app)
    from app.auth.email import mail
    mail.init_app(app)
    from flask_wtf.csrf import CsrfProtect
    csrf = CsrfProtect()
    csrf.init_app(app)

    # import and register blueprints
    from app.home.views import home_blueprint
    from app.auth.views import auth_blueprint
    from app.post.views import post_blueprint
    from app.api.views import api_blueprint
    app.register_blueprint(home_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(post_blueprint)
    app.register_blueprint(api_blueprint)

    return app