import markovify
from newsapi import NewsApiClient

from fns.util.resutils import get_api_key


class FNSCrawler:
    def __init__(self):
        self.api_client = NewsApiClient(api_key=get_api_key())

    def crawl_articles(self):
        results = self.api_client.get_everything(q="deep learning", language="en", page_size=100)
        print(results["totalResults"])
        articles = results["articles"]
        print(articles[0])
        titles = [article["title"] for article in articles]
        descriptions = [article["description"] for article in articles if article["description"] is not None]

        titles_text = "\n".join(titles)
        descriptions_text = "\n".join(descriptions)

        titles_text_model = markovify.Text(titles_text)
        descriptions_text_model = markovify.Text(descriptions_text)

        for _ in range(5):
            print(titles_text_model.make_short_sentence(max_chars=120, min_chars=60))
            print(descriptions_text_model.make_sentence())

    def categorize_sources(self):
        results = self.api_client.get_sources(category="technology", language="en")
        print(results["sources"])


crawler = FNSCrawler()
crawler.crawl_articles()
# crawler.categorize_sources()
