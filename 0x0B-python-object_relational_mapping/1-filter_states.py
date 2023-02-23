#!/usr/bin/python3

""" Connects to and queries """

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], database=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name like BINARY 'N%' ORDER BY id")
    fetch = cur.fetchall()
    for row in fetch:
        print(row)
    cur.close()
    db.close()
