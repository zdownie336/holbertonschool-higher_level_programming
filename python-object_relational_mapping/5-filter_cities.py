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
                "SELECT cities.name FROM states "
                "INNER JOIN cities "
                "ON states.id = cities.state_id "
                "WHERE states.name = %s "
                "ORDER BY cities.id ASC")
    cur.execute(search, (sys.argv[4],))
    rows = cur.fetchall()
    seperator = ''
    for row in rows:
        print(seperator, end='')
        print(row[0], end='')
        seperator = ', '
    print()
    cur.close()
    db.close()
