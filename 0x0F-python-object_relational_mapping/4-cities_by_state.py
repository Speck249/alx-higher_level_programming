#!/usr/bin/python3
"""
Module lists all cities from
database hbtn_0e_4_usa.
"""
import sys
import MySQLdb

if __name__ == '__main__':
    """
    Connect to MySQL server
    and retrieve output.
    """
    db_connection = MySQLdb.connect(user=sys.argv[1],
                                    password=sys.argv[2],
                                    database=sys.argv[3],
                                    host='localhost', port=3306)

    cursor = db_connection.cursor()

    query = "SELECT cities.id, cities.name, states.name FROM " \
            "cities INNER JOIN states ON cities.state_id = states.id;"

    cursor.execute(query)

    result = cursor.fetchall()

    for item in result:
        print(item)

    cursor.close()

    db_connection.close()
