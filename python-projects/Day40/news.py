# API Key for newsapi.org: c8b03097860043b3bfd1539f8a3169b1
import requests
from pprint import pprint
from dotenv import load_dotenv
load_dotenv(override=True)

class NewsFeed:
    base_url = os.environ['NEWS_API_URL']
    api_key = os.environ['NEWS_API_KEY']

    def __init__(self, interest, from_date, to_date, language):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = self._build_url()
        response = requests.get(url)
        content = response.json()
        articles = content['articles']

        email_body = ''
        for article in articles:
            email_body = email_body + \
                article['title'] + "\n" + article['url'] + "\n\n"
        return email_body

    def _get_articles(self, url):
        url = self._build_url()
        response = requests.get(url)
        content = response.json()
        articles = content['articles']
        return articles

    def _build_url(self):
        url = f"{self.base_url}q={self.interest}&from={self.from_date}&to={self.to_date}&{self.language}&apiKey={self.api_key}"
        return url


if __name__ == "__main__":
    news_feed = NewsFeed(interest='nasa',
                         from_date='2024-09-11', to_date='2024-09-15', language='en')
    print(news_feed.get())
