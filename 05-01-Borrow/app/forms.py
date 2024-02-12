from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, DateField, DecimalField, ValidationError
from wtforms.validators import DataRequired, EqualTo, Email, NumberRange
from datetime import date
from app.models import *

class AddStudentFrom(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    firstname = StringField('Firstname') 
    lastname = StringField('Lastname', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Add Student')

    def validate_username(self, username):
        if Student.query.filter_by(username=username.data).first():
            raise ValidationError('Username already taken. Please choose another')
    
    def validate_email(self, email):
        if Student.query.filter_by(email=email.data).first():
            raise ValidationError('Email already taken. Please choose another')