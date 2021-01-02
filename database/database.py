from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URL = 'postgresql://postgres:137627054402@localhost/localsuppliers'

# Whenever we want to use SQLAlchemy to interact with a database, we need to create an Engine.
# echo flag determines if we want to see the sql code generated or not
engine = create_engine(DATABASE_URL, echo=False)

# scoped_session cares about threads here
DatabaseSession = scoped_session(sessionmaker(autocommit=False,
                                              autoflush=False,
                                              bind=engine))
Base = declarative_base()

Base.query = DatabaseSession.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from models import models3, models4, models1, models2
    Base.metadata.create_all(bind=engine)
