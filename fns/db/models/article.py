import cuid
from fns.db import Base
from sqlalchemy import Column, String, DateTime
from sqlalchemy.sql import func


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
            # "date": self.date,
            "category": self.category
        }
