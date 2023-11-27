from flask import Flask
from models.models import CreateDatabase
import controllers

app = Flask(__name__)

CreateDatabase().createAll()

controllers.init_app(app)

if __name__ == '__main__':
    app.run()

