from flask import redirect, url_for
from flask_login import current_user
from functools import wraps

# decorator to check if account is verified
def verify_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.verified==0:
            return redirect(url_for('auth.unverified'))
        return func(*args, **kwargs)
    return decorated_function