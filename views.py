from flask import Blueprint
from flask_restful import Api, Resource
import app

todo_bp = Blueprint(Todo,'/')
api = Api(todo_bp)

api.add_resource(Todo,'send')



app.register_blueprint(url_prefix = "http://127.0.0.1:5000/",__name__)

