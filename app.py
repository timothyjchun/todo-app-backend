from flask import Flask, request
from flask_restful import Resource, reqparse, Api



app = Flask(__name__)

api = Api(app)

class Todo(Resource):
    def get(self):
        pass

    def post(self):
        print(request.data)

api.add_resource(Todo,'/send')


if __name__ == '__main__':
    app.run(debug = True)