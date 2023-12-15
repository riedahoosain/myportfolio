# A website that gets data from a news API and uses sentiment analysis to publish only positive news
import requests
from send_email import send_email
api_key = "5813e71c54cd49acb1cfcbfb63e75770"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "sortBy=publishedAt&apiKey=" \
      "5813e71c54cd49acb1cfcbfb63e75770"
# Make request
request = requests.get(url)
# Get a dictionary with data
content = request.json()
# Access the article titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + str(article["description"]) + 2*"\n"

# Create Email Body to be sent and run email send function
body = "Subject: Tesla news from News API App \n" + body
body = body.encode("utf-8")

send_email(message=body)
print("Email Sent")