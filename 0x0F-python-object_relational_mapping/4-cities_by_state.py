#!/usr/bin/python3
"""a script that lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    "a script that lists all cities from the database hbtn_0e_4_usa"
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        port=3306,
        db=sys.argv[3]
    )

    cursor = db.cursor()
    query = "\
SELECT cities.id, cities.name, states.name\
 FROM cities\
 JOIN states ON cities.state_id = states.id"

    cursor.execute(query)
    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    db.close()
