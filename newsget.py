import urllib2
import config

f = open(config.datapath + '/news.xml','w')

response = urllib2.urlopen('http://feeds.reuters.com/reuters/topNews')
xmlfile = response.read()

f.write(xmlfile)
f.close()
