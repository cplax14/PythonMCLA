#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="xxxxx", # your host, usually localhost
                     user="xxxx", # your username
                      passwd="xxxx", # your password
                      db="xxxx") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor() 

# Use all the SQL you like
cur.execute("SELECT * FROM Games;")

# print all the first cell of all the rows
for row in cur.fetchall() :
    print (row[0], row[1],row[2],row[3],row[4])

db.close()
