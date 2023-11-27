from .. import api
from flask_restx import Resource
from models.models import User
from repositories.user.user_repository import UserRepository
from services.auth import UserAuth
from .serializers import serlizer_user
from .forms import create_user_parser, update_user_parser

users = api.namespace('users', description='Users operations')

@users.route('/')
class UserController(Resource):
    @users.expect(create_user_parser)
    @users.marshal_with(serlizer_user)
    def post(self):
        user = api.payload
        new_user = UserRepository(User(**user)).create()
        return new_user

@users.route('/<int:id>')
class UserControllerWithId(Resource):
    def get(self, id):
        user = UserRepository.get_user_by_id(id)
        return user
    
    def delete(self, id):
        UserRepository.delete_user_by_id(id)
        return 'User deleted', 200
    
    @users.expect(update_user_parser)
    @users.marshal_with(serlizer_user)
    def put(self, id):
        user = api.payload
        new_user = UserRepository(User(**user)).update(id)
        return new_user

@users.route('/users/auth')
class UserAuthController(Resource):
    def post(self):
        userData = api.payload
        user_auth = UserAuth(email=userData['email'], senha=userData['senha'])
        token = user_auth.authenticate()
        return token
