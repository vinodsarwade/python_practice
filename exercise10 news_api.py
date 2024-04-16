'''use the NewsAPI and the request module to fetch the daily news
related to different topics.
go to: https://newsapi.org/
and explore the various option to build your application.'''

import requests
import json
query = input("what type of news are you intrested in ? :")

url = f"https://newsapi.org/v2/everything?q={query}&from=2024-03-16&sortBy=publishedAt&apiKey=85f2bfe1b4f34fd28ff124387e74a23f"

r = requests.get(url)
news = json.loads(r.text)
# print(news)

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("___________________________________________")