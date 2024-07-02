import json
import urllib
from pprint import pprint
import MySQLdb

db = MySQLdb.connect(host="xxxxx", # your host, usually localhost
                     user="xxxx", # your username
                      passwd="xxxx", # your password
                      db="xxxx") # name of the data base

cur = db.cursor()                      

#EDIT 5-18-2015 JAM: changed the SQL to grab the TeamSlug value, which can be found by cracking open the ScheduleURL value. This value is slightly different for a handful of schools.
sqlstr = "SELECT  `TeamSlug` FROM  `KLTeams` WHERE  `TeamSlug` NOT IN (SELECT  `TeamName` FROM  `KLGames`);"


cur.execute(sqlstr)

for team in cur.fetchall():
	apiteam = team[0]#.replace(" ","_")
	print team[0]
	urltoopen = "http://www.kimonolabs.com/api/ondemand/dtpp5fk8?apikey=Saci2RHbszL9wv4xrNraYX6pGnFYOXZf&kimpath2=%s" % (apiteam)
	response = json.load(urllib.urlopen(urltoopen))
	#pprint (response)
	results1 = response["results"]
	results2 = results1["collection1"]
	for row in results2:
		teamscore = 0
		oppscore = 0
		outcome = row["Score"]["text"][:1]
		score = row["Score"]["text"].replace("W ","").replace("L ","")
		scoresplit = score.split(' - ')
		
		if len(score) > 0:

			if outcome == "W":
				teamscore = scoresplit[0]
				oppscore = scoresplit[1]
			elif outcome == "L":
				oppscore = scoresplit[0]
				teamscore = scoresplit[1]
			else:
				oppscore = 0
				teamscore = 0
		
		#print outcome," ",score," ",scoresplit," ",teamscore," ",oppscore		

		sqlstr = "INSERT INTO `KLGames`(`Date`, `TeamName`,`OppTeamName`,`Outcome`,`Score`,`ScoreURL`,`OppTeamScheduleURL`,`TeamScore`,`OppScore`)VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s');" % (
			row["Date"]["text"].replace("\n"," "),apiteam,row["TeamName"]["text"].replace("@ ","").replace("'",""),outcome,score,row["Score"]["href"],row["TeamName"]["href"],teamscore,oppscore)
		cur.execute(sqlstr)

db.close()		
