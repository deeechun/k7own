from functools import wraps
from flask import redirect, url_for
from flask_login import current_user

# decorator to check if account is verified
def verify_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.verified==0:
            return redirect(url_for('user.unverified'))
        return func(*args, **kwargs)
    return decorated_function
