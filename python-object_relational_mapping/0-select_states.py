#!/usr/bin/python3
import MySQLdb

db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="hbtn_0e_0_usa")
cur = db.cursor()
cur.execute("SELECT id ,states FROM hbtn_0e_0_usa ORDER BY states.id ASC")
