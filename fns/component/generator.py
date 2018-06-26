from fns.constant.strconst import StringConstants


class FNSGenerator:
    def __init__(self, title_model, content_model):
        self.title_model = title_model
        self.content_model = content_model

    def produce_article(self):
        return {"title": self._generate_title(), "content": self._generate_content()}

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

    def _generate_content(self):
        return StringConstants.SPACE.join([self._generate_content_sentence() for _ in range(30)])

    def _generate_content_sentence(self):
        description = None

        for _ in range(30):
            if description is None:
                description = self.content_model.make_sentence(max_chars=120, min_chars=60)
            else:
                break

        if description is None:
            description = ""

        return description
