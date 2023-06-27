#!/usr/bin/python3
"""
Module lists the first State object
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
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:'
                           '3306/{}'.format(sys.argv[1],
                                            sys.argv[2],
                                            sys.argv[3]))

    Session = sessionmaker(bind=engine)

    session = Session()

    result = session.query(State).order_by(State.id).first()

    if result is None:
        print('Nothing')
    else:
        print("{}: {}".format(result.id, result.name))
