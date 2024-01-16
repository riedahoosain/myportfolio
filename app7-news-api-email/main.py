# A website that gets data from a news API and emails you the topic of the news
# Uses https://newsapi.org

import requests
from send_email import send_email

api_key = "5813e71c54cd49acb1cfcbfb63e75770"
language = "en"
topic = "tesla"

url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "sortBy=publishedAt&" \
      "apiKey=" \
      f"{api_key}&" \
      f"language={language}"

# Make request
request = requests.get(url)
# Get a dictionary with data
content = request.json()
# Access 20 article titles and description
body = ""
for article in content["articles"][0:20]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" \
        + str(article["description"]) \
        + "\n" + article["url"]+ 2*"\n"

# Create Email Body to be sent and run email send function
body = "Subject: Today's news from News API App \n" + body
body = body.encode("utf-8")

send_email(message=body)
print("Email Articles Sent")