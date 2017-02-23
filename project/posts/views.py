from flask import Blueprint, render_template, request, flash, redirect, url_for
from project.posts.forms import PostForm, UploadForm
from project import app
from werkzeug.utils import secure_filename
from flask import send_from_directory
import os

ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])


posts_blueprint = Blueprint(
	'posts',
	__name__,
	template_folder = 'templates'
)


@posts_blueprint.route('/details', methods=['GET', 'POST'])
def post():
	post_form = PostForm(request.form)
	if request.method == 'POST':
		# from IPython import embed; embed()
		if post_form.validate_on_submit():
			return redirect(url_for('posts.upload_files'))
	return render_template('posts/details.html', post_form=post_form)




def allowed_file(filename):
	return '.' in filename and \
		filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS    #what is '/' doing here


@posts_blueprint.route('/details/upload_files', methods=['GET', 'POST'])
def upload_files():
	upload_form = UploadForm()
	if request.method == 'POST':
		# check if the post request has the file part
		if 'image' not in request.files:
			flash('No file part')
			return redirect(url_for('posts.upload_files'))
		file = request.files['image'] # know what type of dict??
		# if user does not select file, browser also
		# submit a empty part without filename
		if file.filename == '':
			flash('No selected file')
			return redirect(url_for('posts.upload_files'))
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return redirect(url_for('posts.uploaded_file', filename=filename))
		else:
			flash("required jpg jpeg or png")
			return redirect(url_for('posts.upload_files'))
	return render_template('posts/image.html', upload_form=upload_form)




@posts_blueprint.route('/upload_file/<filename>')
def uploaded_file(filename):
	return 	send_from_directory(app.config['UPLOAD_FOLDER'], filename)			
			






