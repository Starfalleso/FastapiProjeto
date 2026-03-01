# SQLAlchemy ORM models
from sqlalchemy import Column, Integer, String
from database import Base

# Book database model
class Book(Base):
    """Book table model"""
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    publisher = Column(String(255), nullable=False)