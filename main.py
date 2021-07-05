from flask import Flask
from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

pg_db_username = 'timothychun'
pg_db_password = 'mypetcookie0122'
pg_db_name = 'todo_app'
pg_db_hostname = 'localhost'


app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(DB_USER=pg_db_username, DB_PASS=pg_db_password,DB_ADDR=pg_db_hostname,DB_NAME=pg_db_name)
#uri = "{database tye}://{user name}:{password}@{database hostname (address)}/{database name}"
app.config['SQLALCHEMY_ECHO'] = True #False로 설정하면 로그가 프린트되지 않는다.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key='orangeisthenewblack01234'

db = SQLAlchemy(app)


class Test_Board(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    context = db.Column(db.String(50),nullable = False)


from posting.views import *
app.register_blueprint(todo_bp, url_prefix = "/post")


if __name__ == '__main__':
    app.run(debug = True)

