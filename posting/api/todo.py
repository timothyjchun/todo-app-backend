from flask import request
from flask_restful import Resource
from db import *

class Todo(Resource):
    def get(self):
        pass

    def post(self):
        text = Test_Board(
            context = request.data
        )
        db.session.add(text)
        db.session.commit()
        
        
