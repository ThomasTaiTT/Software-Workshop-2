from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, DateField, DecimalField, ValidationError
from wtforms.validators import DataRequired, EqualTo, Email, NumberRange
from datetime import date

class DateRange(object):
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def __call__(self, form, field):
        if field.data < self.min or field.data > self.max:
            raise ValidationError('Date must be between {} and {}.'.format(self.min, self.max))
        
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In', validators=[DataRequired()])

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirmpassword = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    dateofbirth = DateField('Date of Birth', format='%Y-%m-%d', validators=[DataRequired(), DateRange(min=date(1900, 1, 1), max=date.today())])
    telephone = IntegerField('Phone number', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    height = DecimalField('Height', validators=[DataRequired(), NumberRange(min = 0, max = 2.9)])
    weight = DecimalField('Weight', validators=[DataRequired(), NumberRange(min=0, max=453.6)])
    submit = SubmitField('Sign In',validators=[DataRequired()])
