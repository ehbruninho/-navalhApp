from flask import Blueprint, jsonify
from app.models.users import User

# Cria o blueprint
user_bp = Blueprint('user', __name__)

# Define rotas usando ele
@user_bp.route('/users')
def get_users():
    User.create_user(email='bhsantos16@gmail.com', password='Bruno2408')
    return jsonify({"msg": "Hello, users!"})
