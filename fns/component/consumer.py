import markovify

from fns.util.resutils import get_category_maps


class ArticleConsumer:
    def __init__(self):
        self.category_maps = get_category_maps()

    def consume_real_articles(self, articles_by_categories):
        pass

    def _consume_real_article_titles(self, articles_by_category):
        pass
