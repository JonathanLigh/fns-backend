import cuid
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.sql import func

from fns.db import Base


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


class Article(Base):
    __tablename__ = "articles"

    id = Column(String, primary_key=True)
    title = Column(String)
    content = Column(String)
    date = Column(DateTime(timezone=True), server_default=func.now())
    category = Column(String)

    def __init__(self, title, content, category):
        self.id = cuid.cuid()
        self.title = title
        self.content = content
        self.category = category

    def __repr__(self):
        return "<article id={}>".format(self.id)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "date": str(self.date),
            "category": self.category
        }
