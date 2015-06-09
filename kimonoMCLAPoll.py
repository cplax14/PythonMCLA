import json
import urllib
from pprint import pprint
import MySQLdb
from time import sleep

db = MySQLdb.connect(host="cplax14MySQL1.db.10018706.hostedresource.com", # your host, usually localhost
                     user="cplax14MySQL1", # your username
                      passwd="MySQL!@#1", # your password
                      db="cplax14MySQL1") # name of the data base

cur = db.cursor()                      

#for row in cur.fetchall():
	#try:
		#GameScoreID = row[0]#.replace(" ","_")
		#print row[0]
urltoopen = "https://www.kimonolabs.com/api/4k1nlw2c?apikey=Saci2RHbszL9wv4xrNraYX6pGnFYOXZf"
response = json.load(urllib.urlopen(urltoopen))
#pprint (response)
results1 = response["results"]
top25 = results1["Top25"]
pprint(top25)


# try:

for row in top25:
	#faceoffstats = row["FieldPlayerFaceOff"].split('-')
	#faceoffwins = faceoffstats[0]
	#faceofflosses = faceoffstats[1]
	recordsplit = row["Record"].split("-")
	wins = recordsplit[0]
	losses = recordsplit[1]
	if row["PreviousRank"] and not row["PreviousRank"].isspace():
		previousrank = row["PreviousRank"]
	else:
		previousrank = 0

	sqlstr = """INSERT INTO `KLPoll`(`TeamName`,`TeamNameURL`, `Record`,`Rank`,`PreviousRank`,`Wins`,`Losses`,`PollPoints`)
	VALUES('%s','%s','%s','%s','%s','%s','%s','%s');""" % (
		row["Team"]["text"].replace("'","''"),row["Team"]["href"],row["Record"], row["Rank"],previousrank,wins,losses,row["PollPoints"])
	#	print(sqlstr)
	cur.execute(sqlstr)


#if len(results1) > 0:
#	fieldplayers = results1["FieldPlayers"]	
#	goalies = results1["Goalies"]