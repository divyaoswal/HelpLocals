from project import db, bcrypt
from datetime import datetime


class User(db.Model):
	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key = True)
	email = db.Column(db.Text, unique=True)
	password = db.Column(db.Text)
	zipcode = db.Column(db.Integer)


	def __init__(self, email, password, zipcode):
		self.email = email
		self.password = bcrypt.generate_password_hash(password).decode('UTF-8')
		self.zipcode = zipcode



class Post(db.Model):
	__tablename__ = "posts"

	id = db.Column(db.Integer, primary_key = True)
	contactName = db.Column(db.Text)
	phoneNo = db.Column(db.Text)
	contactEmail = db.Column(db.Text)
	address = db.Column(db.Text)
	title = db.Column(db.Text)
	description = db.Column(db.Text)
	timestamp = db.Column(db.DateTime)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"))  #what is users in users.id
	images = db.relationship('Image', lazy='dynamic')

	def __init__(self, contactName=None, phoneNo=None, contactEmail=None, address=None, title=None, description=None, user_id=None, timestamp=datetime.utcnow()):
		self.contactName = contactName
		self.phoneNo = phoneNo
		self.contactEmail = contactEmail
		self.address = address
		self.title = title
		self.description = description
		self.timestamp = timestamp
		self.user_id = user_id



class Image(db.Model):
	__tablename__ = "images"

	id = db.Column(db.Integer, primary_key = True)
	image = db.Column(db.String)
	post_id = db.Column(db.Integer, db.ForeignKey('posts.id', ondelete="CASCADE"))

	def __init__(self, image, post_id):
		self.image = image
		self.post_id = post_id


	



