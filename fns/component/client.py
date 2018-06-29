import os
from newsapi import NewsApiClient
from typing import List

from fns.constant.strconst import StringConstants
from fns.util.resutils import get_api_key, get_category_maps


class FNSClient:
    def __init__(self):
        api_key = os.environ.get("NEWS_API_KEY") if os.environ.get("NEWS_API_KEY") else get_api_key()
        self.news_client = NewsApiClient(api_key=api_key)
        self.category_map = get_category_maps()

    def get_sources_by_category(self, fns_category: str):
        news_api_categories = self.category_map["fns-newsapi"].get(fns_category)

        all_sources = []
        for news_api_category in news_api_categories:
            sources = self.news_client.get_sources(category=news_api_category)["sources"]
            source_names = [source["name"] for source in sources]
            all_sources.extend(source_names)

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
            if page_num >= 2:
                break

            page_articles = self.news_client.get_everything(sources=csv_sources, page=page_num, page_size=100)["articles"]
            articles_by_sources.extend(page_articles)
            remaining_articles = total_num_articles - len(articles_by_sources)

        return articles_by_sources

    def get_articles_by_categories(self, fns_categories: List[str]):
        sources_by_categories = [self.get_sources_by_category(category) for category in fns_categories]
        articles_by_sources_by_categories = [self.get_articles_by_sources(sources) for sources in sources_by_categories]

        return {
            fns_category: articles_by_sources_by_category
            for fns_category, articles_by_sources_by_category
            in zip(fns_categories, articles_by_sources_by_categories)
        }
