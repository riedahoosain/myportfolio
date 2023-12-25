# A program that gets the temp data from the given website.

import requests
import selectorlib
from datetime import datetime

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
URL = "http://programmer100.pythonanywhere.com/"


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
    with open("datatemp.txt", "a") as file:
        file.write(extracted + "\n")


scraped = scrape(url=URL)
now = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
extracted = extract(scraped)
content = f"{now},{extracted}"
store_data(extracted=content)
print(content)