from .. import api
from flask_restx import fields

serlizer_user = api.model('User', {
    'nome': fields.String,
    'email': fields.String,
})
