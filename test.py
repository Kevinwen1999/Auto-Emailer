import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import time
import datetime
import string
import random


# server.sendmail(from, to, msg)
from_user = "user069152@gmail.com"
password = "pass069152"
to_user = "user069152@gmail.com"

# msg config
subject = "u fuk"

msg = MIMEMultipart()
msg['From'] = from_user
msg['To'] = to_user
msg['Subject'] = subject

body = "fag"
msg.attach(MIMEText(body, 'plain'))

# Attachments
filename = 'fucku.txt'
attachment = open(filename, 'rb')

part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment', filename=filename)
msg.attach(part)

# Image

img_source = "https://www.macleans.ca/wp-content/uploads/2012/03/canada-goose-e1330966200413.jpg"
msgText = MIMEText('<img src="%s">' % img_source, 'html')
msg.attach(msgText)   # Added, and edited the previous line


email_text = msg.as_string()


# connect to server
server = smtplib.SMTP(host='smtp.gmail.com', port=587)

# encrypt
server.starttls()

# login
server.login(from_user, password)

# spammer

def spammer(n):
    counter = 0
    while counter < n:
        server.sendmail(from_user, to_user, email_text)
        counter += 1
    print("Sent Successfully: ", counter)

def send_at(date, to):
    sec = (date - datetime.datetime.now()).total_seconds()
    time.sleep(sec)
    server.sendmail(from_user, to_user, email_text)

def msg_generator(n = random.randint(1, 100), chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(n))



spammer(5)
server.quit()
