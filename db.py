from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()


class Test_Board(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    context = db.Column(db.String(50),nullable = False)

