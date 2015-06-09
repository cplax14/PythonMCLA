import json
import urllib
from pprint import pprint
import MySQLdb

db = MySQLdb.connect(host="cplax14MySQL1.db.10018706.hostedresource.com", # your host, usually localhost
                     user="cplax14MySQL1", # your username
                      passwd="MySQL!@#1", # your password
                      db="cplax14MySQL1") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor() 

response = json.load(urllib.urlopen("https://www.kimonolabs.com/api/a0t3sjho?apikey=Saci2RHbszL9wv4xrNraYX6pGnFYOXZf"))

results1 = response["results"]
results2 = results1["collection1"]

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor() 

# Use all the SQL you like
#cur.execute("SELECT * FROM Games;")

# print all the first cell of all the rows
for row in results2:
    #sqlstr = "INSERT INTO `KLTeams`(`TeamName`, `ScheduleURL`,`DivisionRecord`,`OverallRecord`,`GoalsFor`,`GoalsAgainst`)VALUES(`%s`,`%s`,`%s`,`%s`,`%s`,`%s`);" % (
    #sqlstr = "INSERT INTO `KLTeams`(`TeamName`, `ScheduleURL`,`DivisionRecord`,`OverallRecord`,`GoalsFor`,`GoalsAgainst`)VALUES(%s,%s,%s,%s,%s,%s);" % (
    sqlstr = "INSERT INTO `KLTeams`(`TeamName`, `ScheduleURL`,`DivisionRecord`,`OverallRecord`,`GoalsFor`,`GoalsAgainst`)VALUES('%s','%s','%s','%s','%s','%s');" % (
    	row["TeamName"]["text"],row["TeamName"]["href"],row["DivisionRecord"],row["OverallRecord"],row["GoalsFor"],row["GoalsAgainst"])
    	
    cur.execute(sqlstr)

    	

db.close()


