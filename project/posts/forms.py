from flask_wtf import FlaskForm
from wtforms import StringField, FileField, IntegerField, TextAreaField, validators

class PostForm(FlaskForm):
	phoneNo = IntegerField('Phone Number', [validators.DataRequired()])
	contactName = StringField('Contact Name', [validators.DataRequired()])
	# street = StringField('street', [validators.DataRequired()])
	# city = StringField('city', [validators.DataRequired()])
	postTitle = StringField('Item Title', [validators.DataRequired()])
	postDescription = TextAreaField('Description of Item', [validators.DataRequired()])

class UploadForm(FlaskForm):
	image = FileField(u'Image File', [validators])  #add validation here
	description = TextAreaField(u'Image Description')