from flask_wtf import FlaskForm
from wtforms import StringField, validators


class UploadForm(FlaskForm):
	image = StringField(u'Image File', [validators.DataRequired()])  #add validation here