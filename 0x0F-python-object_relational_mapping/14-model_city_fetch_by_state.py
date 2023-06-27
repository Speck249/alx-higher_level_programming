#!/usr/bin/python3
"""
Module prints all City objects
from database hbtn_0e_14_usa.
"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
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

    result = session.query(State, City).join(State).all()

    for state, city in result:
        print("{}: ({}) {}".format(state.name, city.id,
                                   city.name))

    session.close()
