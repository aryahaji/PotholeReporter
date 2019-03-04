from flask import Flask

application = Flask(__name__)
application.config.from_pyfile('config.py')

application.config['SECRET_KEY']

from PotHoleReporter import routes