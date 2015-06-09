#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="cplax14MySQL1.db.10018706.hostedresource.com", # your host, usually localhost
                     user="cplax14MySQL1", # your username
                      passwd="MySQL!@#1", # your password
                      db="cplax14MySQL1") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor() 

# Use all the SQL you like
cur.execute("SELECT * FROM Games;")

# print all the first cell of all the rows
for row in cur.fetchall() :
    print (row[0], row[1],row[2],row[3],row[4])

db.close()
