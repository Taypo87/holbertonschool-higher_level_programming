#!/usr/bin/python3

""" Connects to and queries """

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], database=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM cities
        JOIN states ON states.id = cities.state_id
        WHERE states.name LIKE %s""", (argv[4],))
    fetch = cur.fetchall()
    print(", ".join(row[0] for row in fetch))
    cur.close()
    db.close()
