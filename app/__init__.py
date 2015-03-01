from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
import jinja2

app = Flask(__name__)
app.config.from_object('app.config')
app.jinja_loader = jinja2.FileSystemLoader('app/templates')
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)