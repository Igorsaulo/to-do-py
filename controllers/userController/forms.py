from flask_restx.reqparse import RequestParser

create_user_parser = RequestParser()

create_user_parser.add_argument('nome', type=str, required=True, help='Nome do usuário',
                                location='json')
create_user_parser.add_argument('email', type=str, required=True, help='Email do usuário',
                                location='json')
create_user_parser.add_argument('senha', type=str, required=True, help='Senha do usuário',
                                location='json')

update_user_parser = RequestParser()

update_user_parser.add_argument('nome', type=str, required=False, help='Nome do usuário',
                                location='json')
update_user_parser.add_argument('email', type=str, required=False, help='Email do usuário',
                                location='json')
update_user_parser.add_argument('senha', type=str, required=False, help='Senha do usuário',
                                location='json')