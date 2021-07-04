from flask import Flask, request
from flask_restful import Resource, reqparse, Api

app = Flask(__name__)
HOME_PAGE = "https://got-todo-app.herokuapp.com"

from posting.views import *
app.register_blueprint(todo_bp, url_prefix = f"/{HOME_PAGE}/post")


if __name__ == '__main__':
    app.run(debug = True)