from app import db, login_manager, app
from app.models.user import User
from flask_wtf import Form
from flask import render_template, flash, redirect, request, url_for, session, send_file
from wtforms import validators, TextField, PasswordField
from flask.ext.login import login_user, logout_user, login_required
import hashlib
from flask_oauth import OAuth
import requests
import json

oauth = OAuth()

facebook = oauth.remote_app('facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key='860566537333704',
    consumer_secret='ff8591f24f8712467c03c57ad52f1c00',
    request_token_params={'scope': 'email'}
)

@facebook.tokengetter
def get_facebook_token(token='user'):
	return session.get('facebook_token')

@app.route('/oauth-authorized')
@facebook.authorized_handler
def oauth_authorized(resp):
    next_url = url_for('index')
    if resp is None:
        flash(u'You denied the request to sign in.')
        return redirect(next_url)

    session['facebook_token'] = resp['access_token']

    flash('You were signed in as %s' % resp['access_token'])
    response_dict = requests.get('https://graph.facebook.com/me?fields=name,id,email&access_token=%s' % session['facebook_token']).content
    python_dict = json.loads(response_dict)
    print python_dict
    facebook_id = str(python_dict['id'])
    #facebook_email = response_dict['email']
    user = User.query.filter_by(facebook_id=facebook_id).first()
    if user == None:
    	user = User('fb%s' % facebook_id, '', '', facebook_id)
    	db.session.add(user)
    	db.session.commit()
    login_user(user)
    return redirect(next_url)

login_manager.login_view = 'login'

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
		return correctPassword == PasswordField

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

@app.route('/facebookAuthenticate')
def facebookAuthenticate():
	return facebook.authorize(callback=url_for('oauth_authorized',
    	next=request.args.get('next') or request.referrer or None,
    	_external={'SERVER_NAME':'localhost'}))

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return send_file('../public/' + path)
