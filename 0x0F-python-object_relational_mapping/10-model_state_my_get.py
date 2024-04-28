#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    script that lists all State objects from the database hbtn_0e_6_usa
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3])
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    stateName = sys.argv[4]

    Query = session.query(State).filter(State.name == stateName).first()

    if Query is None:
        print("Not found")
    else:
        print('{}'.format(Query.id))

    session.close()
