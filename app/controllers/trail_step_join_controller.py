from app import db, app
from app.models.trail import Trail
from app.models.trail_step_join import TrailStepJoin
from app.models.step import Step
from flask import jsonify, request
import json

@app.route('trail_step_join/create/<int:trail_id>/<int:step_id>')
def create_trail_step_join(trail_id, step_id):
	trail_step_join = TrailStepJoin(trail_id, step_id)
	db.session.add(trail_step_join)
	db.sesion.commit()
	return jsonify(**{'id' : trail_step_join.id})

@app.route('trail_step_join/delete/<int:trail_id>/<int:step_id>')
def delete_trail_step_join(trail_id, step_id):
	trail_step_join = TrailStepJoin.query.filter_by(trail_id = trail_id).filter_by(step_id = step_id).first()
	db.session.delete(trail_step_join)
	db.sesion.commit()
	return jsonify(**{'id' : trail_step_join.id})