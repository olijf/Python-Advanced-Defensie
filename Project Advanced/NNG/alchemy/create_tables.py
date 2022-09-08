# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base

from models.materiaal import Materiaal, Base, engine

# create tables
Base.metadata.create_all(engine)