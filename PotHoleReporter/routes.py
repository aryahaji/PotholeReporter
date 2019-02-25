from PotHoleReporter import application
from flask import render_template

@application.route('/')
@application.route('/index')
def home():
    return render_template('index.html')