from flask import Blueprint, jsonify, flash
from app.models.users import User
from app.utils.notifications import send_email

# Cria o blueprint
user_bp = Blueprint('user', __name__)

# Define rotas usando ele
@user_bp.route('/users')
def get_users():
    email_user = 'bhsantos16@gmail.com'
    password_user ='bruno@2408'

    user = User.query.filter_by(email=email_user).first()
    if not user:
        email,token = User.create_user(email_user, password_user)

        if email and token:
             send_email.send_token(email, token)
        flash("Usuario criado com sucesso, verifique seu email")
    else:
        print('Usuario existente')

    return jsonify({"msg": "Hello, users!"})
