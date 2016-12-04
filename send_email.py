import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


fromAddr = 'kaelscion@gmail.com'
toAddr = 'jaimie@ccstechme.com'
msg = MIMEMultipart()
msg['From'] = fromAddr
msg['To'] = toAddr
msg['Subject'] = "Today's Happiness is Here!"

body = 

