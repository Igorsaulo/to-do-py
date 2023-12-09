from .. import api
from flask_restx import Resource
from models.models import User
from repositories.user.user_repository import UserRepository
from .serializers import serlizer_user
from .forms import create_user_parser, update_user_parser
from flask_jwt_extended import jwt_required

users = api.namespace('users', description='Users operations')

@users.route('/')
class UserController(Resource):
    @users.expect(create_user_parser)
    @users.marshal_with(serlizer_user)
    def post(self):
        user = create_user_parser.parse_args()
        new_user = UserRepository(User(**user)).create()
        return new_user

@users.route('/<int:id>')
class UserControllerWithId(Resource):
    @jwt_required()
    def get(self, id):
        user = UserRepository.get_user_by_id(id)
        return user
    
    @jwt_required()
    def delete(self, id):
        UserRepository.delete_user_by_id(id)
        return 'User deleted', 200

    @jwt_required()    
    @users.expect(update_user_parser)
    @users.marshal_with(serlizer_user)
    def put(self, id):
        user = update_user_parser.parse_args()
        new_user = UserRepository(User(**user)).update(id)
        return new_user
