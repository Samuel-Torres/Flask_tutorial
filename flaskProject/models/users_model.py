"Users Model"

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base


class Users(Base):
    "Users Schema"

    __tablename__ = "Users"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    posts = relationship("Posts", back_populates="user", cascade="all, delete-orphan")
