#!/usr/bin/python3
"""
A script that lists all states,
with a name starting with N (upper N),
from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if (__name__ == "__main__"):
    """A script that lists all states, starting with N (upper N)"""
    mydb = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3]
    )

    mycursor = mydb.cursor()
    query = "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id"
    mycursor.execute(query)
    result = mycursor.fetchall()

    for row in result:
        print(row)

    mycursor.close()
    mydb.close()
