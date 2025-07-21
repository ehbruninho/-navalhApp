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

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user_id = session.get('user_id')
        print(user_id)
        if not user_id:
            return redirect(url_for('user.login_user'))

        type_user = User.get_type_user(user_id)
        print(type_user)
        if type_user != 'Administrator':

            return redirect(url_for('user.login_user'))

        return f(*args, **kwargs)
    return decorated_function

