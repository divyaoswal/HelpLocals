from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, IntegerField

class CreateAccountForm(FlaskForm):
	email = StringField('Email', [validators.DataRequired()])
	password = PasswordField('Password', [validators.DataRequired()])
	zipcode = StringField('Zipcode', [validators.DataRequired()])


class LoginForm(FlaskForm):
	email = StringField('Email', [validators.DataRequired()])
	password = PasswordField('Password', [validators.DataRequired()])



