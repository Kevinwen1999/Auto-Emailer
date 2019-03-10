import smtplib

# connect to server
s = smtplib.SMTP(host="smtp.gmail.com", port=587)

# encrpt
s.starttls()

