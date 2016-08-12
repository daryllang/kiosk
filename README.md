# Daryl's Weather/Twitter Kiosk

* Designed for a Raspberry Pi with 7" screen (800 x 480 pixels)
* Author: Daryl Lang <daryl@daryllang.com>

## Environment setup

Let's see. Make sure you have Python.
```
python -V
```
And you'll definitely need Python Twitter.
```
sudo pip install python-twitter
```

You'll want to be running a web server. If you need one go ahead an get Nginx...
``` 
sudo apt-get install nginx
sudo /etc/init.d/nginx start
```
View /etc/nginx/sites-enabled/default to see where your root web directory is, or to change it if you want. You'll want to clone this repository into a folder that your web browser recognizes, like "/var/www", or a subfolder like "/var/www/kiosk".

Need a web browser? See https://www.raspberrypi.org/forums/viewtopic.php?f=63&t=121195 for how to install Chromium on a Raspberry Pi. This should get you a working copy of Chromium:

```
wget -qO - http://bintray.com/user/downloadSubjectPublicKey?username=bintray | sudo apt-key add -
echo "deb http://dl.bintray.com/kusti8/chromium-rpi jessie main" | sudo tee -a /etc/apt/sources.list
sudo apt-get update
sudo apt-get install chromium-browser
```

## The Kiosk config file

Fill in the values for config-sample.py and save it as config.py. You'll need to set up a Twitter app if you haven't already.

## How do I config the twitter.py script?

The Twitter script attached is designed specifically to pull from 2 feeds, @NYCTSubway for the New York City subway and @NotifyNYC NYC emergency alerts. You can modify it for other feeds.

## Cron

You'll want to run these 3 scripts on a cron.
```
crontab -e
```
Then add these lines to your crontab file to run the twitter script every minute, the weather script every 3 minutes, and the news feed script every 10 minutes. They write data to tweets.json, weather.json, forecast.xml, and news.xml.

```
* * * * * python /home/daryluser/kiosk/twitterget.py
*/3 * * * * python /home/daryluser/kiosk/weatherget.py
*/10 * * * * python /home/daryluser/kiosk/newsget.py
```

## The design for the home page

The file that you'll load in your browser to see all the data you've pulled is index.html. It reads data once a second from tweets.json, weather.json, forecast.xml, and news.xml. It refreshes every 15 minutes. Styling is in style.css.

## Running this screen as a kiosk with a Raspberry Pi display.

Depending on your screen setup, some version of this code will load the Chromium browser and display whatever your root directory's home page is in kiosk mode.

```
startx &
chromium-browser --display=:0 --kiosk --disable-session-crashed-bubble --disable-infobars http://localhost/ & 
```
This is helpful if things go wrong -- Clearing the Chromium cache. (Assumes your username is username)
```
sudo rm -r  /home/username/.cache/chromium/Default/Cache/*
```
