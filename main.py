from flask import Flask
from flask_restful import Resource

app = Flask(__name__)
app.config.from_object('config')

from db import db
db.init_app(app)

from posting.views import todo_bp
app.register_blueprint(todo_bp, url_prefix = "/post")


if __name__ == '__main__':
    app.run(debug = True)

