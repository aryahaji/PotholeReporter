from PotHoleReporter import application
from flask import render_template

@application.route('/')
def home():
    return render_template('index.html')