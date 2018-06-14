from server import db
from sqlalchemy.dialects.postgresql import JSON


class MarkovModel(db.Model):
    __tablename__ = 'markov_models'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    model_json = db.Column(JSON)

    def __init__(self, title, model_json):
        self.title = title
        self.model_json = model_json

    def __repr__(self):
        return '<id {}>'.format(self.id)
