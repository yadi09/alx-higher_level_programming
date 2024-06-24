#!/usr/bin/python3
"""a script that adds the State object “Louisiana”
To the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("\
mysql+mysqldb://{}:{}@localhost:3306/{}\
".format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State()
    new_state.name = "Louisiana"
    session.add(new_state)
    session.commit()

    state = session.query(State).filter(
        State.name == "Louisiana").order_by(State.id.desc()).first()

    print(state.id)

    session.close()
