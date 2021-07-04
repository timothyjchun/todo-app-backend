from flask import request
from flask_restful import Resource
from main import *

class Todo(Resource):
    def get(self):
        pass

    def post(self):
        new_context = Test_Board(
            context = request.data
        )
        db.session.add(new_context)
        db.session.commit()
        
