from flask import request
from flask_restful import Resource
from db import *
from form import TodoSchema
import json



class DeleteTodo(Resource):
    def post(self):
        data = json.loads(request.data)
        print(f"data: {data}")
        task = Test_Board.query.filter_by(id = data["id"]).first()
        print(f"task: {task}")
        db.session.delete(task)
        db.session.commit()


