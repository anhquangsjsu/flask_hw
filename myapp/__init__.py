from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

myapp_obj = Flask(__name__)
myapp_obj.config.from_mapping(
    SECRET_KEY = "this is a brilliant code, you cannot find out",
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS = False # to supress the warning
)

db = SQLAlchemy(myapp_obj)
db.create_all()

from myapp import routes, models