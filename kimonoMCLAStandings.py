import json
import urllib
from pprint import pprint
import MySQLdb

db = MySQLdb.connect(host="xxxxx", # your host, usually localhost
                     user="xxxx", # your username
                      passwd="xxxx", # your password
                      db="xxxx") # name of the data base

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


