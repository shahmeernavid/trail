from app import db
from datetime import datetime

class Trail(db.model):
    id = db.column(db.Integer, primary_key=True)
    date_created = db.column(db.DateTime, nullable=False, default=datetime.now())
    topic = db.column(db.text, nullable=False)
    popularity_count = db.column(db.Integer)
    user_id = db.column(db.Integer, ForeignKey=("users.id"))
    parent_id = db.column(db.Integer, ForeignKey=("trail.id"))
    trial_type = db.column(db.text, nullable=False)

    def __init__(self):
        self.id
        self.date_created
        self.topic
        self.popularity_count
        self.user_id
        self.parent_id
        self.trial_type

    def add_trail():

    def remove_trail():

has many steps
