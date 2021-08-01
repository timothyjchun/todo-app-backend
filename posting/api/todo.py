from flask import request, jsonify
from flask_restful import Resource
from db import *
from form import TodoSchema
import json

class Todo(Resource):
    def get(self):
        schema = TodoSchema(many = True)
        todo = db.session.query(Test_Board).all()
        id = db.session.query().with_entities(Test_Board.id).all()
        # todo = db.session.query().with_entities(Test_Board.context).all()
        print(todo)
        result = schema.dump(todo)
        print(result)
        return jsonify(dict(result = result, id=id))
        
    #for a POST request, get the new data and save it to the database
    def post(self):
        data = TodoSchema().load(json.loads(request.data))
        print(type(data))
        text = Test_Board(
            context = data['context'],
            color_option = data['color_option']
        )
        print(f"text:{text}")
        db.session.add(text)
        db.session.commit()
        
        
