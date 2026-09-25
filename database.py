from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

class Base(DeclarativeBase):
    pass

engine = create_engine("sqlite:///armazem.db")

def criar_banco():
    Base.metadata.create_all(bind = engine)

def get_sessao():
    Session = sessionmaker(bind = engine)   
    return Session()
