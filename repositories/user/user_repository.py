from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.models import User
from services.passmaster import PassMaster

class UserRepository:
    def __init__(self, user):
        engine = create_engine('sqlite:///database.db')
        Session = sessionmaker(bind=engine)
        self.session = Session()

        self.user = user


    def create(self):
        self.user.senha = PassMaster.hashed_senha(self.user.senha)
        self.session.add(self.user)
        self.session.commit()
        user_dict = {
            'nome': self.user.nome,
            'email': self.user.email,
            'senha': self.user.senha
        }
        return user_dict
    
    
    def update(self, id):
        user = self.session.query(User).filter_by(user_id=id).first()
        
        if self.user.nome is not None:
            user.nome = self.user.nome
        if self.user.email is not None:
            user.email = self.user.email
        if self.user.senha:
            user.senha = PassMaster.hashed_senha(self.user.senha)

        self.session.commit()

        user_dict = {
            'nome': user.nome,
            'email': user.email,
            'senha': user.senha
        }
        return user_dict

    
    
    @staticmethod
    def get_user_by_email(email):
        engine = create_engine('sqlite:///database.db')
        Session = sessionmaker(bind=engine)
        session = Session()
        user = session.query(User).filter_by(email=email).first()
        return user
    
    @staticmethod
    def get_all_users():
        engine = create_engine('sqlite:///database.db')
        Session = sessionmaker(bind=engine)
        session = Session()
        users = session.query(User).all()
        users_dict = []
        for user in users:
            users_dict.append({
                'id': user.user_id,
                'nome': user.nome,
                'email': user.email,
                'senha': user.senha
            })
        return users_dict
    
    @staticmethod
    def get_user_by_id(id):
        engine = create_engine('sqlite:///database.db')
        Session = sessionmaker(bind=engine)
        session = Session()
        user = session.query(User).filter_by(user_id=id).first()
        user_dict = {
            'id': user.user_id,
            'nome': user.nome,
            'email': user.email,
            'senha': user.senha
        }
        return user_dict
    
    
    @staticmethod
    def delete_user_by_id(id):
        engine = create_engine('sqlite:///database.db')
        Session = sessionmaker(bind=engine)
        session = Session()
        user = session.query(User).filter_by(user_id=id).first()
        session.delete(user)
        session.commit()
        session.close()
        return True
