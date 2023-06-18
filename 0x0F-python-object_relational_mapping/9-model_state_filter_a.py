#!/usr/bin/python3
"""
Module lists State objects with
the letter 'a' in their names
from database hbtn_0e_6_usa.
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

    result = session.query(State).filter\
        (State.name.like('%a%')).order_by\
        (State.id).all()

    for item in result:
        print("{}: {}".format(item.id, item.name))
