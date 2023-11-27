from flask_restx.reqparse import RequestParser

tarefa_parser = RequestParser()
tarefa_parser.add_argument('tarefa_nome', type=str, required=True, help='Titulo da tarefa',
                           location='json')
tarefa_parser.add_argument('descricao', type=str, required=True, help='Descrição da tarefa',
                           location='json')
tarefa_parser.add_argument('user_id', type=int, required=True, help='Id do usuário',
                           location='json')

tarefa_parser_update = RequestParser()
tarefa_parser_update.add_argument('tarefa_nome', type=str, required=False, help='Titulo da tarefa',
                                  location='json')
tarefa_parser_update.add_argument('descricao', type=str, required=False, help='Descrição da tarefa',
                                  location='json')
