import cuid
from server import db


class Article(db.Model):
    __tablename__ = "articles"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    date = db.Column(db.Date)
    category = db.Column(db.String)

    def __init__(self, title, content, date, category):
        self.id = cuid.cuid()
        self.title = title
        self.content = content
        self.date = date
        self.category = category

    def __repr__(self):
        return "<article id={}>".format(self.id)
