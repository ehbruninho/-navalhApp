from functools import wraps
from flask import redirect,url_for, session
from app.models.users import User

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user_id = session.get('user_id')
        if not user_id:
            return redirect(url_for('user.login_user'))

        user = User.query.get(user_id)
        if not user:
            session.clear()
            return redirect(url_for('user.login_user'))

        return f(*args, **kwargs)
    return decorated_function

