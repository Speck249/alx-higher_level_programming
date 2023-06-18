#!/usr/bin/python3
"""
Module contains scripts that is
safe from MySQL injections.
"""
import sys
import MySQLdb

if __name__ == '__main__':
    """
    Connect to MySQL server and
    retrieve desired output.
    """
    db_connection = MySQLdb.connect(user=sys.argv[1],
                                    password=sys.argv[2],
                                    database=sys.argv[3],
                                    host='localhost', port=3306)

    state_searched = sys.argv[4]

    cursor = db_connection.cursor()

    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY"
                   " states.id;", (state_searched,))

    result = cursor.fetchall()

    for result in cursor:
        print(result)

    cursor.close()

    db_connection.close()
