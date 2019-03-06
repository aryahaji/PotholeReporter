from flask import Flask
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__, instance_relative_config=True)
application.config.from_pyfile('config.py')
application.config['SECRET_KEY']
application.config['SQLALCHEMY_DATABASE_URI']
db = SQLAlchemy(application)