#!/usr/bin/python3
"""a script that lists all states
with a name starting with N (upper N)
from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    " script that lists all states with a name starting with N"
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id")

    result = cursor.fetchall()
    if result:
        for row in result:
            print(row)

    cursor.close()
    db.close()
