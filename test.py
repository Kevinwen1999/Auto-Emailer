import smtplib

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
counter = 0
while counter < 50:
    s.sendmail(username + "@gmail.com", username + "@gmail.com", msg)
    counter += 1
