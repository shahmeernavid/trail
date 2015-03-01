from app import db

class Follow(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	trail_id = db.Column(db.Integer, db.ForeignKey("trail.id"))
	user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

	def __init__(self, trail_id, user_id):
		self.trail_id = trail_id
		self.user_id = user_id