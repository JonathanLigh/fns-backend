import markovify
from newsapi import NewsApiClient

from fns.util.apiutils import get_api_key

news_client = NewsApiClient(api_key=get_api_key())

top_headlines = news_client.get_top_headlines(sources='bbc-news,the-verge', language='en')

for article in top_headlines["articles"]:
    title = article["title"]
    description = article["description"]

    # print(title + " : " + description)


class FNSCrawler:
    def __init__(self):
        self.api_client = NewsApiClient(api_key=get_api_key())

    def crawl_articles(self):
        results = self.api_client.get_top_headlines(category="business", language="en", country="us")
        # print(results)
        articles = results["articles"]
        titles = [article["title"] for article in articles]
        descriptions = [article["description"] if article["description"] is not None else "" for article in articles]

        titles_text = "\n".join(titles)
        descriptions_text = "\n".join(descriptions)

        # print(descriptions_text)

        titles_text_model = markovify.Text(titles_text)
        descriptions_text_moel = markovify.Text(descriptions_text)

        for _ in range(5):
            print(titles_text_model.make_sentence(max_overlap_total=20))
            # print(descriptions_text_moel.make_sentence(max_overlap_total=3))


crawler = FNSCrawler()
crawler.crawl_articles()
