"Users Model"

from models import Base
from sqlalchemy import Column, Integer, String


class Users(Base):
    "Users Schema"

    __tablename__ = "Users"
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String)
    password = Column(String)
