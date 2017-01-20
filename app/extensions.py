from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from flask_wtf.csrf import CsrfProtect
from flask_mail import Mail
from functools import wraps
from flask import redirect, url_for

db = SQLAlchemy()

login_manager = LoginManager()
# config action on login_required views
login_manager.login_view = '/login'
login_manager.login_message = '로그인을 먼저 해주세요.'
login_manager.login_message_category = 'warning'

csrf = CsrfProtect()

mail = Mail()

# decorator to check if account is verified
def verify_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.verified==0:
            return redirect(url_for('user.unverified'))
        return func(*args, **kwargs)
    return decorated_function
