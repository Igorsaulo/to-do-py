from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    nome = Column(String)
    email = Column(String, unique=True)
    senha = Column(String)
    tarefas = relationship("Tarefa", back_populates="user")


class Tarefa(Base):
    __tablename__ = 'tarefas'
    tarefa_id = Column(Integer, primary_key=True)
    tarefa_nome = Column(String)
    descricao = Column(String)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    user = relationship("User", back_populates="tarefas")


class CreateDatabase:
    def __init__(self):
        self.createAll()

    @staticmethod
    def createAll():
        database_url = 'sqlite:///database.db'
        engine = create_engine(database_url, echo=True)
        Base.metadata.create_all(bind=engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        session.commit()
        session.close()
