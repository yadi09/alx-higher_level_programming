#!/usr/bin/python3
"""
City Model Class City
"""

from sqlalchemy import Column, String, Integer, ForeignKey
from model_state import Base


class City(Base):
    """
    class definition of a City
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Interger, ForeignKey("states.id"), nullable=False)
