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

    session.add(State("Louisiana"))
    session.commit()
    query = session.query(State).order_by(State.id.desc()).first()
    print(query.id)
