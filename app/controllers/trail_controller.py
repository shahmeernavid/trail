from app import db, login_manager, app
from app.models.user import User
from flask_wtf import Form
from flask import render_template, flash, redirect, request, url_for, session, send_file
from wtforms import validators, TextField, PasswordField
from flask.ext.login import login_user, logout_user, login_required
import hashlib
from flask_oauth import OAuth

@app.route('/trail/<int: trail_id>', methods=['GET'])
def get(trail_id):
    trail = Trail.query.get(trail_id)
    return jsonify(** trail.serialize())

@app.route('/trail/', methods=['POST'])
def create():
    request_dict = request.get_json()
    trail = trail(request_dict.id, request_dict.topic, request_dict.popularity_count, request_dict.trail_type)
    db.session.add(trail)
    db.session.commit()

@app.route('/trail/<int: trail_id>', methods=['PUT'])
def update(trail_id):
    request_dict = request.get_json()
    trail = Trail.query.get(trail_id)

    trail.id = request_dict.id
    trail.topic = request_dict.topic
    trail.popularity_count = request_dict.popularity_count
    trail.trail_type = request_dict.trail_type

    db.session.add(trail)
    db.session.commit()

@app.route('/trail/<int: trail_id/delete', methods=['POST'])
def delete(trail_id):
    request_dict = request.get_json()
    trail = Trail.query.get(trail_id)

    db.session.delete(trail)
    db.session.commit()