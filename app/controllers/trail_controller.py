from app import db, app
from app.models.trail import Trail
from app.models.trail_step_join import TrailStepJoin
from app.models.follow import Follow
from flask import jsonify, request
import json
from app.controllers.invalid_usage import InvalidUsage

@app.route('/trail/<int:trail_id>', methods=['GET', 'PUT', 'POST'])
def get_or_update_trail(trail_id):
    if request.method == 'GET':
        trail = Trail.query.get(trail_id)
        return jsonify(** trail.serialize())
    elif request.method == 'PUT':
        request_dict = request.get_json()
        trail = Trail.query.get(trail_id)

        trail.topic = request_dict['topic']
        trail.trail_type = request_dict['trail_type']

        db.session.commit()
        return jsonify(**{'id' : trail.id})
    else:
        if request.args.get('action') == 'duplicate':
            trail = Trail.query.get(trail_id)
            new_trail = Trail(trail.topic, request.get_json()['user_id'], trail.id, "followed")
            db.session.add(new_trail)
            db.session.commit()
            trail_step_joins = TrailStepJoin.query.filter_by(trail_id = trail_id).all()
            ids = [trail_step_join.step_id for trail_step_join in trail_step_joins]
            for step_id in ids:
                new_trail_step_join = TrailStepJoin(new_trail.id, step_id)
                db.session.add(new_trail_step_join)
            db.session.commit()
            return jsonify(**{'id' : new_trail.id})
        else:
            raise InvalidUsage('Sending POST request requires ?action=duplicate', status_code=400)


@app.route('/trail/', methods=['POST'])
def create_trail():
    request_dict = request.get_json()
    trail = trail(request_dict['topic'], request_dict['user_id'], request_dict['parent_id'], request_dict['trail_type'])
    db.session.add(trail)
    db.session.commit()
    return jsonify(**{'id' : trail.id})

@app.route('/trail/delete/<int:trail_id>', methods=['POST'])
def delete_trail(trail_id):
    request_dict = request.get_json()
    trail = Trail.query.get(trail_id)

    db.session.delete(trail)
    db.session.commit()
    return jsonify(**{'id' : trail.id})

@app.route('/trails', methods=['GET'])
def list_trails():
    trails = Trail.query.all()
    return json.dumps([trail.serialize() for trail in trails])

@app.route('/trails/<string>', methods=['GET'])
def search_trails():
    trails = Trail.query.filter(Trail.topic.contains(string)).all()
    return json.dumps([trail.serialize() for trail in trails])

@app.route('/trails/user/<int:user_id>', methods=['GET'])
def trails_followed_by_user(user_id):
    follows = Follow.query.filter_by(user_id = user_id).all()
    ids = [follow.trail_id for follow in follows]
    trails = Trail.query.filter(Trail.id.in_(ids)).all()
    return json.dumps([trail.serialize() for trail in trails])

@app.route('/trails/step/<int:step_id>', methods=['GET'])
def trails_containing_step(step_id):
    trail_step_joins = TrailStepJoin.query.filter_by(step_id = step_id).all()
    ids = [trail_step_join.trail_id for trail_step_join in trail_step_joins]
    trails = Trail.query.filter(Trail.id.in_(ids)).all()
    return json.dumps([trail.serialize() for trail in trails])
