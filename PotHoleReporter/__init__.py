from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

application = Flask(__name__, instance_relative_config=True)
GoogleMaps(application, key="AIzaSyCSh5DlWvP9q8WXx4-x6-9XJG17WWd3ET8")
application.config.from_pyfile('config.py')
application.config['SECRET_KEY']
application.config['SQLALCHEMY_DATABASE_URI']
db = SQLAlchemy(application)
bcrypt = Bcrypt(application)
loginManager = LoginManager(application)
loginManager.login_view = 'login'
loginManager.login_message_category= 'info'

from PotHoleReporter import routes