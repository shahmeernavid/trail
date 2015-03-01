from app import db, app
from app.models.step import Step
from app.models.trail_step_join import TrailStepJoin
from app.models.trail import Trail
from app.controllers.invalid_usage import InvalidUsage
from flask import jsonify, request
import json

@app.route('/step/<int:step_id>', methods=['GET', 'PUT', 'POST'])
def get_or_update_step(step_id):
    if request.method == 'GET':
        step = Step.query.get(step_id)
        return jsonify(** step.serialize())
    elif request.method == 'PUT':
        request_dict = request.get_json()
        step = Step.query.get(step_id)

        step.resource = request_dict.resource
        step.title = request_dict.title
        step.description = request_dict.description
        step.completed = request_dict.completed

        db.session.commit()
        return jsonify(**{'id': step.id})       
    else:
        if request.args.get('action') == 'complete':
            trail_step_joins = TrailStepJoin.query.filter_by(step_id = step_id).all()
            ids = [trail_step_join.trail_id for trail_step_join in trail_step_joins]
            trails = Trail.query.filter(Trail.id.in_(ids)).all()
            for trail in trails:      
                trail.upvote()
            db.session.commit()
            return json.dumps([trail.id for trail in trails])     
        elif request.args.get('action') == 'uncomplete':
            trail_step_joins = TrailStepJoin.query.filter_by(step_id = step_id).all()
            ids = [trail_step_join.trail_id for trail_step_join in trail_step_joins]
            trails = Trail.query.filter(Trail.id.in_(ids)).all()
            for trail in trails:
                trail.downvote()
            db.session.commit()
            return json.dumps([trail.id for trail in trails])    
        else:
            raise InvalidUsage('Sending POST request requires ?action=complete or ?action=uncomplete', status_code=400)

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
    return json.dumps([step.serialize() for step in steps])

@app.route('/steps/<string>', methods=['GET'])
def search_steps(string):
    steps = Step.query.filter(Step.title.contains(string)).all()
    return json.dumps([step.serialize() for step in steps])

@app.route('/steps/trail/<int:trail_id>', methods=['GET'])
def steps_part_of_trail(trail_id):
    trail_step_joins = TrailStepJoin.query.filter_by(trail_id = trail_id).all()
    ids = [trail_step_join.step_id for trail_step_join in trail_step_joins]
    steps = Step.query.filter(Step.id.in_(ids)).all()
    return json.dumps([step.serialize() for step in steps])

