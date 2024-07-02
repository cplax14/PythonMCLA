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
sqlstr = "SELECT `TeamSlug` FROM `KLTeams` WHERE `TeamSlug` NOT IN (SELECT `TeamSlug` FROM `KLPlayers`) LIMIT 20;"
#sqlstr = "SELECT `TeamSlug` FROM `KLTeams` WHERE `TeamSlug` = 'Missouri';"


cur.execute(sqlstr)

for team in cur.fetchall():
	try:
		apiteam = team[0]#.replace(" ","_")
		print team[0]
		urltoopen = "http://www.kimonolabs.com/api/ondemand/cm7qivrm?apikey=Saci2RHbszL9wv4xrNraYX6pGnFYOXZf&kimpath2=%s" % (apiteam)
		response = json.load(urllib.urlopen(urltoopen))
		#pprint (response)
		results1 = response["results"]
		results2 = results1["collection1"]	

		#pprint (results2)
		for row in results2:
	#		if row["Number"]["href"]=="http://mcla.us/team/Missouri/2015/#39382":
	#			row["PlayerName"]["text"] = "O'Keefe, Riley"

			sqlstr = "INSERT INTO `KLPlayers`(`PlayerName`,`TeamSlug`, `Height`,`Weight`,`HighSchool`,`Hometown`,`Number`,`NumberURL`,`Position`,`Year`,`PlayerNameURL`)VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');" % (
				row["PlayerName"]["text"].replace("'","''"),apiteam,row["Height"].replace("'","''"),row["Weight"],row["HighSchool"].replace("'","''"),row["Hometown"].replace("'","''"),row["Number"]["text"],row["Number"]["href"],row["Position"],row["Year"],row["PlayerName"]["href"])
		#	print(sqlstr)
			cur.execute(sqlstr)
		sleep(2)
	except:
		apiteam = team[0]#.replace(" ","_")
		print team[0]
		urltoopen = "http://www.kimonolabs.com/api/ondemand/cm7qivrm?apikey=Saci2RHbszL9wv4xrNraYX6pGnFYOXZf&kimpath2=%s" % (apiteam)
		response = json.load(urllib.urlopen(urltoopen))
		#pprint (response)
		results1 = response["results"]
		results2 = results1["collection1"]	

		#pprint (results2)
		for row in results2:
	#		if row["Number"]["href"]=="http://mcla.us/team/Missouri/2015/#39382":
	#			row["PlayerName"]["text"] = "O'Keefe, Riley"

			sqlstr = "INSERT INTO `KLPlayers`(`PlayerName`,`TeamSlug`, `Height`,`Weight`,`HighSchool`,`Hometown`,`Number`,`NumberURL`,`Position`,`Year`,`PlayerNameURL`)VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');" % (
				row["PlayerName"]["text"].replace("'","''"),apiteam,row["Height"].replace("'","''"),row["Weight"],row["HighSchool"].replace("'","''"),row["Hometown"].replace("'","''"),row["Number"]["text"],row["Number"]["href"],row["Position"],row["Year"],row["PlayerName"]["href"])
		#	print(sqlstr)
			cur.execute(sqlstr)
		sleep(2)

db.close()		
