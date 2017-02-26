# if this file is in folder it wont execute sayinh no module project

import json
from project.models import Post, Image, User
from project import db

lines = []

with open('scrapy_craigslist/craigslist.jl', 'r') as f:
	for line in f:
		lines.append(json.loads(line))


def get_craigslist_user_id():
	users = User.query.filter(User.email=="craigslist@home_locals.com").all()
	if not users:
		user = User("craigslist@home_locals.com", "home_locals", 94108)
		db.session.add(user)
		db.session.commit()
	else:	
		user = users[0]
	return user.id


craigslist_user_id = get_craigslist_user_id()


for line in lines:
	post = Post(
		description=line.get('description'),
		address=line.get('location'),
		title=line.get('title'), 
		user_id=craigslist_user_id)
	db.session.add(post)
	db.session.commit()
	db.session.add(Image(line.get('image_url'), post.id))
	db.session.commit()


