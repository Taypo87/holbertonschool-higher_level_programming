#!/usr/bin/python3
"""Lists all state objects from given database"""

import sqlalchemy
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State).first()
    if results is not None:
        print("{}: {}".format(results.id, results.name))
    else:
        print("Nothing")
    session.close()
