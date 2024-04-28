#!/usr/bin/python3
"""
A script that takes in the name of a state as an argument
and lists all cities of that state,
using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if (__name__ == "__main__"):
    """script that takes in the name of a state as an argument"""
    mydb = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    mycursor = mydb.cursor()
    mycursor.execute("""
        SELECT cities.name FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name LIKE BINARY %(states_name)s
        ORDER BY cities.id ASC
        """, {
            'states_name': sys.argv[4]
        }
    )

    result = mycursor.fetchall()
    cities = ", ".join([row[0] for row in result])
    print(cities)

    mycursor.close()
    mydb.close()
