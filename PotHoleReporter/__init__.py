from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

application = Flask(__name__, instance_relative_config=True)
application.config.from_pyfile('config.py')
application.config['SECRET_KEY']
application.config['SQLALCHEMY_DATABASE_URI']
db = SQLAlchemy(application)
bcrypt = Bcrypt(application)
loginManager = LoginManager(application)
loginManager.login_view = 'login'
loginManager.login_message_category= 'info'

from PotHoleReporter import routes