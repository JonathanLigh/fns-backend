from newsapi import NewsApiClient

from fns.util.apiutils import get_api_key

news_client = NewsApiClient(api_key=get_api_key())

top_headlines = news_client.get_top_headlines(sources="the-new-york-times")
