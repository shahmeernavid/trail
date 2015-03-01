from app import db

class TrialsToSteps(db.model):
    trial_id = db.column(db.Integer, ForeignKey=("trials.id"), primary_key=True)
    step_id = db.column(db.Integer, ForeignKey=("steps.id"), primary_key=True)

    def __init__(self, trial_id, step_id):
        self.trial_id = trial_id
        self.step_id = step_id