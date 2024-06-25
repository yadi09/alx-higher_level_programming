#!/usr/bin/python3
"""City class with relashionship state class"""

from sqlalchemy import Column, Integer, String, ForignKey
from relationship_state import State, Base


class City(Base):
    "class called City"
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForignKey="states.id")
