from fns.db import Base
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import JSON


class Markov(Base):
    __tablename__ = 'markov'

    category = Column(String, primary_key=True)
    title = Column(String())
    model_json = Column(JSON)

    def __init__(self, category, title, model_json):
        self.category = category
        self.title = title
        self.model_json = model_json

    def __repr__(self):
        return '<markov category={}>'.format(self.category)
