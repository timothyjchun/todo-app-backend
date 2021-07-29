from flask import request
from flask_restful import Resource
from db import *

class Todo(Resource):
    def get(self):
        todo = db.session.query().with_entities(Test_Board.context).all()
        print(todo)
        return todo

    def post(self):
        text = Test_Board(
            context = request.data
        )
        db.session.add(text)
        db.session.commit()
        
        
