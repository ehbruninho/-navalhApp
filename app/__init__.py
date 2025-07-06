from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import DevelopmentConfig  # ou ProductionConfig
from flask_wtf import CSRFProtect
from flask_session import Session
from sqlalchemy import event
from sqlalchemy.engine import Engine
from sqlite3 import Connection as SQLite3Connection
from datetime import timedelta



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
    app.config['SESSION_PERMANENT'] = True
    app.config['SESSION_LIFETIME'] = timedelta(minutes=30)
    sess.init_app(app)

    # Importando tabelas do sistema
    from app.models import users
    from app.models import region
    from app.models import local
    from app.models import barbers
    from app.models import services
    from app.models import servicesbarbers
    from app.models import times_slot
    from app.models import appointments
    from app.models import payments

    # Registra rotas
    from app.routes.user_routes import user_bp
    app.register_blueprint(user_bp)

    #Cuida do banco de dados (FK)
    @event.listens_for(Engine, "connect")
    def set_sqlite_pragma(dbapi_connection,connection_record):
        if isinstance(dbapi_connection, SQLite3Connection):
            cursor = dbapi_connection.cursor()
            cursor.execute("PRAGMA foreign_keys=ON;")
            cursor.close()

    return app
