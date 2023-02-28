#!/usr/bin/python3
"""Lists state object that matches argument passed """

import sqlalchemy
from sqlalchemy import create_engine, select
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = select(State).where(State.name.like('{}'.format(argv[4])))
    results = engine.execute(query).fetchall()
    if results is not None:
        for record in results:
            print("{}".format(record.id))
    else:
        print("Not found")
    session.close()
