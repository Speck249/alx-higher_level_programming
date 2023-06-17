#!/usr/bin/python3
"""
Module lists the id of the first
State object that matches search term
from database hbtn_0e_6_usa.
"""
from sqlalchemy import create_engine, or_
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import argparse
import sys

if __name__  == '__main__':
    """
    Connect to MySQL server and
    retrieve the desired output.
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).filter(State.name == sys.argv[4]).first()

    if result is None:
        print('Not found')
    else:
        print("{}".format(result.id))
