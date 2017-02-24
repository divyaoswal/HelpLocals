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


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/help_locals_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['TEMPLATES_AUTO_RELOAD'] = True


db = SQLAlchemy(app)

from project.users.views import users_blueprint
from project.posts.views import posts_blueprint
from project.images.views import images_blueprint

app.register_blueprint(users_blueprint, url_prefix='/')   #pycache folder is created
app.register_blueprint(posts_blueprint, url_prefix='/users/<int:user_id>/posts')
app.register_blueprint(images_blueprint, url_prefix='/users/<int:user_id>/posts/<int:post_id>')

