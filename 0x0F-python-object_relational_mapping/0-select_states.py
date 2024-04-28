#!/usr/bin/python3
"""A script that lists all states from the database hbtn_0e_0_usa."""


import MySQLdb
from sys import argv

if (__name__ == "__main__"):
    "script that lists all states from the database hbtn_0e_0_usa"
    mydb = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM states ORDER BY id")

    result = mycursor.fetchall()
    for row in result:
        print(row)

    mycursor.close()
    mydb.close()
