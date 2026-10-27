#!/usr/bin/python3
"""Module: selecting specific parameters for ORM."""

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
    search = (
                "SELECT cities.name FROM cities "
                "INNER JOIN states "
                "ON cities.states_id = states.id"
                "WHERE states.name LIKE BINARY %s "
                "ORDER BY cities.id ASC")
    cur.execute(search, (sys.argv[4]),)
    rows = cur.fetchall()
    for row in rows:
        print(row, end=", ")
    cur.close()
