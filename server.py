from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from colorama import Fore, init
init(autoreset=True)

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://localhost:5432/fns"
db = SQLAlchemy(app)

db.init_app(app)
db.create_all()


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()
