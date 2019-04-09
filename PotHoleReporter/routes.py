from flask import render_template, url_for, redirect, flash, request, jsonify
from PotHoleReporter import application, db, bcrypt
from PotHoleReporter.forms import LoginForm, RegisterForm, SubmitTicketForm
from PotHoleReporter.models import User, Towns, Tickets
from flask_login import login_user, current_user, login_required, logout_user

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

@application.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(town=form.town.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            nextPage = request.args.get('next')
            return redirect(nextPage) if nextPage else redirect(url_for('account'))
        else:
            flash('Login Failed', 'danger')

    return render_template('login.html', title='Login', form=form)

@application.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@application.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(firstName=form.firstName.data, lastName=form.lastName.data, town=form.town.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@application.route('/newTicket', methods=['GET', 'POST'])
def submitTicket():
    form = SubmitTicketForm()
    if form.validate_on_submit():
        ticket = Tickets(town=form.town.data, size=form.size.data, xcord=form.xcord.data, ycord=form.ycord.data)
        db.session.add(ticket)
        db.session.commit()
        flash(f'Ticket has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('ticket.html', title='Submit Ticket', form=form)

@application.route('/account')
@login_required
def account():
    return render_template('account.html', title='Account')

@application.route('/locations/<town_number>')
def locations(town_number):
    locations = Tickets.query.filter_by(town=town_number).all()
    all_locs = []
    for loc in locations:
        location_details = {
            "lat": loc.xcord,
            "lng": loc.ycord,
            "title": loc.id,
            "size": loc.size}
        all_locs.append(location_details)
    return jsonify({'locations': all_locs})

@application.route('/town/<town>/<town_number>')
def town(town, town_number):
    ticket = Tickets.query.filter_by(town=town_number).all()
    return render_template('town.html', title=town, tickets=ticket, town=town_number)