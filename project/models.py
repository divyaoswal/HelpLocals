from project import db, bcrypt


class User(db.Model):
	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key = True)
	email = db.Column(db.Text, unique=True)
	password = db.Column(db.Text)
	zipcode = db.column(db.Integer)


	def __init__(self, zipcode, email, password):
		self.email = email
		self.password = bcrypt.generate_password_hash(password).decode('UTF-8')
		self.zipcode = zipcode



# class Post(db.Model):
# 	__tablename__ = "posts"

# 	id = db.Column(db.Integer, primary_key = True)
# 	user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"))  #what is users in users.id
# 	image = db.Column