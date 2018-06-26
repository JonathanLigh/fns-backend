from fns.component import *


class FakeNewsSimulator:
    def __init__(self):
        self.fns_client = FNSClient()

        self.title_model = None
        self.desc_model = None

    def pull_models_from_database(self):
        pass

    def generate_models(self):
        articles_by_categories = self.fns_client.get_articles_by_categories(["business", "life-arts", "science-tech"])

        title_models_by_categories = create_title_models_by_category(articles_by_categories)
        description_models_by_categories = create_description_models_by_category(articles_by_categories)

        return title_models_by_categories, description_models_by_categories

    def generate_fake_articles(self):
        title = self.title_model.make_sentence()


if __name__ == "__main__":
    # TODO: if database does not exist, initialize the db
    pipeline = FakeNewsSimulator()
    print(pipeline.generate_models())
