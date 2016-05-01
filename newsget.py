import urllib2
import config

f = open(config.datapath + '/news.xml','w')

response = urllib2.urlopen('http://feeds.abcnews.com/abcnews/topstories')
xmlfile = response.read()

print "OK"

f.write(xmlfile)
f.close()
