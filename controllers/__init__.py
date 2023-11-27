from flask_restx import Api
from importlib import import_module

api = Api()

def init_app(app):
    api.init_app(app)
    import_module('controllers.tarefaController')
    import_module('controllers.userController')
