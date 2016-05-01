#! /usr/bin/python

import urllib2

f = open('/home/pi/Daryl/glancebot/testing.txt','r')
filecontents = f.read()
print filecontents
newfilecontents = int(filecontents) + 1
f.close()

f = open('/home/pi/Daryl/glancebot/testing.txt','w')
f.write(str(newfilecontents))
f.close()
