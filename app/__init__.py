from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import DevelopmentConfig  # ou ProductionConfig
from flask_wtf import CSRFProtect
from flask_session import Session

# Cria instâncias globais
db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()
sess = Session()

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Pluga o SQLAlchemy e o Migrate
    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)

    # Configurando Sessions
    app.config['SESSION_TYPE'] = 'filesystem'
    sess.init_app(app)

    # Importa models para registrar no SQLAlchemy
    from app.models import users  # e outros models

    # Registra rotas
    from app.routes.user_routes import user_bp
    app.register_blueprint(user_bp)

    return app
