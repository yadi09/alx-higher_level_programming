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

    Query = session.query(State).filter(
        State.name.like('%a%')
    ).order_by(State.id)

    for row in Query:
        print('{}: {}'.format(row.id, row.name))

    session.close()
