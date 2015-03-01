from app import db, login_manager, app
from app.models.user import User
from flask_wtf import Form
from flask import render_template, flash, redirect, request, url_for, session, send_file
from wtforms import validators, TextField, PasswordField
from flask.ext.login import login_user, logout_user, login_required
import hashlib
from flask_oauth import OAuth

@app.route('/step/<int: step_id>', methods=['GET'])
def get(step_id):
    step = Step.query.get(step_id)
    return jsonify(** step.serialize())

@app.route('/step/', methods=['POST'])
def create():
    request_dict = request.get_json()
    step = step(request_dict.id, request_dict.resource, request_dict.title, request_dict.description, request_dict.completed)
    db.session.add(step)
    db.session.commit()

@app.route('/step/<int: step_id>', methods=['PUT'])
def update(step_id):
    request_dict = request.get_json()
    step = Step.query.get(step_id)

    step.resource = request_dict.resource
    step.title = request_dict.title
    step.description = request_dict.description
    step.completed = request_dict.completed

    db.session.add(step)
    db.session.commit()

@app.route('/step/<int: step_id/delete', methods=['POST'])
def delete(step_id):
    request_dict = request.get_json()
    trail = Trail.query.get(step_id)

    db.session.delete(step)
    db.session.commit()