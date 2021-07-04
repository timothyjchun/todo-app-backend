from flask import Blueprint
from flask_restful import Api, Resource
from posting.api.todo import *

todo_bp = Blueprint('post',__name__)

api = Api(todo_bp)

api.add_resource(Todo,'/send')


