from app import db
from datetime import datetime

class Trail(db.model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.now())
    topic = db.Column(db.String, nullable=False)
    popularity_count = db.Column(db.Integer)
    user_id = db.Column(db.Integer, ForeignKey=("users.id"))
    parent_id = db.Column(db.Integer, ForeignKey=("trail.id"))
    trail_type = db.Column(db.String, nullable=False)

    def __init__(self, id, topic, popularity_count, trail_type):
        self.id = id
        self.topic = topic
        self.popularity_count = 0
        self.trail_type = trail_type

    def serialize(self):
        serialized_trail = {
            "id": self.id,
            "date_created": self.date_created,
            "topic": self.topic,
            "popularity_count": self.popularity_count,
            "user_id": self.user_id,
            "parent_id": self.parent_id,
            "trail_type": self.trail_type,
        }
        return serialized_trail