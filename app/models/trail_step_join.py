from app import db

class TrialsToSteps(db.model):
    trial.id = db.column(db.Integer, ForeignKey=("trials.id"), primary_key=True)
    step.id = db.column(db.Integer, ForeignKey=("steps.id"), primary_key=True)

    def __init__(self):


