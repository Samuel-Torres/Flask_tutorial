"""
Database setup file to create the database, tables, sessions.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .models import Base  # your models

engine = None
Session = None

def init_db(db_url: str):
    global engine, Session
    engine = create_engine(db_url, echo=True)
    Session = sessionmaker(bind=engine)
    return engine  # return the engine for CLI use
