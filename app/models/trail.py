from app import db
from datetime import datetime

class Trail(db.model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.now())
    topic = db.Column(db.String, nullable=False)
    popularity_count = db.Column(db.Integer)
    user_id = db.Column(db.Integer, ForeignKey=("users.id"))
    parent_id = db.Column(db.Integer, ForeignKey=("trail.id"))
    trial_type = db.Column(db.String, nullable=False)

    def __init__(self, id, topic, popularity_count, trial_type):
        self.id = id
        self.topic = topic
        self.popularity_count = 0
        self.trial_type = trial_type