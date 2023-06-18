#!/usr/bin/python3
"""
Module lists all states whose
names match search term.
"""
import sys
import MySQLdb

if __name__ == '__main__':
    """
    Connect to MySQL server and
    display desired output.
    """
    db_connection = MySQLdb.connect(user=sys.argv[1],
                                    password=sys.argv[2],
                                    database=sys.argv[3],
                                    host='localhost', port=3306)

    cursor = db_connection.cursor()

    state_searched = sys.argv[4]

    query = "SELECT * FROM states WHERE name LIKE BINARY " \
            "'{}' ORDER BY states.id;".format(state_searched)

    cursor.execute(query)

    result = cursor.fetchall()

    for item in result:
        print(item)

    cursor.close()

    db_connection.close()
