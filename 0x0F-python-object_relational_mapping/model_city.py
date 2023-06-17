#!/usr/bin/python3
"""
Module creates City class that
inherits from the Base class.
"""
from sqlalchemy import MetaData
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base

class City(Base):
    """
    Creates table that stores unique city id(column_1)
    along with their names(column_2) and references to
    state_id.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key= True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
