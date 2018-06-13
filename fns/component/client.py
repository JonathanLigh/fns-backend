from newsapi import NewsApiClient

from util.resutils import *


class FNSClient:
    def __init__(self):
        self.news_client = NewsApiClient(api_key=get_api_key())
        self.category_map = get_category_maps()

    def get_sources_by_category(self, category: str):
        news_api_categories = self.category_map["fns-newsapi"].get(category)

        all_sources = []
        for news_api_category in news_api_categories:
            sources = self.news_client.get_sources(category=news_api_category)["sources"]
            all_sources.extend(sources)

        return all_sources

    def get_articles_by_source(self, source):
        pass
