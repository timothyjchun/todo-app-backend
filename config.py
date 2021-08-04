import os
import configparser

SQLALCHEMY_DATABASE_URI = "postgresql://opyosnsutmfjyb:9cae28d9613531aa063db87bf1c07d215dd9e184edb5250feac91c74074569d9@ec2-52-45-183-77.compute-1.amazonaws.com:5432/d8q45oit7uisbq"
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = True

config = configparser.ConfigParser()
config.read('config.ini')

SECRET_KEY = config['HOST']['SECRET_KEY']
print(SECRET_KEY)



