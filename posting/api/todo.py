from flask import request
from flask_restful import Resource
from db import *

class Todo(Resource):
    def get(self):
        todo = db.session.query().with_entities(Test_Board.context).all()
        print(todo)
        return todo
        
    #for a POST request, get the new data and save it to the database
    def post(self):
        text = Test_Board(
            context = request.data.decode("utf-8")
        )
        print(text)
        db.session.add(text)
        db.session.commit()
        
        
