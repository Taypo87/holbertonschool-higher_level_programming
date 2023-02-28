#!/usr/bin/python3
"""Lists state object that matches argument passed """

import sqlalchemy
from sqlalchemy import create_engine, select, update
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    updates = session.query(State).filter_by(id=2).first()
    updates.name = "New Mexico"
    session.commit()
    session.close()
