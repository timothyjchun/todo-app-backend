pg_db_username = 'timothychun'
pg_db_password = 'mypetcookie0122'
pg_db_name = 'todo_app'
pg_db_hostname = 'localhost'


SQLALCHEMY_DATABASE_URI = "postgresql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(DB_USER=pg_db_username, DB_PASS=pg_db_password,DB_ADDR=pg_db_hostname,DB_NAME=pg_db_name)
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = "orangeisthenewblack01234"