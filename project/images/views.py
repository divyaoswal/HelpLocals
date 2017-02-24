from flask import Blueprint, render_template, request, redirect, url_for
from project.images.forms import UploadForm
from project import db
from project.models import Image


images_blueprint = Blueprint(
	'images',
	__name__,
	template_folder = 'templates'
)




@images_blueprint.route('/upload_files', methods=['GET', 'POST'])
def upload_files(user_id, post_id):
	upload_form = UploadForm(request.form)
	if request.method == 'POST':
		URL = request.form['image']
		image_obj = Image(URL, post_id)
		db.session.add(image_obj)
		db.session.commit()
		# from IPython import embed; embed()
		return redirect(url_for('posts.show', user_id=user_id, post_id=post_id))
	return render_template('images/image.html', upload_form=upload_form, user_id=user_id, post_id=post_id)



