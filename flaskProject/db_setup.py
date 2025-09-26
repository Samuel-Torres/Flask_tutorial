"""
Database setup file to create the database, tables, sessions.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base
from . import (  # pylint: disable=unused-import # this auto-imports models via models/__init__.py
    models,
)

engine = None
Session = None


def init_db(db_path: str):
    """Initialize the database engine and sessionmaker."""
    global engine, Session
    engine = create_engine(db_path)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
