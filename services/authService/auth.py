from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from repositories.user.user_repository import UserRepository
from utils.passwordManager import PasswordManager


class AuthService:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

    def authenticate(self):
        user = UserRepository.get_user_by_email(self.email)
        if user is None:
            return False
        if PasswordManager.check_senha(user.senha, self.senha):
            return {
                'token': create_access_token(identity=user.user_id)
            }
        return False
    
    @staticmethod
    @jwt_required()
    def get_user_id():
        return get_jwt_identity()