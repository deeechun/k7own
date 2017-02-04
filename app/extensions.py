from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CsrfProtect
from flask_mail import Mail

db = SQLAlchemy()

login_manager = LoginManager()
# config action on login_required views
login_manager.login_view = '/login'
login_manager.login_message = '로그인을 먼저 해주세요.'
login_manager.login_message_category = 'warning'

csrf = CsrfProtect()

mail = Mail()
