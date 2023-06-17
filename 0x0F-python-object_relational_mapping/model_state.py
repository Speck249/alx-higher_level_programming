#!/usr/bin/python3
"""
Module creates Base class and
an inheriting State class to
work with SQLAlchemy ORM.
"""
from sqlalchemy import MetaData
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    Creates table that stores unique state id(column_1)
    along with their names(column_2).
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key= True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
