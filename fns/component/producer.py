from fns.constant.strconst import StringConstants


class FNSProducer:
    def __init__(self, title_model, description_model):
        self.title_model = title_model
        self.description_model = description_model

    def produce_articles(self):
        title = self.title_model.make_short_sentence(max_chars=120, min_chars=60)
        description = StringConstants.SPACE.join([self._generate_description_sentence() for _ in range(5)])

        return title, description

    def _generate_title(self):
        title = None

        for _ in range(30):
            if title is None:
                title = self.title_model.make_short_sentence(max_chars=120, min_chars=60)
            else:
                break

        if title is None:
            title = ""

        return title

    def _generate_description_sentence(self):
        description = None

        for _ in range(30):
            if description is None:
                description = self.description_model.make_sentence(max_chars=120, min_chars=60)
            else:
                break

        if description is None:
            description = ""

        return description
