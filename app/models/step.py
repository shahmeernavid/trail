from app import db
import os
import hashlib
from datetime import datetime
from app.models.trail_step_join import TrailStepJoin

class Step(db.Model):
    # AUTOINCREMENT NOT NULL UNIQUE
    id = db.Column(db.Integer, primary_key=True)
    resource = db.Column(db.String, nullable=False)
    title = db.Column(db.VARCHAR(50), nullable=False)
    description = db.Column(db.VARCHAR(140))
    completed = db.Column(db.Boolean, nullable=False, default=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.now())

    trail_step_join = db.relationship(TrailStepJoin, backref='step', lazy='dynamic')

    def __init__(self, resource, title, description, parent):
        self.resource = resource
        self.title = title
        self.description = description
        self.completed = False

    # increment counter of the parent
    # all trails it points to, updates trails

    def set_resource(self, resource):
        self.resource = resource

    def set_title(self, title):
        self.title = title

    def set_description(self, description):
        self.description = description

    def complete_step(self):
        self.completed = True

    def remove_step(self):
        self.id = None
        self.resource = None
        self.title = None
        self.description = None
        self.completed = None
        self.date_created = None