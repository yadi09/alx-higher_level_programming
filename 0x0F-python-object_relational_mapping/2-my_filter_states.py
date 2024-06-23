#!/usr/bin/python3
"""a script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument."""

import MySQLdb
import sys

if __name__ == "__main__":
    "script that takes in an argument and displays all values"
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE BINARY name='{:s}'".format(sys.argv[4])
    cursor.execute(query)

    result = cursor.fetchall()
    for row in result:
        print(row)

    cursor.close()
    db.close()
