from app import db
import os
import hashlib
from app.models.follow import Follow

class User(db.Model):
	id = db.Column(db.Integer, nullable=False, primary_key=True)
	username = db.Column(db.String)
	password = db.Column(db.String)
	salt = db.Column(db.String)
	email = db.Column(db.String)
	facebook_id = db.Column(db.String)

	follows = db.relationship(Follow, backref='user', lazy='dynamic')

	def __init__(self, username, password, email, facebook_id):
		self.salt = os.urandom(16).encode('base_64')
		self.password = hashlib.sha256(self.salt + password).hexdigest()
		self.username = username
		self.email = email
		self.facebook_id = facebook_id

	def __repr__(self):
		return '<User: %s>' % self.id

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		try:
			return unicode(self.id)  # python 2
		except NameError:
			return str(self.id)  # python 3
