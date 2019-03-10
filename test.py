import smtplib

# connect to server
s = smtplib.SMTP(host='smtp.gmail.com', port=587)

# encrypt
s.starttls()

username = "user069152"
password = "pass069152"
msg = "Hello, this is a test"

# login
s.login(username, password)

counter = 0
while counter < 50:
    s.sendmail(username + "@gmail.com", username + "@gmail.com", msg)
    counter += 1
