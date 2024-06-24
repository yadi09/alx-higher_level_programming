#!/usr/bin/python3
"""a script that lists all State objects
from the database hbtn_0e_6_usa"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "mysql+mysqldb://yadi09:Yadi_0988@localhost:3306/hbtn_0e_6_usa"
)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

states = session.query(State).order_by(State.id.asc()).all()

for row in states:
    print(": ".join([str(row.id), row.name]))

session.close()
