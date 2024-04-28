#!/usr/bin/python3
"""a script 14-model_city_fetch_by_state.py that prints
all City objects from the database hbtn_0e_14_usa
"""

import sys
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3])
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State.name, City.id, City.name).filter(
        State.id == City.state_id).order_by(City.id).all()

    for row in result:
        print("{}: ({}) {}".format(row[0], str(row[1]), row[2]))

    session.close()
