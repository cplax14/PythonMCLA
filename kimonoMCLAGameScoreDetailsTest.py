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

#EDIT 5-18-2015 JAM: changed the SQL to grab the TeamSlug value, which can be found by cracking open the ScheduleURL value. This value is slightly different for a handful of schools.
sqlstr = """SELECT DISTINCT REPLACE(REPLACE(`ScoreURL`,'http://mcla.us/game/',''),'/score.html','') as GameScoreID 
			FROM KLGames 
			WHERE ScoreURL IS NOT NULL AND LTRIM(RTRIM(ScoreURL))<>''  AND 
			REPLACE(REPLACE(`ScoreURL`,'http://mcla.us/game/',''),'/score.html','') IN (16900)

			ORDER BY `GameScoreID`  DESC LIMIT 10;"""
#sqlstr = "SELECT `TeamSlug` FROM `KLTeams` WHERE `TeamSlug` = 'Missouri';"


cur.execute(sqlstr)

for row in cur.fetchall():
	#try:
		GameScoreID = row[0]#.replace(" ","_")
		print row[0]
		urltoopen = "http://www.kimonolabs.com/api/ondemand/8ql6u7ne?apikey=Saci2RHbszL9wv4xrNraYX6pGnFYOXZf&kimpath2=%s" % (GameScoreID)
		response = json.load(urllib.urlopen(urltoopen))
		#pprint (response)
		results1 = response["results"]
		pprint(results1)
		#if len(results1) > 0:
		#	fieldplayers = results1["FieldPlayers"]	
		#	goalies = results1["Goalies"]