import imghdr
import smtplib
import ssl
from email.message import EmailMessage

SENDER = "innotechsa24@gmail.com"
PASSWORD = "deyf zggm ptau giqx"
RECEIVER = "innotechsa24@gmail.com"


def send_email(image_path):
    print("send_email function started")
    email_message = EmailMessage()
    email_message["Subject"] = "New camera alert detected"
    email_message.set_content("Hey we just picked up a new image on the camera")

    with open(image_path, "rb") as file:
        content = file.read()
        filename = file.name
        im_type = imghdr.what(None, content)

    email_message.add_attachment(content, maintype="image", subtype=im_type, filename=filename)

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()
    
    print("send_email function ended")


if __name__ == "__main__":
    print("This is the email module")
