from flask_restx.reqparse import RequestParser

login_parser = RequestParser()

login_parser.add_argument('email', type=str, required=True, help='Email do usuário',
                                location='json')
login_parser.add_argument('senha', type=str, required=True, help='Senha do usuário',
                                location='json')
