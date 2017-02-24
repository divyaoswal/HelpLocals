from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, validators

class PostForm(FlaskForm):
	phoneNo = IntegerField('Phone Number', [validators.DataRequired()])
	contactName = StringField('Contact Name', [validators.DataRequired()])
	street = StringField('street', [validators.DataRequired()])
	city = StringField('city', [validators.DataRequired()])
	title = StringField('Item Title', [validators.DataRequired()])
	price = IntegerField('Price', [validators.DataRequired()])
	description = TextAreaField('Description of Item', [validators.DataRequired()])


	# description = TextAreaField(u'Image Description')