import json
import urllib
from pprint import pprint
response = json.load(urllib.urlopen("https://www.kimonolabs.com/api/alloziy2?apikey=Saci2RHbszL9wv4xrNraYX6pGnFYOXZf"))

#print results.items()


#topnresults = results[:2]

#pprint (topnresults)
results1 = response["results"]
results2 = results1["collection1"]

for k in results2:
	#print k["Name"]["text"]
	print k["Name"]["text"]," ",k["Name"]["href"]

#pprint (results2)

#for k,v in topnresults:
#	print "key: ",k," value: ",v
