#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == '__main__':
    db_connection = MySQLdb.connect(user=sys.argv[1],
        password=sys.argv[2], database=sys.argv[3],
        host='localhost', port=3306)

    cursor = db_connection.cursor()
    
    query = "SELECT * FROM states ORDER BY states.id;"
    
    cursor.execute(query)

    result = cursor.fetchall()
    
    for item in result:
        print(item)
