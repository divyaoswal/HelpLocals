from flask import Blueprint, request, render_template, redirect, url_for, flash, session, g
from project.users.forms import LoginForm
from project.models import User
from project import db, bcrypt
from project.users.forms import CreateAccountForm

from sqlalchemy.exc import IntegrityError


users_blueprint = Blueprint(
	'users',
	__name__,
	template_folder = 'templates'
)

@users_blueprint.route('/signup', methods=['GET', 'POST'])
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


@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if request.method == 'POST':
		if form.validate_on_submit():
			found_user = User.query.filter_by(email= form.email.data).first()
			if found_user:
				authenticated_user = bcrypt.check_password_hash(found_user.password, request.form['password'])
				# from IPython import embed; embed()
				if authenticated_user:
					session["user_id"] = found_user.id
					return redirect(url_for('posts.post', user_id=found_user.id))
				flash("Invalid email or password")			
	return render_template('users/login.html', form=form)	


