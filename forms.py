from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, validators


class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', [
        validators.Length(min=1, max=50, message='First Name must be between 1 and 50 characters.'),
        validators.DataRequired(message='First Name is required.')
    ])
    last_name = StringField('Last Name', [
        validators.Length(min=1, max=50, message='Last Name must be between 1 and 50 characters.'),
        validators.DataRequired(message='Last Name is required.')
    ])
    email = StringField('Email', [
        validators.Length(min=6, max=100, message='Email must be between 6 and 100 characters.'),
        validators.DataRequired(message='Email is required.'),
        validators.Email(message='Invalid email address use e.g., juan@gmail.com.')
    ])
    password = PasswordField('Password', [
        validators.DataRequired(message='Password is required.')
    ])
    confirm_password = PasswordField('Confirm Password', [
        validators.DataRequired(message='Confirm Password is required.'),
        validators.EqualTo('password', message='Passwords do not match.')
    ])
    accept_terms = BooleanField('I accept Terms and Conditions', validators=[
        validators.DataRequired(message='You must accept the Terms and Conditions.')])

