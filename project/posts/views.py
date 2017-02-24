from flask import Blueprint, render_template, request, redirect, url_for
from project.posts.forms import PostForm
from project import db
from project.models import Post, User


posts_blueprint = Blueprint(
	'posts',
	__name__,
	template_folder = 'templates'
)


@posts_blueprint.route('/new', methods=['GET', 'POST'])
def new(user_id):
	post_form = PostForm(request.form)
	if request.method == 'POST':
		if post_form.validate_on_submit():
			post_obj = Post(request.form['contactName'], request.form['phoneNo'], request.form['street'], request.form['city'], request.form['price'], request.form['title'], request.form['description'], user_id)
			db.session.add(post_obj)
			db.session.commit()
			return redirect(url_for('images.upload_files', user_id=user_id, post_id=post_obj.id))
	return render_template('posts/new.html', user_id=user_id, post_form=post_form)


@posts_blueprint.route('/<int:post_id>')
def show(user_id, post_id):
	post = Post.query.get(post_id)
	user = User.query.get(post.user_id)
	return render_template('posts/show.html', user_id=user_id, post=post, user=user)



