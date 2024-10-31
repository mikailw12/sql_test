from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
 
sqlite_database = 'sqlite:///metanit2.db'
engine = create_engine(sqlite_database)
 
class Base(DeclarativeBase): pass
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    company_id = Column(Integer, ForeignKey('companies.id'))
    company = relationship('Company', back_populates='user')

 
class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    users = relationship('User', back_populates='company')
 

Base.metadata.create_all(bind=engine)