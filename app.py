from flask import Flask
from models.models import CreateDatabase
import controllers
from dotenv import load_dotenv
import os
from flask_jwt_extended import JWTManager

app = Flask(__name__)
load_dotenv()
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

JWTManager(app)
CreateDatabase().createAll()


controllers.init_app(app)

if __name__ == '__main__':
    app.run()
