from app import db
from datetime import datetime
from app.models.trail_step_join import TrailStepJoin
from app.models.follow import Follow
from app.models.user import User

class Trail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.now())
    topic = db.Column(db.String, nullable=False)
    popularity_count = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    parent_id = db.Column(db.Integer, db.ForeignKey("trail.id"))
    trail_type = db.Column(db.String, nullable=False)

    follows = db.relationship(Follow, backref='trail', lazy='dynamic')
    trail_step_joins = db.relationship(TrailStepJoin, backref='trail', lazy='dynamic')

    def __init__(self, topic, user_id, parent_id, trail_type):
        self.topic = topic
        self.popularity_count = 0
        self.user_id = user_id
        self.parent_id = parent_id
        self.trail_type = trail_type

    def serialize(self):
        serialized_trail = {
            "id": self.id,
            "date_created": self.date_created.strftime('%Y-%m-%dT%H:%M:%S'),
            "topic": self.topic,
            "popularity_count": self.popularity_count,
            "user_id": self.user_id,
            "parent_id": self.parent_id,
            "trail_type": self.trail_type,
        }
        return serialized_trail

    def upvote(self):
        self.popularity_count += 1

    def downvote(self):
        self.popularity_count -= 1
