#! /usr/bin/python

import twitter
import config

api = twitter.Api(consumer_key=config.consumer_key_var, consumer_secret=config.consumer_secret_var, access_token_key=config.access_token_var, access_token_secret=config.access_token_secret_var)

tweetsindex = '{ '

#Begin transit query

results = api.GetUserTimeline(screen_name="NYCTSubway", count=8, include_rts=False, exclude_replies=True)

transittweetgroup = '"transit" : { "tweets": ['
transittimesgroup = '"times": ['

first = True
for tweet in results:
     if first:
         first = False
     else:
         transittweetgroup = transittweetgroup + ","
         transittimesgroup = transittimesgroup + ","
     scrubbedtweet = tweet.text
     scrubbedtweet = scrubbedtweet.replace('"','\\"').replace('\n', ' ').replace('\r', ' ')
     scrubbedtweet = scrubbedtweet.replace("#ServiceAlert:"," ")
     scrubbedtweet = scrubbedtweet.encode('ascii', 'ignore')
     transittweetgroup = transittweetgroup + '"' + scrubbedtweet + '"'
     transittimesgroup = transittimesgroup + '"' + tweet.created_at + '"'    

transittweetgroup = transittweetgroup + '],'
transittimesgroup = transittimesgroup + ']'
tweetsindex = tweetsindex + transittweetgroup + transittimesgroup + '}, '

#Begin notify query

results = api.GetUserTimeline(screen_name="NotifyNYC", count=8, include_rts=False, exclude_replies=True)

notifytweetgroup = '"notify" : { "tweets": ['
notifytimesgroup = '"times": ['

first = True
for tweet in results:
     if first:
         first = False
     else:
         notifytweetgroup = notifytweetgroup + ","
         notifytimesgroup = notifytimesgroup + ","
     scrubbedtweet = tweet.text.encode('ascii', 'ignore')
     scrubbedtweet = scrubbedtweet.replace('"','\\"').replace('\n', ' ').replace('\r',' ')
     notifytweetgroup = notifytweetgroup + '"' + scrubbedtweet + '"'
     notifytimesgroup = notifytimesgroup + '"' + tweet.created_at + '"'

notifytweetgroup = notifytweetgroup + '],'
notifytimesgroup = notifytimesgroup + ']'
tweetsindex = tweetsindex + notifytweetgroup + notifytimesgroup + '}'



#Close it out and write to file

tweetsindex = tweetsindex + '}'

f = open(config.datapath + '/tweets.json','w')
f.write(tweetsindex)
f.close()