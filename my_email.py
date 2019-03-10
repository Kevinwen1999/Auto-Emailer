import smtplib
import time
import datetime
import string
import random

# s.sendmail(from, to, msg)
username = "user069152"
password = "pass069152"
msg = "Hello, this is a test"

# connect to server
s = smtplib.SMTP(host='smtp.gmail.com', port=587)

# encrypt
s.starttls()

# login
s.login(username, password)

# spammer
def spammer(n, to):
    while n >= 0:
        msg = msg_generator()
        s.sendmail(username + "@gmail.com", to, msg)
        n -= 1

# send at certain time
# date must be in datetime format
# example
"""
send_at(datetime.datetime.now(), username + "@gmail.com")
"""
def send_at(date, to):
    sec = (date - datetime.datetime.now()).total_seconds()
    time.sleep(sec)
    s.sendmail(username + "@gmail.com", to, msg)

def msg_generator(n = random.randint(1, 100), chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(n))
