from .. import api
from flask_restx import fields

serlizer_tarefa = api.model('Tarefa', {
    'tarefa_id': fields.Integer,
    'tarefa_nome': fields.String,
    'descricao': fields.String,
    'user_id': fields.Integer
})
