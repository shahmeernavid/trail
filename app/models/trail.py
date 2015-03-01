from app import db
from datetime import datetime
from app.models.trail_step_join import TrailStepJoin
from app.models.follow import Follow

class Trail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.now())
    topic = db.Column(db.String, nullable=False)
    popularity_count = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    parent_id = db.Column(db.Integer, db.ForeignKey("trail.id"))
    trail_type = db.Column(db.String, nullable=False)

    trail_step_joins = db.relationship(TrailStepJoin, backref='trail', lazy='dynamic')
    follows = db.relationship(Follow, backref='trail', lazy='dynamic')

    def __init__(self):
        self.id
        self.date_created
        self.topic
        self.popularity_count
        self.user_id
        self.parent_id
        self.trail_type
