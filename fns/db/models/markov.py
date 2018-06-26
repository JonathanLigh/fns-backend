from fns.db import Base
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import JSON


class Markov(Base):
    __tablename__ = 'markov'

    category = Column(String, primary_key=True)
    title_model_json = Column(JSON)
    content_model_json = Column(JSON)

    def __init__(self, category, title_model_json, description_model_json):
        self.category = category
        self.title_model_json = title_model_json
        self.content_model_json = description_model_json

    def __repr__(self):
        return '<markov category={}>'.format(self.category)
