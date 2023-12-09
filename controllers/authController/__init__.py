from .. import api
from flask_restx import Resource
from services.authService.auth import AuthService
from .serializers import serlizer_token
from .forms import login_parser

auth = api.namespace('auth', description='Auth operations')


@auth.route('/login')
class AuthController(Resource):
    @auth.expect(login_parser)
    @auth.marshal_with(serlizer_token)
    def post(self):
        user = login_parser.parse_args()
        return AuthService(user.email, user.senha).authenticate()