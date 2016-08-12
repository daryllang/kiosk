# Daryl's Weather/Twitter Kiosk

* Designed for a Raspberry Pi screen
* Author: Daryl Lang <daryl@daryllang.com>

## Environment setup

Let's see. You'll definitely need Python Twitter 
```
sudo pip install python-twitter
```

If you're planning to use this machine to run the scripts, serve the web pages, and display the webpages, you'll want to be running a web server like Nginx...
``` 
sudo apt-get install nginx
sudo /etc/init.d/nginx start
```
View /etc/nginx/sites-enabled/default to see where your root web directory is, or to change it if you want.

See https://www.raspberrypi.org/forums/viewtopic.php?f=63&t=121195 for how to install Chromium on a Raspberry Pi. This worked for me:

```
wget -qO - http://bintray.com/user/downloadSubjectPublicKey?username=bintray | sudo apt-key add -
echo "deb http://dl.bintray.com/kusti8/chromium-rpi jessie main" | sudo tee -a /etc/apt/sources.list
sudo apt-get update
sudo apt-get install chromium-browser
```

## This program's config file

Fill in the values for config-sample.py and save it as config.py.

## Twitter script

The Twitter script attached is designed specifically to pull from 2 feeds, for the New York City subway and NYC emergency alerts. You can modify it for other feeds.

## Cron

You'll want to run these 3 scripts on a cron.
```
crontab -e
```
Then add these lines to your crontab file to run the twitter script every minute, the news feed script every 10 minutes, and the weather script every 3 minutes. 
```
* * * * * python /home/daryluser/kiosk/twitterget.py
*/10 * * * * python /home/daryluser/kiosk/newsget.py
*/3 * * * * python /home/daryluser/kiosk/weatherget.py
```

## Running this screen as a kiosk

Depending on your screen setup, some version of this code in a script that runs at login will load the Chromium browser and display whatever your root directory's home page is in kiosk mode.

```
startx &
chromium-browser --display=:0 --kiosk --disable-session-crashed-bubble --disable-infobars http://localhost/ & 
```
This is helpful if things go wrong -- Clearing the Chromium cache. (Assumes your username is username)
```
sudo rm -r  /home/username/.cache/chromium/Default/Cache/*
```
