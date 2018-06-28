import markovify

from fns import fns_categories
from fns.component.client import FNSClient
from fns.component.consumer import create_title_models_by_category, create_content_models_by_category
from fns.component.generator import FNSGenerator
from fns.db import db_session
from fns.db.models import Article, Markov
from fns.structure.text import NLPText


def update_category_models():
    fns_client = FNSClient()
    real_articles_by_categories = fns_client.get_articles_by_categories(fns_categories)
    title_models_by_category = create_title_models_by_category(real_articles_by_categories)
    content_models_by_category = create_content_models_by_category(real_articles_by_categories)

    markov_models = Markov.query.all()
    Markov.query.delete()

    for markov_model in markov_models:
        updated_title_model = title_models_by_category[markov_model.category]
        updated_content_model = content_models_by_category[markov_model.category]

        if markov_models:
            old_title_model = NLPText.from_json(markov_model.title_model_json)
            old_content_model = NLPText.from_json(markov_model.content_model_json)

            updated_title_model = markovify.combine([updated_title_model, old_title_model])
            updated_content_model = markovify.combine([updated_content_model, old_content_model])

        updated_model_instance = Markov(
            markov_model.category,
            updated_title_model.to_json(),
            updated_content_model.to_json()
        )

        db_session.add(updated_model_instance)

    db_session.commit()


def update_db_with_latest_fake_articles():
    latest_markov_models = Markov.query.all()

    for markov_model in latest_markov_models:
        generator = FNSGenerator.load_from_json(markov_model.title_model_json, markov_model.content_model_json)
        article = generator.produce_article()
        db_article_instance = Article(article["title"], article["content"], markov_model.category)
        db_session.add(db_article_instance)

    db_session.commit()
