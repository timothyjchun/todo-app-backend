from flask import Flask
from flask_restful import Resource

app = Flask(__name__)
# HOME_PAGE = "https://got-todo-app.herokuapp.com"
# HOME_PAGE = "http://127.0.0.1:5000"

from posting.views import *
app.register_blueprint(todo_bp, url_prefix = "/post")


if __name__ == '__main__':
    app.run(debug = True)

