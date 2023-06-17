#!/usr/bin/python3
"""
Module displays all cities of a state
passed as an argument
"""
import sys
import MySQLdb

if __name__ == '__main__':
    """
    Connect to MySQL server and
    retrieve desired output.
    """
    db_connection = MySQLdb.connect(user=sys.argv[1],
        password=sys.argv[2], database=sys.argv[3],
        host='localhost', port=3306)

    state_name = sys.argv[4]

    cursor = db_connection.cursor()

    cursor.execute("SELECT cities.id, cities.name, states.name \
            FROM cities \
            JOIN states ON cities.state_id = states.id \
            WHERE states.name = '{}' \
            ORDER BY states.id;".format(state_name))

    result = cursor.fetchall()

    print(", ".join([item[1] for item in result]))

    cursor.close()
    db_connection.close()
