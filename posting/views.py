from flask import Blueprint
from flask_restful import Api, Resource
from posting.api.todo import *
from posting.api.deleteTodo import *

todo_bp = Blueprint('post',__name__)

api = Api(todo_bp)

api.add_resource(Todo,'/send')
api.add_resource(DeleteTodo,'/delete')
