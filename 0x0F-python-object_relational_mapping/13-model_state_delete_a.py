#!/usr/bin/python3
"""
Module deletes State objects with names
containing the letter 'a' from database
hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    """
    Connect to MySQL server and
    retrieve desired output.
    """
    engine = create_engine('mysql+mysqldb://{}:'
                           '{}@localhost:3306/{}'
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]))

    Session = sessionmaker(bind=engine)

    session = Session()

    delete_obj = session.query(State).filter(State.name.like('%a%'))\
        .all()

    for obj in delete_obj:
        session.delete(obj)

    session.commit()
