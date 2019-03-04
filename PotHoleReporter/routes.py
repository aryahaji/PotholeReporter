from PotHoleReporter import application
from PotHoleReporter.forms import LoginForm, RegisterForm
from flask import render_template

@application.route('/')
@application.route('/index')
def home():
    return render_template('index.html')

@application.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    return render_template('register.html', title="Register", form=form)

@application.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title="Login", form=form)