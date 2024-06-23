#!/usr/bin/python3
"""a script that takes in the name of a state as an argument
and lists all cities"""

import MySQLdb
import sys


if __name__ == "__main__":
    "a script that takes in the name of a state as an argument\
    and lists all cities"
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    query = "\
    SELECT cities.name FROM cities WHERE cities.state_id = (\
    SELECT id FROM states WHERE states.name = %s)"

    cursor.execute(query, (sys.argv[4],))
    result = cursor.fetchall()
    cities = ", ".join([row[0] for row in result])
    print(cities)

    cursor.close()
    db.close()
