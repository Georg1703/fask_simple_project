from flask import Flask
from flask_restful import Api

from app.api import Personal, Experience, Education
from app.cli import register_commands

def create_app():
    app = Flask(__name__)
    api = Api(app)
    
    api.add_resource(Personal, '/personal')
    api.add_resource(Experience, '/experience')
    api.add_resource(Education, '/education')

    register_commands(app)

    return app
