#!/usr/bin/python3
"""a script that takes in arguments
and displays all values in the states table"""

import MySQLdb
import sys

if __name__ == "__main__":
    "a script that displays all values in the states table"
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name=%s"

    try:
        cursor.execute(query, (sys.argv[4],))
        result = cursor.fetchall()

        for row in result:
            print(row)
    except Exception:
        pass
    finally:
        cursor.close()
        db.close()
