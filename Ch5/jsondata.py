#
# Example for retrieving data in json
#

import urllib.request
import json


def printResults(data):

	# Use the json module to load the string data into a python object
	theJSON = json.loads(data)
	
	# now we can access contents of the JSON like any other Python object

	if "title" in theJSON["metadata"]:
		print(theJSON["metadata"]["title"])
		
	# output the number of events followed by each event magnitude and place.
	count = theJSON["metadata"]["count"]
	print (str(count) + " events recorded.")
	
	for i in theJSON["features"]:
		print(i["properties"]["place"])
	print("------------")
		
	# print events greater than magnitude 4.0
	for i in theJSON["features"]:
		if i["properties"]["mag"] >= 4.0:
			print ("%2.1f" % i["properties"]["mag"],  i["properties"]["place"])
	print("------------")			
	# print events people reported feeling, "felt" events
	print("events people reported feeling, 'felt' events:")
	for i in theJSON["features"]:
		if i["properties"]["felt"] != None:
			if i["properties"]["felt"] > 0:
				print ("%2.1f" % i["properties"]["mag"],  i["properties"]["place"],
			       " Was reported felt by: ", i["properties"]["felt"])
	print("------------")	
def main():

	
	# variable using free data from USGS, lists earthquakes for the last
	# day larger than Mag 2.5
	urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
	
	# open and read variable
	webUrl = urllib.request.urlopen(urlData)
	print ("result code: " + str(webUrl.getcode()))
	if (webUrl.getcode() == 200):
		data = webUrl.read()
		printResults(data)
	else:
		print("Received error, cannot parse results")
		

if __name__ == "__main__":
	main()