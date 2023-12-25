# A program that checks a music band's website and sends an email when there are new tours.
import requests
import selectorlib
import smtplib
import ssl
import os
import time
import sqlite3


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
URL = "http://programmer100.pythonanywhere.com/tours/"


# Establish a connection
connection = sqlite3.connect('data.db')



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
    '''Writes the new data to a sqlite db'''
    row = extracted.split(",")
    row = [item.strip() for item in row]
    cursor = connection.cursor()
    cursor.execute("INSERT INTO events VALUES(?,?,?)", row)
    connection.commit()


def read_data(extracted):    
    row = extracted.split(",")
    row = [item.strip() for item in row]
    band, city, date = row
    cursor = connection.cursor()

    # Query Data
    cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?", (band, city, date))
    rows = cursor.fetchall()
    print(rows)
    return rows


if __name__ == "__main__":

    while True:

        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)

        if extracted != "No upcoming tours":
            row = read_data(extracted=extracted)
            if not row:
                store_data(extracted=extracted)
                send_email(message=f"""\
Subject: New event was found
                       
Hey, new event was found.
                       
Sent from My Webscraping App
                       
""")
        time.sleep(5)