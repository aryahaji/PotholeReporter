from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
#add DB models import here

class RegisterForm(FlaskForm):
    firstName = StringField('First Name', validators=[DataRequired()])
    lastName = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    passwordConfirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('passowrd')])
    token = StringField('Unique Token from Email', validators=[DataRequired()])
    submit = SubmitField('Create an Account!')

    #prevents crash by ensuring email isn't in DB
    def validate_email(self, email):
        #TODO write function once DB model is created
        pass
    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Email()])
    submit = SubmitField('Login!')

#TODO create submit ticket form
class TicketForm(FlaskForm):
    pass
