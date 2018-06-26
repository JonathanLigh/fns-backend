import markovify

from fns.constant.strconst import StringConstants


def create_title_models_by_category(articles_by_categories):
    return {
        category: _create_model_of_article_field("title", articles_by_categories[category])
        for category in articles_by_categories
    }


def create_content_models_by_category(articles_by_categories):
    return {
        category: _create_model_of_article_field("description", articles_by_categories[category])
        for category in articles_by_categories
    }


def _create_model_of_article_field(field_type, articles):
    field_text = StringConstants.NEWLINE.join([article[field_type] for article in articles])
    field_text = _remove_bad_chars(field_text.encode("ascii", "ignore").decode("ascii"))
    return markovify.Text(field_text)


def _remove_bad_chars(text):
    broken_chars = ["(", ")", "\"", "\'", "[", "]"]
    new_text = text
    for char in broken_chars:
        new_text = new_text.replace(char, "")

    return new_text
