from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

App = Flask(__name__)
App.config.from_object('config')  # configure our app

db = SQLAlchemy(App) # connect the database

from app import views, models
