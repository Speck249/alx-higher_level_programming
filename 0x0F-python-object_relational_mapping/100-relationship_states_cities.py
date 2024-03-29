#!/usr/bin/python3
"""
Module creates new State & City objects
based on established relationship.
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    """
    Connect to MySQL server and
    retrieve desired data.
    """
    engine = create_engine('mysql+mysqldb://'
                           '{}:{}@localhost:3306/{}'
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    new_state = State(name='California')

    new_city = City(name='San Francisco', parent=new_state)

    new_state.cities.append(new_city)

    session.add(new_state)

    session.add(new_city)

    session.commit()

    session.close()
