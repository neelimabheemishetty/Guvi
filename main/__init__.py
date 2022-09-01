
from distutils.command.config import config
from distutils.log import debug
from email.policy import default
from enum import unique
from msilib.schema import Directory
import os
from tkinter import N
from turtle import title
import time
import bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

Directory = os.path.abspath(os.path.dirname(__file__))
print(Directory)

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791438bb0b13ce0c668df290ab254'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(Directory, 'next.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASSE')
mail=Mail(app)


from main import routes