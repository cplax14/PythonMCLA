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
sqlstr = "SELECT DISTINCT REPLACE(REPLACE(`ScoreURL`,'http://mcla.us/game/',''),'/score.html','') as GameScoreID,ScoreURL FROM KLGames WHERE ScoreURL IS NOT NULL AND LTRIM(RTRIM(ScoreURL))<>'' ORDER BY `NewScoreURL`  DESC;"
#sqlstr = "SELECT `TeamSlug` FROM `KLTeams` WHERE `TeamSlug` = 'Missouri';"


cur.execute(sqlstr)

for row in cur.fetchall():
	print row[1]