#!/usr/bin/python
import urllib2
import json


continent = raw_input("Enter continent: ")

j = urllib2.urlopen('http://restcountries.eu/rest/v1/region/' + continent)
j_obj = json.load(j)
length= len(j_obj)
for country in j_obj:
	print country['name'] 



