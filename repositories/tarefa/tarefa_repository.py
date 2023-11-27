from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.models import Tarefa


class TarefaRepository:
    def __init__(self, tarefa):
        engine = create_engine('sqlite:///database.db')
        Session = sessionmaker(bind=engine)
        self.session = Session()

        self.tarefa = tarefa

    def create(self,user_id):
        self.session.add(self.tarefa)
        self.session.commit()
        tarefa_dict = {
            'tarefa_id': self.tarefa.tarefa_id,
            'tarefa_nome': self.tarefa.tarefa_nome,
            'descricao': self.tarefa.descricao,
            'user_id': user_id
        }
        return tarefa_dict

    def update(self, id):
        tarefa = self.session.query(Tarefa).filter_by(tarefa_id=id).first()
        tarefa.tarefa_nome = self.tarefa.tarefa_nome
        tarefa.descricao = self.tarefa.descricao
        self.session.commit()
        tarefa_dict = {
            'tarefa_id': tarefa.tarefa_id,
            'tarefa_nome': tarefa.tarefa_nome,
            'descricao': tarefa.descricao,
            'user_id': tarefa.user_id
        }
        return tarefa_dict

    @staticmethod
    def get_tarefa_by_id(id):
        engine = create_engine('sqlite:///database.db')
        Session = sessionmaker(bind=engine)
        session = Session()
        tarefa = session.query(Tarefa).filter_by(tarefa_id=id).first()
        tarefa_dict = {
            'tarefa_id': tarefa.tarefa_id,
            'tarefa_nome': tarefa.tarefa_nome,
            'descricao': tarefa.descricao,
            'user_id': tarefa.user_id
        }
        return tarefa_dict

    @staticmethod
    def get_all_tarefas_by_user_id(user_id):
        engine = create_engine('sqlite:///database.db')
        Session = sessionmaker(bind=engine)
        session = Session()
        tarefas = session.query(Tarefa).filter_by(user_id=user_id).all()
        tarefas_dict = []
        for tarefa in tarefas:
            tarefas_dict.append({
                'tarefa_id': tarefa.tarefa_id,
                'tarefa_nome': tarefa.tarefa_nome,
                'descricao': tarefa.descricao,
                'user_id': tarefa.user_id
            })
        return tarefas_dict

    @staticmethod
    def delete_tarefa_by_id(id):
        engine = create_engine('sqlite:///database.db')
        Session = sessionmaker(bind=engine)
        session = Session()
        tarefa = session.query(Tarefa).filter_by(tarefa_id=id).first()
        session.delete(tarefa)
        session.commit()
        return 'Tarefa deleted', 200
