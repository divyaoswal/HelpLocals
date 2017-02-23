from flask import Flask, render_template
from flask_modus import Modus
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CsrfProtect
import os

app = Flask(__name__)
modus = Modus(app)
bcrypt = Bcrypt(app)
CsrfProtect(app)

# PATH USED TO STORE FILES OF IMAGES
UPLOAD_FOLDER = '/Users/divyaoswal/rithm/help_locals/photos'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/help_locals_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


db = SQLAlchemy(app)

from project.users.views import users_blueprint
from project.posts.views import posts_blueprint
app.register_blueprint(users_blueprint, url_prefix='/')   #pycache folder is created
app.register_blueprint(posts_blueprint, url_prefix='/post')

@app.route('/')
def root():
	return render_template('home.html')