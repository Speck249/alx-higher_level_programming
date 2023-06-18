#!/usr/bin/python3
"""
Module adds new State object
to database hbtn_0e_6_usa.
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

    new_obj = State(name='Louisiana')

    session.add(new_obj)

    session.commit()

    print("{}".format(new_obj.id))
