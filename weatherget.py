#! /usr/bin/python

import urllib2
import config

f = open(config.datapath + '/weather.json','w')

response = urllib2.urlopen('http://forecast.weather.gov/MapClick.php?lat=40.6676&lon=-73.985&unit=0&lg=english&FcstType=json')
jsonfile = response.read()

f.write(jsonfile)
f.close()

f2 = open(config.datapath + '/forecast.xml','w')

response2 = urllib2.urlopen('http://graphical.weather.gov/xml/sample_products/browser_interface/ndfdXMLclient.php?lat=40.6676&lon=-73.985&product=time-series&temp=temp&wx=wx')
xmlfile = response2.read()
f2.write(xmlfile)
f2.close()
