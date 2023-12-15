# A website that gets data from a news API and uses sentiment analysis to publish only positive news
import requests
api_key = "5813e71c54cd49acb1cfcbfb63e75770"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "sortBy=publishedAt&apiKey=" \
      "5813e71c54cd49acb1cfcbfb63e75770"
# Make request
request = requests.get(url)
# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])