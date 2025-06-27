#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    try:
        # Create the engine and connect to the database
        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]
            ),
            pool_pre_ping=True
        )
        # Create a session
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query the first State object
        state = session.query(State).order_by(State.id).first()

        # Print the result
        print("Nothing" if not state else "{}: {}".format(state.id, state.name))

    except Exception as e:
        print(f"Error: {e}")
