# A program that gets the temp data from the given website.

import requests
import selectorlib
from datetime import datetime
import sqlite3

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
URL = "http://programmer100.pythonanywhere.com/"

connecion = sqlite3.connect('data.db')

def scrape(url):
    """Scrape the page source from URL"""
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extracttemp.yaml")
    value = extractor.extract(source)["temp"]
    return value

def store_data(extracted):
   now = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
   cursor = connecion.cursor()
   cursor.execute("INSERT INTO temperatures VALUES(?, ?)", (now, extracted))
   connecion.commit()
   print(f"date scraped: {now} temperature: {extracted}")


scraped = scrape(url=URL)

extracted = extract(scraped)
store_data(extracted=extracted)