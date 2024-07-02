import json
import urllib
from pprint import pprint
import MySQLdb
from time import sleep

db = MySQLdb.connect(host="xxxxx", # your host, usually localhost
                     user="xxxx", # your username
                      passwd="xxxx", # your password
                      db="xxxx") # name of the data base

cur = db.cursor()                      

#EDIT 5-18-2015 JAM: changed the SQL to grab the TeamSlug value, which can be found by cracking open the ScheduleURL value. This value is slightly different for a handful of schools.
sqlstr = "SELECT DISTINCT REPLACE(REPLACE(`ScoreURL`,'http://mcla.us/game/',''),'/score.html','') as GameScoreID,ScoreURL FROM KLGames WHERE ScoreURL IS NOT NULL AND LTRIM(RTRIM(ScoreURL))<>'' ORDER BY `NewScoreURL`  DESC;"
#sqlstr = "SELECT `TeamSlug` FROM `KLTeams` WHERE `TeamSlug` = 'Missouri';"


cur.execute(sqlstr)

for row in cur.fetchall():
	print row[1]
