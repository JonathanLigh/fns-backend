from typing import List
from newsapi import NewsApiClient

from constant.strconst import StringConstants
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

    def get_articles_by_sources(self, sources: List[str]):
        csv_sources = StringConstants.COMMA.join(sources)

        articles_by_sources = []

        page_num = 1
        initial_results = self.news_client.get_everything(sources=csv_sources, page=page_num, page_size=100)
        total_num_articles = initial_results["totalResults"]
        page_one_articles = initial_results["articles"]

        articles_by_sources.extend(page_one_articles)
        remaining_articles = total_num_articles - len(articles_by_sources)

        while remaining_articles > 0:
            page_num += 1
            page_articles = self.news_client.get_everything(sources=csv_sources, page=page_num, page_size=100)["articles"]
            articles_by_sources.extend(page_articles)
            remaining_articles = total_num_articles - len(articles_by_sources)

        return articles_by_sources
