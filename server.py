from flask import Flask

from fns.db import init_db, db_session
from colorama import Fore, init

init(autoreset=True)

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://localhost:5432/fns"


@app.route('/')
def hello_world():
    return [{'title': 'The Big Gay', 'content': 'This past weekend marked the 25th annual...','date': '2018-06-26', 'catagory': 'Business'},
            {'title': 'Chaos at the 50th Annual Impact Summit', 'content': 'Chaos errupts from the 50th annual Impact summit as generations of dreamers wake up.', 'date': '2018-06-26', 'catagory': 'Tech'},
            {'title': 'Pangea Separates After What Also Felt Like 270 Million Years of Nothing', 'content': 'Founder and CEO, who cares, of the now un-trademarked Pangea today announced, to no one\'s surprise, the LLC\'s dissolution.', 'date': '2018-06-26', 'catagory': 'Comedy'}]

@app.teardown_appcontext
def shutdown_session(ecpection=None):
    db_session.remove()

if __name__ == '__main__':
    init_db()
    app.run()
