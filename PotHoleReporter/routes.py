import os
from flask import render_template, url_for, redirect, flash, request, jsonify
from PotHoleReporter import application, db, bcrypt
from PotHoleReporter.forms import LoginForm, RegisterForm, SubmitTicketForm
from PotHoleReporter.models import User, Towns, Tickets
from werkzeug.utils import secure_filename
from flask_login import login_user, current_user, login_required, logout_user

UPLOAD_FOLDER='PotHoleReporter/static/pothole_imgs'

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
        img = form.image.data
        if img is None:
            ticket = Tickets(town=form.town.data, size=form.size.data, description=form.description.data, xcord=form.xcord.data, ycord=form.ycord.data, image='NULL')
            db.session.add(ticket)
            db.session.commit()
            flash(f'Ticket has been created!', 'success')
            return redirect(url_for('home'))
        else:
            imgName = secure_filename(img.filename)
            ticket = Tickets(town=form.town.data, size=form.size.data, description=form.description.data, xcord=form.xcord.data, ycord=form.ycord.data, image=imgName)
            img.save(os.path.join(UPLOAD_FOLDER, imgName))
            db.session.add(ticket)
            db.session.commit()
            flash(f'Ticket has been created!', 'success')
            return redirect(url_for('home'))
    return render_template('ticket.html', title='Submit Ticket', form=form)

@application.route('/account')
@login_required
def account():
    townNumbers = {
        "Buffalo": 1,
        "Amherst": 2,
        "Clarence": 3,
        "West Seneca": 4,
        "Cheektowaga": 5,
        "Tonawanda": 6,
        "Eden": 7,
        "Grand Island": 8,
        "Lancaster": 9,
        "Williamsville": 10,
        "Hamburg": 11,
        "Orchard Park": 12,
        "Depew": 13,
        "Kenmore": 14,
        "Angola": 15
    }
    page = request.args.get('page',1,type=int)
    tickets_per_page = 2
    ticket = Tickets.query.filter_by(town=townNumbers.get(current_user.town)).paginate(page, tickets_per_page, False)
    next_url = url_for('account', page=ticket.next_num) \
        if ticket.has_next else None
    prev_url = url_for('account', page=ticket.prev_num) \
        if ticket.has_prev else None
    return render_template('account.html', title='Account', tickets=ticket.items, next=next_url, prev=prev_url, number_of_pages=ticket.pages)

@application.route('/delete/<ticketId>')
def delete(ticketId):
    ticket = Tickets.query.filter_by(id=ticketId).first()
    db.session.delete(ticket)
    db.session.commit()
    flash(f'Ticket ' + ticketId +' has been removed.', 'danger')
    print("Deleted")
    return redirect(url_for('account'))

@application.route('/locations/<town_number>')
def locations(town_number):
    locations = Tickets.query.filter_by(town=town_number).all()
    all_locs = []
    for loc in locations:
        location_details = {
            "lat": loc.xcord,
            "lng": loc.ycord,
            "title": loc.id,
            "description": loc.description,
            "size": loc.size,
            "image": url_for('static', filename='pothole_imgs/'+loc.image)}
        all_locs.append(location_details)
    return jsonify({'locations': all_locs})

@application.route('/town/<town>/<town_number>')
def town(town, town_number):
    page = request.args.get('page',1,type=int)
    tickets_per_page = 5
    ticket = Tickets.query.filter_by(town=town_number).paginate(page, tickets_per_page, False)
    next_url = url_for('town', town=town, town_number=town_number, page=ticket.next_num) \
        if ticket.has_next else None
    prev_url = url_for('town', town=town, town_number=town_number, page=ticket.prev_num) \
        if ticket.has_prev else None
    return render_template('town.html', title=town, tickets=ticket.items, town=town_number, next=next_url, prev=prev_url, number_of_pages=ticket.pages)