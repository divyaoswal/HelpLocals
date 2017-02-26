from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from project.users.forms import LoginForm
from project.models import User, Post, Image
from project import db, bcrypt
from project.users.forms import CreateAccountForm
from sqlalchemy import desc
from flask_paginate import Pagination
from sqlalchemy.exc import IntegrityError


users_blueprint = Blueprint(
	'users',
	__name__,
	template_folder = 'templates'
)

PER_PAGE = 28

@users_blueprint.route('/')
def index():
	posts_query = Post.query.filter(Post.timestamp != None).order_by(desc(Post.timestamp))
	page = request.args.get('page', type=int, default=1)
	# total = 0
	# recent_posts_id = []
	# for post in posts_query:
	# 	recent_posts_id.append(post.id)
	# recent_posts_ids_images = Image.query.filter(Image.post_id.in_(recent_posts_id))
	# total = recent_posts_ids_images.count()
	# image_paginate = recent_posts_ids_images.paginate(per_page=4, page=page)
	posts_paginate = posts_query.paginate(per_page=PER_PAGE, page=page)	
	pagination = Pagination(page=page, per_page=PER_PAGE, total=posts_query.count())
	return render_template('home.html',  pagination=pagination, posts_paginate=posts_paginate)


@users_blueprint.route('/<page>')
def page():
	pass


@users_blueprint.route('users/signup', methods=['GET', 'POST'])
def signup():
	form = CreateAccountForm(request.form)
	if request.method == 'POST':
		if form.validate_on_submit():
			try:
				new_user = User(request.form['email'], request.form['password'], request.form['zipcode'])
				db.session.add(new_user)
				db.session.commit()
			except IntegrityError as e:
				# db.session.rollback()
				return render_template('users/signup.html', form=form, error="Username already taken")
			return redirect(url_for('users.login'))
		flash("Invalid submission, Please try again.")
	return render_template('users/signup.html', form=form)


@users_blueprint.route('users/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if request.method == 'POST':
		if form.validate_on_submit():
			found_user = User.query.filter_by(email= form.email.data).first()
			if found_user:
				authenticated_user = bcrypt.check_password_hash(found_user.password, request.form['password'])
				if authenticated_user:
					session["user_id"] = found_user.id
					return redirect(url_for('posts.new', user_id=found_user.id))
				flash("Invalid email or password")			
	return render_template('users/login.html', form=form)	


