from .. import api
from flask_restx import Resource
from models.models import Tarefa
from repositories.tarefa.tarefa_repository import TarefaRepository
from .forms import tarefa_parser, tarefa_parser_update
from .serializers import serlizer_tarefa
from flask_jwt_extended import jwt_required

tarefas = api.namespace('tarefas', description='Tarefas operations')


@tarefas.route('/<int:id>')
class TarefaControllerWithId(Resource):
    @jwt_required()
    @tarefas.marshal_with(serlizer_tarefa)
    def get(self, id):
        tarefa = TarefaRepository.get_tarefa_by_id(id)
        return tarefa

    @jwt_required()
    @tarefas.marshal_with(serlizer_tarefa)
    @tarefas.expect(tarefa_parser_update)
    def put(self, id):
        tarefa = tarefa_parser_update.parse_args()
        new_tarefa = TarefaRepository(Tarefa(**tarefa)).update(id)
        return new_tarefa

    @jwt_required()
    def delete(self, id):
        TarefaRepository.delete_tarefa_by_id(id)
        return 'Tarefa deleted', 200


@tarefas.route('/user/<int:id>')
class TarefaControllerWithUserId(Resource):
    @jwt_required()
    def get(self, id):
        tarefas = TarefaRepository.get_all_tarefas_by_user_id(id)
        return tarefas

    @jwt_required()
    @tarefas.marshal_with(serlizer_tarefa)
    @tarefas.expect(tarefa_parser)
    def post(self, id):
        tarefa = tarefa_parser.parse_args()
        new_tarefa = TarefaRepository(Tarefa(**tarefa)).create(id)
        return new_tarefa, 201
