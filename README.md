Preliminary script for sending yourself weekly weather forecasts powered by forecast.io

I know there are other services for this similar thing, but as with everything I prefer them if they are pushed to me rather than me having to go pull it.


Anyway there are multiple ways to do this, I have in the past used phantomjs to take screenshots rather than selenium. 

This is just a python script that uses selenium in order to take a screenshot of forecast.io then uses smtplib to email the picture to yourself.

(Also works with forcast.io's lines or pretty much any other web page.)

## Configuring

You will need to input your lat/longitude and also some email account's password to use gmail's SMTP server (or change it yourself if you like)

You probably would like a cron task to run this I just have something like 

`0 20 * * 7 python morning_weather.py`

which would send me a forecast on Sunday night.

## DISCLAIMER

Do whatever you like with this, I wrote it for myself (and writing this readme took longer). So it was just a very quick job of sticking together two scripts. Happy to take pull or feature requests 

