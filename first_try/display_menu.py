from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from database_setup import Restaurant, MenuItem, Base

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////restaurantmenu.db'
db = SQLAlchemy(app)
