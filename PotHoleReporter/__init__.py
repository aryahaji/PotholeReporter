from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

application = Flask(__name__, instance_relative_config=True)
application.config.from_pyfile('config.py')
application.config['SECRET_KEY']
application.config['SQLALCHEMY_DATABASE_URI']
application.config['MAIL_SERVER']
application.config['MAIL_PORT']
application.config['MAIL_USE_TLS']
application.config['MAIL_USERNAME']
application.config['MAIL_PASSWORD']
db = SQLAlchemy(application)
bcrypt = Bcrypt(application)
loginManager = LoginManager(application)
loginManager.login_view = 'login'
loginManager.login_message_category= 'info'
mail = Mail(application)


from PotHoleReporter import routes