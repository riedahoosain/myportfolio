#This is a script that can send emails in Python using gmail
import smtplib, ssl

SUBJECT = "Sent from My Python Portfolio Website"

host = "smtp.gmail.com"
port = 465

username = "innotechsa24@gmail.com"
password = "nvyz ytcl ahrb kjie"

receiver = "innotechsa24@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: Sent from My Python Portfolio Website
Hi!
How are you?
Bye!
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)