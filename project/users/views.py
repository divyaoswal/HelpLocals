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


@users_blueprint.route('login', methods=['GET', 'POST'])
def login():

	login_form = LoginForm(request.form) 
	create_form = CreateAccountForm(request.form)
	# from IPython import embed; embed()
	if request.method == 'POST':
		if create_form.validate_on_submit():
			try:
				new_user = User(request.form['email'], request.form['password'], request.form['zipcode'])
				db.session.add(new_user)
				db.session.commit()
			except IntegrityError as e:
				db.session.rollback()
				return render_template('users/account.html', create_form=create_form, login_form=login_form, error="You have already account please login")	
			return redirect(url_for('posts.post'))

		elif login_form.validate_on_submit():
			# from IPython import embed; embed()
			found_user = User.query.filter_by(email=login_form.email.data).first()
			if found_user:
				authenticated_user = bcrypt.check_password_hash(found_user.password, request.form['password'])
				if authenticated_user:
					session["user_id"] = found_user.id	
					return redirect(url_for('posts.post'))
			else:
				flash("Please enter required credentials")	#i want to more specific tell the user to create account
	return render_template('users/account.html', login_form=login_form, create_form=create_form)






