from fns import fns_categories
from fns.component import *
from fns.db import db_session
from fns.db.models import Article, Markov
from fns.structure.text import NLPText


class FakeNewsSimulator:
    def __init__(self):
        self.fns_client = FNSClient()

        self.title_models_by_categories, self.content_models_by_categories = self._load_models()
        self.generators = self._create_generators()

    def _create_generators(self):
        return {
            category: FNSGenerator(
                self.title_models_by_categories[category],
                self.content_models_by_categories[category]
            )
            for category in self.title_models_by_categories
        }

    def _load_models(self):
        title_models_by_categories, content_models_by_categories = self._load_models_from_database()
        if len(title_models_by_categories) == 0 and len(content_models_by_categories) == 0:
            title_models_by_categories, content_models_by_categories = self._generate_models()

        return title_models_by_categories, content_models_by_categories

    def _load_models_from_database(self):
        title_models_by_categories = {}
        content_models_by_categories = {}

        for category in fns_categories:
            markov_models_instance = Markov.query.get(category)

            if markov_models_instance is not None:
                title_models_by_categories[category] = NLPText.from_json(markov_models_instance.title_model_json)
                content_models_by_categories[category] = NLPText.from_json(markov_models_instance.content_model_json)

        return title_models_by_categories, content_models_by_categories

    def _generate_models(self):
        articles_by_categories = self.fns_client.get_articles_by_categories(fns_categories)

        title_models_by_categories = create_title_models_by_category(articles_by_categories)
        content_models_by_categories = create_content_models_by_category(articles_by_categories)

        for category in title_models_by_categories:
            if Markov.query.get(category) is None:
                title_model = title_models_by_categories[category]
                content_model = content_models_by_categories[category]

                markov_models_instance = Markov(category, title_model.to_json(), content_model.to_json())

                db_session.add(markov_models_instance)

        db_session.commit()

        return title_models_by_categories, content_models_by_categories

    def generate_fake_articles(self):
        articles_by_category = {category: self.generators[category].produce_article() for category in fns_categories}

        for category in articles_by_category:
            article_dict = articles_by_category[category]
            article_instance = Article(article_dict["title"], article_dict["content"], category)

            db_session.add(article_instance)

        db_session.commit()

        return articles_by_category
