#!/usr/bin/python3
"""
A script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if (__name__ == "__main__"):
    """
    script that lists all cities from the database hbtn_0e_4_usa
    """
    mydb = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    mycursor = mydb.cursor()
    mycursor.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        INNER JOIN states
        ON cities.state_id = states.id
    """)

    result = mycursor.fetchall()

    for row in result:
        print(row)

    mycursor.close()
    mydb.close()
