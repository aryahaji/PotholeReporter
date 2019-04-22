from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, RadioField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegisterForm(FlaskForm):
    firstName = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])
    lastName = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=30)])
    town = StringField('Town', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirmPassword = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register!')

class LoginForm(FlaskForm):
    town = StringField('Town', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login!')

class SubmitTicketForm(FlaskForm):
    towns = [('1', 'Buffalo'), ('2', 'Amherst'), ('3', 'Clarence'), ('4', 'West Seneca'), ('5', 'Cheektowaga'), ('6', 'Tonawanda'), ('7', 'Eden'),
    ('8', 'Grand Island'), ('9', 'Lancaster'), ('10', 'Williamsville'), ('11', 'Hamburg'), ('12', 'Orchard Park'), ('13', 'Depew'), ('14', 'Kenmore'), ('15', 'Angola')]
    town = SelectField('Town', choices=towns , validators=[DataRequired()])
    size = RadioField('Size', choices=[('s', 'Small'), ('m', 'Medium'), ('l', 'Large')], validators=[DataRequired()])
    xcord = StringField('x-Coordinate', validators=[DataRequired()])
    ycord = StringField('y-Coordinate', validators=[DataRequired()])
    image = FileField('Image', validators=[FileAllowed(['jpg', 'png'], 'Images Only')])
    submit = SubmitField('Create Ticket!')