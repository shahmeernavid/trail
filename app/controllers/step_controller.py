from app import db, app
from app.models.step import Step
from app.models.trail_step_join import TrailStepJoin
from flask import jsonify, request
import json

@app.route('/step/<int:step_id>', methods=['GET', 'PUT'])
def get_or_update_step(step_id):
    if request.method == 'GET':
        step = Step.query.get(step_id)
        return jsonify(** step.serialize())
    else:
        request_dict = request.get_json()
        step = Step.query.get(step_id)

        step.resource = request_dict.resource
        step.title = request_dict.title
        step.description = request_dict.description
        step.completed = request_dict.completed

        db.session.add(step)
        db.session.commit()
        return jsonify(**{'id': step.id})       

@app.route('/step', methods=['POST'])
def create_step():
    request_dict = request.get_json()
    step = Step(request_dict['resource'], request_dict['title'], request_dict['description'])
    db.session.add(step)
    db.session.commit()
    return jsonify(**{'id': step.id})

@app.route('/step/delete/<int:step_id>', methods=['POST'])
def delete_step(step_id):
    step = Step.query.get(step_id)

    db.session.delete(step)
    db.session.commit()
    return jsonify(**{'id': step.id})

@app.route('/steps', methods=['GET'])
def list_steps():
    steps = Step.query.all()
    return json.dump([step.serialize() for step in steps])

@app.route('/steps/<string>', methods=['GET'])
def search_steps(string):
    steps = Step.query.filter(Step.title.contains(string)).all()
    return json.dump([step.serialize() for step in steps])

@app.route('/steps/trail/<int:trail_id>', methods=['GET'])
def steps_part_of_trail(trail_id):
    trail_step_joins = TrailStepJoin.query.filter_by(trail_id = trail_id).all()
    ids = [trail_step_join.step_id for trail_step_join in trail_step_joins]
    steps = Step.query.filter(Step.id.in_(ids)).all()
    return json.dump([step.serialize() for step in steps])

