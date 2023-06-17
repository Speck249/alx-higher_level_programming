#!/usr/bin/python3
"""
Module lists all states with name
starting with N from database hbtn_0e_0_usa.
"""
import sys
import MySQLdb

if __name__ == '__main__':
    """
    Connect to MySQL and
    retrieve desired output.
    """
    db_connection = MySQLdb.connect(user=sys.argv[1],
        password=sys.argv[2], database=sys.argv[3],
        host='localhost', port=3306)

    cursor = db_connection.cursor()
    
    query = "SELECT * FROM states \
            WHERE BINARY name LIKE 'N%' \
            ORDER BY states.id;"
    
    cursor.execute(query)
    
    result = cursor.fetchall()

    for item in result:
        print(item)

    cursor.close()
    db_connection.close()
