from sqlalchemy import create_engine, ForeignKey, String, Integer
from sqlalchemy.orm import DeclarativeBase, relationship


sqlite_database = 'sqlite:///metanit2.db'
engine = create_engine(sqlite_database)

class Base(DeclarativeBase):
    pass

#...

Base.metadata.create_all(bind=engine)