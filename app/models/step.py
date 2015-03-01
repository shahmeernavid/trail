from app import db
import os
from datetime import datetime

class Step(db.model):
    # AUTOINCREMENT NOT NULL UNIQUE
    id = db.Column(db.Integer, primary_key=True)
    resource = db.Column(db.String, nullable=False)
    title = db.Column(db.varchar(50), nullable=False)
    description = db.Column(db.varchar(140))
    completed = db.Column(db.Boolean, nullable=False, default=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.now())

    def __init__(self, resource, title, description, parent):
        self.resource = resource
        self.title = title
        self.description = description
        self.completed = False

    def serialize(self):
        serialized_step = {
            "id": self.id,
            "resource": self.resource,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "date_created": self.date_created,
        }
        return serialized_step