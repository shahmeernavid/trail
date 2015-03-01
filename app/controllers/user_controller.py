from app import db, app
from app.models.user import User
from app.models.follow import Follow
from flask import jsonify
import json

@app.route('/user/create', methods=['POST'])
def create():
	request_dict = request.get_json()
	user = User(request_dict['username'], request_dict['password'], request_dict['email'], None)
	db.session.add(user)
	db.session.commit()
	return jsonify(**{'id': user.id})

@app.route('/users/trail/<int:trail_id>', methods=['GET'])
def users_following_trail(trail_id):
 	follows = Follow.query.filter_by(trail_id = trail_id).all()
 	ids = [follow.user_id for follow in follows]
 	users = User.query.filter(User.id.in_(ids)).all()
  	return json.dumps([user.serialize() for user in users])