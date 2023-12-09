from .. import api
from flask_restx import fields

serlizer_token = api.model('Token', {
    'token': fields.String,
})
