from app.config.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class Task(Base):
    
    __tablename__ = 'tasks'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    to_do = Column(Boolean)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates="task")