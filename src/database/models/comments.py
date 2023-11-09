from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship 

from src.database.db import Base

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    comment = Column(String(280))
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=None)
    post_id = Column(Integer, ForeignKey('posts.id', ondelete='CASCADE'))
    post = relationship('Post', backref='comments')
    user_id = Column(
        'users_id', ForeignKey('users.id', ondelete='CASCADE'), default=None
    )
    user = relationship('User', backref='comments')