import cuid
from fns.db import Base
from sqlalchemy import Column, String, Integer, Date


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    date = Column(Date)
    category = Column(String)

    def __init__(self, title, content, date, category):
        self.id = cuid.cuid()
        self.title = title
        self.content = content
        self.date = date
        self.category = category

    def __repr__(self):
        return "<article id={}>".format(self.id)
