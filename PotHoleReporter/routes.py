from flask import render_template, url_for, redirect, flash, request
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

@application.route('/Buffalo')
def Buffalo():
    ticket = Tickets.query.filter(Tickets.town=={'1'})
    return render_template('buffalo.html', title='Buffalo', tickets=ticket)

@application.route('/Amherst')
def Amherst():
    return render_template('amherst.html', title='Amherst')

@application.route('/Clarence')
def Clarence():
    return render_template('clarence.html', title='Clarence')

@application.route('/WestSeneca')
def WestSeneca():
    return render_template('westseneca.html', title='West Seneca')

@application.route('/Cheektowaga')
def Cheektowaga():
    return render_template('cheektowaga.html', title='Cheektowaga')

@application.route('/Tonawanda')
def Tonawanda():
    return render_template('tonawanda.html', title='Tonawanda')

@application.route('/Eden')
def Eden():
    return render_template('eden.html', title='Eden')

@application.route('/GrandIsland')
def GrandIsland():
    return render_template('grandisland.html', title='Grand Island')

@application.route('/Lancaster')
def Lancaster():
    return render_template('lancaster.html', title='Lancaster')

@application.route('/Williamsville')
def Williamsville():
    return render_template('williamsville.html', title='Williamsville')

@application.route('/Hamburg')
def Hamburg():
    return render_template('hamburg.html', title='Hamburg')

@application.route('/OrchardPark')
def OrchardPark():
    return render_template('orchardpark.html', title='Orchard Park')

@application.route('/Depew')
def Depew():
    return render_template('depew.html', title='Depew')

@application.route('/Kenmore')
def Kenmore():
    return render_template('kenmore.html', title='Kenmore')

@application.route('/Angola')
def Angola():
    return render_template('angola.html', title='Angola')