#!/usr/bin/python3
"""
Module updates name of State object
in the database hbtn_0e_6_usa.
"""
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
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

    target = session.query(State).get(2)
    target.name = 'New Mexico'
    session.commit()
