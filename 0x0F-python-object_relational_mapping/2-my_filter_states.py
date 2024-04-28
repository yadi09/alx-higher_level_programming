#!/usr/bin/python3
"""
script that takes in an argument,
and displays all values in the states table of hbtn_0e_0_usa,
where name matches the argument.
"""

import MySQLdb
import sys

if (__name__ == "__main__"):
    """displays all values in the states table of hbtn_0e_0_usa,
       where name matches the argument.
    """

    mydb = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3]
    )

    mycursor = mydb.cursor()
    query = "SELECT * FROM states WHERE name = %s"
    mycursor.execute(query, (sys.argv[4],))
    result = mycursor.fetchall()

    for row in result:
        print(row)

    mycursor.close()
    mydb.close()
