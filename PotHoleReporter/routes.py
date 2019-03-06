from flask import render_template, url_for, redirect
from PotHoleReporter import application

@application.route('/')
@application.route('/home')
def home():
    return render_template('index.html', title='Home')

@application.route('/about')
def about():
    return render_template('about.html', title='About')

@application.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')

@application.route('login', methods=['GET', 'POST'])
def login():
    return render_template('login.html', title='Login')

@application.route('logout')
def logout():
    return redirect(url_for('login'))

@application.route('register', methods=['GET', 'POST'])
def register():
    return render_template('register.html', title='Register')

