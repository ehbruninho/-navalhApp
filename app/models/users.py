from sqlalchemy import Column, Integer, String, Boolean, Enum
from app.models.base import  create_session
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
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
        session = create_session()
        try:
            user = cls(email,password)
            session.add(user)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f'Erro ao salvar Usuário! Error: {e}')
        finally:
            session.close()

