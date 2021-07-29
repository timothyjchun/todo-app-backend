from flask import request, jsonify
from flask_restful import Resource
from db import *
import json

class Todo(Resource):
    def get(self):
        todo = db.session.query().with_entities(Test_Board.context).all()
        print(todo)
        return jsonify(todo)
        
    #for a POST request, get the new data and save it to the database
    def post(self):
        text = Test_Board(
            context = json.loads(request.data)['text']
        )
        print(text)
        db.session.add(text)
        db.session.commit()
        
        
