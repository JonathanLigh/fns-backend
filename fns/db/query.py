from fns.db.models import Article, Markov


def get_articles_by_category(category):
    article_instances = Article.query.filter_by(category=category).all()
    return [article_instance.__dict__ for article_instance in article_instances]
