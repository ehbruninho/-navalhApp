from sqlalchemy import Column, Integer, String, Boolean, Enum, DateTime
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import secrets
from app.utils.db_helper import *

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    password = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    first_name = Column(String(100), nullable=True)
    last_name = Column(String(100), nullable=True)
    doc_register = Column(String(14), nullable=True, unique=True)
    mobile_number = Column(String(15), nullable=True)
    foto = Column(String(255), nullable=True)
    verification_code = Column(String(100))
    is_verified = Column(Boolean, nullable=True, default=False)
    type_user = Column(Enum("Barber","Client","Administrator"), nullable=False, default="Client")
    create_att = Column(DateTime,nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.password = generate_password_hash(password)
        self.verification_code = secrets.token_urlsafe(16)
        self.is_verified = False
        self.create_att = datetime.now()
        self.type_user = "Client"


    @classmethod
    def create_user(cls, email, password):
        user = cls(email, password)
        db.session.add(user)
        return user

    @classmethod
    def login_user(cls, email, password):
        user = get_instance_by(cls,email=email)
        if user and check_password_hash(user.password, password):
            return user
        return None

    @classmethod
    def check_token(cls, user_id, verification_code):
        user = get_instance_by(cls,id=user_id)
        if verification_code == user.verification_code:
            user.is_verified = True
            user.verification_code = ""
            commit_instance(user)
            return True
        return False

    @classmethod
    def check_exist_email(cls,email):
        return bool(get_instance_by(cls,email=email))

    @classmethod
    def complete_user(cls, user_id, first_name, last_name,doc_register, foto, mobile_number):
            updates = {
                "first_name": first_name,
                "last_name": last_name,
                "doc_register": doc_register,
                "foto": foto,
                "mobile_number": mobile_number,
            }
            user = update_instance_by(cls,user_id,updates)
            return bool(user)

    @classmethod
    def delete_user(cls, user_id):
        return delete_instance_by(cls,user_id)

    @classmethod
    def update_password(cls, user_id, password):
       hashed_password = generate_password_hash(password)
       user = update_instance_by(cls,user_id, {"password": hashed_password})
       return bool(user)