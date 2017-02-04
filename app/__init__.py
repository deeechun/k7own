import os
from flask import Flask, render_template
from app.extensions import db, login_manager, csrf, mail
from app.scripts import verify_required
from app.models import User, PostHome

# import and setup environment variables
import config_env

# create app and load config from Config object in config.py
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

# initialize extensions from extensions.py
db.init_app(app)
login_manager.init_app(app)
csrf.init_app(app)
mail.init_app(app)

# import and register blueprints
from app.home.views import home_blueprint
from app.user.views import user_blueprint
from app.post.views import post_blueprint
from app.api.views import api_blueprint
app.register_blueprint(home_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(post_blueprint)
app.register_blueprint(api_blueprint)

# error page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
