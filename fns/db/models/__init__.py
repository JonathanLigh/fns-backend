from server import db
from sqlalchemy.dialects.postgresql import JSON


class MarkovModel(db.Model):
    __tablename__ = 'markov_models'

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String())
    model_json = db.Column(JSON)
    model_type = db.Column(db.String())

    def __init__(self, category, model_json):
        self.category = category
        self.model_json = model_json

    def __repr__(self):
        return '<id {}>'.format(self.id)
