# app/extensions.py
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import CSRFProtect
from flask_session import Session

db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()
sess = Session()
