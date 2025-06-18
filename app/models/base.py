from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from app.config import DevelopmentConfig  # ou ProductionConfig, depende do ambiente

Base = declarative_base()

DATABASE_URL = DevelopmentConfig.SQLALCHEMY_DATABASE_URI
engine = create_engine(DATABASE_URL, echo=False)

SessionLocal = sessionmaker(bind=engine)

def create_session():
    return SessionLocal()