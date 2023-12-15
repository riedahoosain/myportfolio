#This is a script that can send emails in Python using gmail
import smtplib, ssl


def send_email(message):

    SUBJECT = "Sent from My Python Portfolio Website"

    host = "smtp.gmail.com"
    port = 465

    username = "innotechsa24@gmail.com"
    password = "deyf zggm ptau giqx"

    receiver = "innotechsa24@gmail.com"
    context = ssl.create_default_context()

    
    
 
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)