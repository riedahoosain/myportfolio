# A program that checks a music band's website and sends an email when there are new tours.
import requests
import selectorlib
import smtplib
import smtplib, ssl
import os
import time


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
URL = "http://programmer100.pythonanywhere.com/tours/"


def scrape(url):
    """Scrape the page source from URL"""
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value


def send_email(message):

    host = "smtp.gmail.com"
    port = 465

    username = "innotechsa24@gmail.com"
    password = "deyf zggm ptau giqx"

    receiver = "innotechsa24@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

    print("Email was sent")


def store_data(extracted):
    with open("data.txt", "a") as file:
        file.write(extracted + "\n")


def read_data(extracted):
    with open("data.txt", "r") as file:
        return file.read()


if __name__ == "__main__":

    while True:

        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)

        content = read_data(extracted)
        if extracted != "No upcoming tours":
            if extracted not in content:
                store_data(extracted)            
                send_email(message = f"""\
Subject: New event was found
                       
Hey, new event was found.
                       
Sent from My Webscraping App
                       
""")
        time.sleep(10)


             