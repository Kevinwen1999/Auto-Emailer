import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


# server.sendmail(from, to, msg)
from_user = "user069152@gmail.com"
password = "pass069152"
to_user = from_user

# msg config
subject = "u fuk"

msg = MIMEMultipart()
msg['From'] =  from_user
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
part.add_header('Content-Disposition', "attachment: filename = " + filename)
msg.attach(part)

email_text = msg.as_string()

# connect to server
server = smtplib.SMTP(host='smtp.gmail.com', port=587)

# encrypt
server.starttls()

# login
server.login(from_user, password)

# spammer
counter = 0
while counter < 50:
    server.sendmail(from_user, to_user, email_text)
    counter += 1

server.quit()