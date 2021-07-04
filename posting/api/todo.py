from flask import request
from flask_restful import Resource

class Todo(Resource):
    def get(self):
        pass

    def post(self):
        print(str(request.data))
