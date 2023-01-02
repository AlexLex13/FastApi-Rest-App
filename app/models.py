from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
from .database import Base

class Post(Base):
    __tablename__ = "Post"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String,  nullable=False)
    content = Column(String,  nullable=False)
    published = Column(Boolean, server_default='TRUE', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), 
                        server_default=text('NOW()'), nullable=False)
    user_id = Column(Integer, ForeignKey("User.id", ondelete="CASCADE"), nullable=False)

    owner = relationship("User")


class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String,  nullable=False, unique=True)
    password = Column(String,  nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), 
                        server_default=text('NOW()'), nullable=False)


class Vote(Base):
    __tablename__ = "Vote"

    post_id = Column(Integer, ForeignKey("Post.id", ondelete="CASCADE"), primary_key=True)
    user_id = Column(Integer, ForeignKey("User.id", ondelete="CASCADE"), primary_key=True)