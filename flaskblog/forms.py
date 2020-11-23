from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired(), Length(min=2, max = 25)])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_password = PasswordField('Password', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')

    def  validate_username(self, username):

        user = User.query.filter_by(username = username.data).first()

        if user:
            raise ValidationError('That username is already taken. Please choose another one')

    def  validate_email(self, email):

        user = User.query.filter_by(email = email.data).first()

        if user:
            raise ValidationError("There's already an account created with that email.")
    
    def  validate_email(self, email):

        user = User.query.filter_by(email = email.data).first()

        if user:
            raise ValidationError("There's already an account created with that email.")

class LoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log in')