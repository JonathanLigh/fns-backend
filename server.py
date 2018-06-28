from flask import Flask, json, Response

from fns.db import init_db, db_session
from fns.db.query import get_articles_by_category
from colorama import Fore, init

init(autoreset=True)

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://localhost:5432/fns"


@app.route('/')
def hello_world():
    response = Response(
        response=json.dumps([{'title': 'The Big Gay', 'content': 'This past weekend marked the 25th annual...','date': '2018-06-26', 'category': 'Business'},
            {'title': 'Chaos at the 50th Annual Impact Summit', 'content': 'Chaos errupts from the 50th annual Impact summit as generations of dreamers wake up.', 'date': '2018-06-26', 'category': 'Tech'},
            {'title': 'Pangea Separates After What Also Felt Like 270 Million Years of Nothing', 'content': 'Founder and CEO, who cares, of the now un-trademarked Pangea today announced, to no one\'s surprise, the LLC\'s dissolution.', 'date': '2018-06-26', 'category': 'Comedy'}]),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/articles/<category>")
def get_articles_by_category_api(category):
    response = Response(response=get_articles_by_category(category), status=200, mimetype="application/json")
    return response


@app.teardown_appcontext
def shutdown_session():
    db_session.remove()


if __name__ == '__main__':
    # init_db()
    app.run()
