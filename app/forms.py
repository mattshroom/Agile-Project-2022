from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, HiddenField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    
    username    = StringField('username',   validators=[DataRequired()])
    password    = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember me?')
    
    submit = SubmitField('sign in')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class ResultsForm(FlaskForm):
        score =  HiddenField('finalscore', validators=[DataRequired()])
        guesses = HiddenField('finalguesses', validators=[DataRequired()])
        time = HiddenField('finaltime', validators=[DataRequired()])
        logo = HiddenField('finallogo', validators=[DataRequired()])
        submit = SubmitField('submitResult')