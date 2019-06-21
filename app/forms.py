from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, FloatField, SubmitField
from app.models import User
from .env import DB
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    surname = StringField('Surname')
    name = StringField('Name')
    email = StringField('Email')
    X = FloatField('X')
    Y = FloatField('Y')

    submit = SubmitField('Add to map')

    def validate_surname(self, surname):
        user = User.query.filter_by(surname=surname.data).first()
        if user is not None:
            raise ValidationError('Please use a different surname.')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')
                
    def validate_name(self, name):
        user = User.query.filter_by(name=name.data).first()
        if user is not None:
            raise ValidationError('Please use a different name address.')
