from sqlalchemy import Column, Integer, String, Boolean, Enum
from app.models.base import  create_session
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import secrets
from app import db

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

    def __init__(self, email, password):
        self.email = email
        self.password = generate_password_hash(password)
        self.verification_code = secrets.token_urlsafe(16)
        self.is_verified = False
        self.type_user = "Client"

    @classmethod
    def create_user(cls, email, password):
        session_db = create_session()
        try:
            user = cls(email,password)
            session_db.add(user)
            session_db.commit()
            email_value = user.email
            token_value = user.verification_code
            return email_value, token_value
        except Exception as e:
            session_db.rollback()
            print(f'Erro ao salvar Usuário! Error: {e}')
            return None
        finally:
            session_db.close()

    @classmethod
    def login_user(cls, email, password):
        session_db = create_session()
        try:
            user = session_db.query(cls).filter_by(email=email).first()
            if user and check_password_hash(user.password, password):
                return user
            return None
        except Exception as e:
            print(f'Erro ao validar login! Error: {e}')
        finally:
            session_db.close()

    @classmethod
    def check_token(cls, user_id, verification_code):
        session_db = create_session()
        try:
            user = session_db.query(cls).filter_by(id=user_id).first()
            if verification_code == user.verification_code:
                user.is_verified = True
                session_db.commit()
                return True
            return False
        except Exception as e:
            print(f'Erro ao consultar token! Error: {e}')
        finally:
            session_db.close()

    @classmethod
    def check_exist_email(cls,email):
        session_db = create_session()
        try:
            user = session_db.query(cls).filter_by(email=email).first()
            if user:
                return True
            return False
        except Exception as e:
            print(f'Erro ao consultar email! Error: {e}')
        finally:
            session_db.close()

    @classmethod
    def complete_user(cls, user_id, first_name, last_name,doc_register, foto, mobile_number):
        session_db = create_session()
        try:
            user = session_db.query(cls).filter_by(id=user_id).first()
            if user:
                user.first_name = first_name
                user.last_name = last_name
                user.doc_register = doc_register
                user.foto = foto
                user.mobile_number = mobile_number
                session_db.commit()
                return True
            return False
        except Exception as e:
            session_db.rollback()
            print(f'Erro ao salvar Usuario! Error: {e}')
        finally:
            session_db.close()

    @classmethod
    def delete_user(cls, user_id):
        session_db = create_session()
        try:
            user = session_db.query(cls).filter_by(id=user_id).first()
            if user:
                session_db.delete(user)
                session_db.commit()
                return True
            return False
        except Exception as e:
            print(f'Erro ao consultar token! Error: {e}')
            session_db.rollback()
        finally:
            session_db.close()