#!/usr/bin/python3
"""A Python file similar to model_state.py named model_city.py
That contains the class definition of a City."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ))

    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(
        State.name, City.id, City.name
    ).filter(
        State.id == City.state_id
    ).order_by(
        City.id.asc()
    ).all()

    for row in cities:
        print(row[0] + ": (" + str(row[1]) + ") " + row[2])

    session.close()
