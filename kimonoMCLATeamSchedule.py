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

sqlstr = "SELECT `TeamName` FROM `KLTeams` LIMIT 1;"

cur.execute(sqlstr)

for team in cur.fetchall():
	apiteam = team[0]
	#print team[0]
	urltoopen = "http://www.kimonolabs.com/api/ondemand/dtpp5fk8?apikey=Saci2RHbszL9wv4xrNraYX6pGnFYOXZf&kimpath2=%s" % (apiteam)
	response = json.load(urllib.urlopen(urltoopen))
	results1 = response["results"]
	results2 = results1["collection1"]
	for row in results2:
	#sqlstr = "INSERT INTO `KLGames`(`Date`, `TeamName`,`OppTeamName`,`Outcome`,`Score`,`ScoreURL`,`OppTeamScheduleURL`)VALUES('%s','%s','%s','%s','%s','%s','%s');" % (
	#	row["Date"]["text"].replace("\n"," "),apiteam,row["TeamName"]["text"].replace("@ ",""),row["Score"]["text"][:1],row["Score"]["text"].replace("W ",""),row["Score"]["href"],row["TeamName"]["href"])
	#print sqlstr
	#cur.execute(sqlstr)


#response = json.load(urllib.urlopen("https://www.kimonolabs.com/api/dtpp5fk8?apikey=Saci2RHbszL9wv4xrNraYX6pGnFYOXZf"))
#response = json.load(urllib.urlopen("http://www.kimonolabs.com/api/ondemand/dtpp5fk8?apikey=Saci2RHbszL9wv4xrNraYX6pGnFYOXZf&kimpath2=Davenport"))

#print results.items()


#topnresults = results[:2]

#pprint (response)


#for k in results2:
#for k in response:
#	print k
#print k["Date"]["text"].replace("\n"," "),k["Date"]["href"],k["Score"]["text"],k["TeamName"]["text"],k["TeamName"]["href"]
#print k["Name"]["text"]," ",k["Name"]["href"]
#print k["results"]["collection1"]

#pprint (results2)

#for k,v in topnresults:
#	print "key: ",k," value: ",v

# Use all the SQL you like
#cur.execute("SELECT * FROM Games;")

# print all the first cell of all the rows
db.close()
