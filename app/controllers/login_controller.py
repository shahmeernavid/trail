from app import db, login_manager, app
from app.models.user import User
from flask_wtf import Form
from flask import render_template, flash, redirect, request, url_for
from wtforms import validators, TextField, PasswordField
from flask.ext.login import login_user, logout_user, login_required
import hashlib

# Define login and registration forms (for flask-login)
class LoginForm(Form):
  username = TextField(validators=[validators.required()])
  password = PasswordField(validators=[validators.required()])

  def validate_login(self):
    user = self.get_user()

    if user is None:
      raise validators.ValidationError('Invalid user')

    # we're comparing the plaintext pw with the the hash from the db
    if not self.check_password_hash(user.password, user.salt, self.password.data):
      raise validators.ValidationError('Invalid password')

  def get_user(self):
    return db.session.query(User).filter_by(username=self.username.data).first()

  def check_password_hash(self, correctPassword, salt, password):
  	password = hashlib.sha256(salt + password).hexdigest()
  	return correctPassword == password

@app.route("/")
@login_required
def index():
  return render_template("index.html")

@app.route("/test")
@login_required
def test():
  return render_template("test.html")

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(user_id)

@app.route("/login", methods=["GET","POST"])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		form.validate_login()
		user = form.get_user()
		login_user(user)
		flash("Logged In Successfully")
		return redirect(request.args.get("next") or url_for("index"))
	return render_template("login.html", form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))