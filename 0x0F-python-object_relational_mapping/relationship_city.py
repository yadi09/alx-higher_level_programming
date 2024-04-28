#!/usr/bin/python3
"""
This module defines a City class
Contains the class definition of a City
"""

from relationship_state import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.exe.declarative import declarative_base


class City(Base):
    """
    Class that defines each city
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Interger, ForeignKey("states.id"), nullable=False)
