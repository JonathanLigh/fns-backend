from flask import Flask

from fns.db import init_db, db_session
from colorama import Fore, init

init(autoreset=True)

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://localhost:5432/fns"


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.teardown_appcontext
def shutdown_session(ecpection=None):
    db_session.remove()

if __name__ == '__main__':
    init_db()
    app.run()
