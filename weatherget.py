#! /usr/bin/python

import urllib2
import config

f = open(config.datapath + '/weather.json','w')

response = urllib2.urlopen(config.forecastweatherurl)
jsonfile = response.read()

f.write(jsonfile)
f.close()

f2 = open(config.datapath + '/forecast.xml','w')

response2 = urllib2.urlopen(config.graphicalweatherurl)
xmlfile = response2.read()
f2.write(xmlfile)
f2.close()
