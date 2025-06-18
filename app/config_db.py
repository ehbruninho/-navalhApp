from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from app.config import DevelopmentConfig  # ou ProductionConfig

Base = declarative_base()
engine = create_engine(DevelopmentConfig.SQLALCHEMY_DATABASE_URI)