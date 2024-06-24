#!/usr/bin/python3
"""a script that prints the State object
with the name passed as argument
from the database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("\
mysql+mysqldb://{}:{}@localhost:3306/{}\
".format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = select(State).where(State.name == sys.argv[4])

    state = session.execute(query).scalar()

    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
