import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Adjectives(Base):
    __tablename__ = 'positive_adjectives'
    id = Column(Integer, primary_key=True)
    adjective = Column(String(250), nullable=False)
    
class Positive(Base):
    __tablename__ = 'positive_categories'
    id = Column(Integer, primary_key=True)
    category = Column(String(250), nullable=False)
    
engine = create_engine('sqlite:///happiness.db')

Base.metadata.create_all(engine)
