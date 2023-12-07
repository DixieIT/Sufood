from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form
from flask_wtf.csrf import CSRFProtect



app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sufood.db'
db = SQLAlchemy(app)

from app import routes  # Import routes after creating the app instance

