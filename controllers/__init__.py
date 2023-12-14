from flask_restx import Api
from importlib import import_module

api = Api()

api.authorizations = {
    'Bearer Token': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}
api.security = 'Bearer Token'


def init_app(app):
    api.init_app(app)
    import_module('controllers.tarefaController')
    import_module('controllers.userController')
    import_module('controllers.authController')
