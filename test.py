from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker


engine = create_engine('sqlite:///testsDB.db', echo=False)
Base = declarative_base()
Base.metadata.create_all(engine)