#!/usr/bin/python3
"""
This module defines a script that creates the State “California”
with the City “San Francisco” from the database hbtn_0e_100_usa
Creates the State "California" with the City "San Francisco" from a DB
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_State = State(name='California')
    new_City = City(name='San Francisco')
    new_State.cities.append(new_City)

    session.add(new_State)
    session.add(new_City)

    session.commit()

    session.close()
