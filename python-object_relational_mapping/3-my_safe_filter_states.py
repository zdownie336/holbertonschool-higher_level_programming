#!/usr/bin/python3
"""Module: going through how ORMs work."""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],)
    cur = db.cursor()
    search =("SELECT * FROM states "
            "WHERE name = %s "
            "ORDER BY id ASC")
    cur.execute(search, sys.argv[4])
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
