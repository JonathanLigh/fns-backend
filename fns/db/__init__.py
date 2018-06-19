from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgresql://localhost:5432/fns')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    """
    import all defined models here so they will be registered on the metadata
    """
    from fns.db.models import article, markov
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    #   create fixtures (permission roles)



