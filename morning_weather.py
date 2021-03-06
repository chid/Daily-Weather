from selenium import webdriver
from PIL import Image

fox = webdriver.Firefox()
# set your GPS location
fox.get('http://forecast.io/?q=LATITUDE,LONGITUDE')

# Credentials (if needed)  
username = "****@gmail.com"
password = "****"
strTo = 'PUT YOUR EMAIL HERE'


import time
time.sleep(10)
fox.execute_script('$(".c")[0].click()')  # if you want celcius
time.sleep(2)
fox.save_screenshot('screenshot.png') # saves screenshot of entire page
fox.quit()

# Send an HTML email with an embedded image and a plain text message for
# email clients that don't want to display the HTML.

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage


# Define these once; use them twice!
strFrom = 'from@example.com'

# Create the root message and fill in the from, to, and subject headers
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'Morning Weather'
msgRoot['From'] = strFrom
msgRoot['To'] = strTo
msgRoot.preamble = 'This is a multi-part message in MIME format.'

# Encapsulate the plain and HTML versions of the message body in an
# 'alternative' part, so message agents can decide which they want to display.
msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

msgText = MIMEText('This is the alternative plain text message.')
msgAlternative.attach(msgText)

# We reference the image in the IMG SRC attribute by the ID we give it below
# msgText = MIMEText('<b>Some <i>HTML</i> text</b> and an image.<br><img src="cid:image1"><br>Nifty!', 'html')
msgText = MIMEText('<img src="cid:image1">', 'html')
msgAlternative.attach(msgText)

# This example assumes the image is in the current directory
fp = open('screenshot.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# Define the image's ID as referenced above
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)

# Send the email (this example assumes SMTP authentication is required)
import smtplib
##smtp = smtplib.SMTP()
##smtp.connect('smtp.example.com')
##smtp.login('exampleuser', 'examplepass')
##smtp.sendmail(strFrom, strTo, msgRoot.as_string())
##smtp.quit()


# The actual mail send  
server = smtplib.SMTP('smtp.gmail.com:587')  
server.starttls()  
server.login(username,password)  
server.sendmail(strFrom, strTo, msgRoot.as_string()) 
server.quit()  
