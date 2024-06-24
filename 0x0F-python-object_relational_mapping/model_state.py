#!/usr/bin/python3
"""a python file that contains the class definition of a State
and an instance Base = declarative_base()"""

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class State(Base):
    "a class maped to states"
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)


engine = create_engine(
    'mysql+mysqldb://yadi09:Yadi_0988@localhost:3306/hbtn_0e_6_usa'
)

Base.metadata.create_all(engine)
