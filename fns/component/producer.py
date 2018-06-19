from fns.constant.strconst import StringConstants


class FakeArticleProducer:
    def __init__(self, title_model, description_model):
        self.title_model = title_model
        self.description_model = description_model

    def produce_articles(self):
        title = self.title_model.make_short_sentence(max_chars=120, min_chars=60)
        description = StringConstants.SPACE.join([self.description_model.make_sentence() for _ in range(5)])

        return title, description
