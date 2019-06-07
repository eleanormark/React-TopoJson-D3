"""Database models"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import SingletonThreadPool

Base = declarative_base()


class Physicians(Base):
    __tablename__ = 'physicians'

    id = Column(Integer, primary_key=True)
    specialty = Column(String)
    state = Column(String)
    count = Column(Integer)


class Specialties(Base):
    __tablename__ = 'specialties'

    id = Column(Integer, primary_key=True)
    specialty = Column(String)
    count = Column(Integer)


def sqlite_engine():
    return create_engine(
        'sqlite:///data.db',
        poolclass=SingletonThreadPool,
        connect_args={'check_same_thread':False}
    )


def create_tables(engine):
    Base.metadata.create_all(engine)


def get_session(engine):
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    return session
