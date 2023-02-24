#!/usr/bin/python3

""" Connects to and queries """

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], database=argv[3])

    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE NAME = '{}' ORDER BY id".format(argv[4]))
    fetch = cur.fetchall()
    for row in fetch:
        if row[1] == argv[4]:
            print(row)
    cur.close()
    db.close()
