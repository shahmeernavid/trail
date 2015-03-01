from app import db

class TrailStepJoin(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	trail_id = db.Column(db.Integer, db.ForeignKey("trail.id"))
	step_id = db.Column(db.Integer, db.ForeignKey("step.id"))

	def __init__(self, trail_id, self_id):
		self.trail_id = trail_id
		self.self_id = self_id