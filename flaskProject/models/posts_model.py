"Posts Model"

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base


class Posts(Base):
    """Posts Schema"""

    __tablename__ = "Posts"

    post_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)

    # Foreign key relationship to Users table
    user_id = Column(Integer, ForeignKey("Users.user_id"), nullable=False)

    # ORM relationship (lets us do post.user or user.posts)
    user = relationship("Users", back_populates="posts")
