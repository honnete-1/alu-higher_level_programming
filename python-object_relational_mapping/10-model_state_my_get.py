#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # 3 arguments: username, password, db name
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # MySQL connection string
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query: all states containing 'a'
    states_with_a = session.query(State).filter(State.name.like('%a%')).all()

    # Delete them
    for state in states_with_a:
        session.delete(state)

    # Commit changes
    session.commit()

    session.close()
