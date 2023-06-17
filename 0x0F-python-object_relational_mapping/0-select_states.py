#!/usr/bin/python3
"""
Module lists all states
from the database hbtn_0e_0_usa.
"""
import sys
import MySQLdb

if __name__ == '__main__':
    """
    Connect to the MySQL server
    and retrieve desired output.
    """
    db_connection = MySQLdb.connect(user=sys.argv[1],
        password=sys.argv[2], database=sys.argv[3],
        host='localhost', port=3306)

    cursor = db_connection.cursor()
    
    cursor.execute("SELECT * FROM states ORDER BY states.id;")

    result = cursor.fetchall()
 
    for item in result:
        print(item)
