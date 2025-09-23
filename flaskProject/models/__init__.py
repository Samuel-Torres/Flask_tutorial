"""
This file makes the models directory a package and gives you one shared Base:
"""

from sqlalchemy.orm import declarative_base
from .users_model import Users

# creates table if it doesn't exist
Base = declarative_base()
