from app import db, app
from app.models.trail import Trail
from app.models.follow import Follow
from app.models.user import User
from flask import jsonify, request
import json

@app.route('follow/create/<int:trail_id>/<int:user_id>')
def create_follow(trail_id, user_id):
	follow = Follow(trail_id, user_id)
	db.session.add(follow)
	db.sesion.commit()
	return jsonify(**{'id' : follow.id})

@app.route('follow/delete/<int:trail_id>/<int:user_id>')
def delete_follow(trail_id, user_id):
	follow = Follow.query.filter_by(trail_id = trail_id).filter_by(user_id = user_id).first()
	db.session.delete(follow)
	db.sesion.commit()
	return jsonify(**{'id' : follow.id})