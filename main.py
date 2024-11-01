from sqlalchemy import create_engine, Integer, String, ForeignKey, Column
from sqlalchemy.orm import Session, DeclarativeBase, relationship

sqlite_database = 'sqlite:///metanit.db'

engine = create_engine(sqlite_database)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    company_id = Column(String, ForeignKey('companies.id'))

    company = relationship('Company', back_populates='users')

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    users = relationship('User', back_populates='company')
    products = relationship('Product', back_populates='company')


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    company_id = Column(Integer, ForeignKey('companies.id'))

    company = relationship('Company', back_populates='products')

Base.metadata.create_all(engine)


with Session(autoflush=False, bind=engine) as db:
    user = db.query(User).all()
    for u in user:
        print(f'{u.name}, {u.company.name}')
