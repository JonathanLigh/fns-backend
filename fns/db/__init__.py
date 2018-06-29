import os
from sqlalchemy.ext.declarative import declarative_base

from fns.db.session import create_db_session
from fns.util.resutils import get_database_paths

database_path = os.environ.get("DATABASE_URL") if os.environ.get("DATABASE_URL") else get_database_paths()["LOCAL"]
engine, db_session = create_db_session(database_path)

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    from fns.db.models import Article, Markov

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    # TODO: create fixtures (permission roles)
