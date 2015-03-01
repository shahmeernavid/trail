from app import db
import os
import hashlib

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String)
	password = db.Column(db.String)
	salt = db.Column(db.String)
	email = db.Column(db.String)

	def __init__(self, username, password, email):
		self.salt = os.urandom(16).encode('base_64')
		self.password = hashlib.sha256(self.salt + password).hexdigest()
		self.username = username
		self.email = email

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
