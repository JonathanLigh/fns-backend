from server import db
from sqlalchemy.dialects.postgresql import JSON


class MarkovModel(db.Model):
    __tablename__ = 'markov_models'

    category = db.Column(db.String, primary_key=True)
    title = db.Column(db.String())
    model_json = db.Column(JSON)

    def __init__(self, category, title, model_json):
        self.category = category
        self.title = title
        self.model_json = model_json

    def __repr__(self):
        return '<markov_model category={}>'.format(self.category)
