#!/usr/bin/python3
"""Module is for sqlachemy"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)

    session = Session()

    tables = session.query(State).\
        filter(State.name.like(sys.argv[4])).\
        first()

    if tables is None:
        print("Not found")
    else:
        print(tables.id)
