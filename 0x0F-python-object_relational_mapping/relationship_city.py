#!/usr/bin/python3
"""
Module creates City class that
inherits from Base class.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """
    Creates table that stores
    unique city ids and names
    with reference to state_id.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, unique=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'),
                      nullable=False)
