import json

from fns.db.models import Article


def get_articles_by_category(category):
    article_instances = Article.query.filter_by(category=category).all()
    return json.dumps([article_instance.to_dict() for article_instance in article_instances])
