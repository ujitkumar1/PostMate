from flask import render_template, make_response, request, session, redirect
from flask_restful import Resource

from src import db
from models import User


class Signup(Resource):
    def get(self):
        return make_response(render_template('signup.html'), 200)

    def post(self):
        username = request.form['username']
        name = request.form['name']
        password = request.form['password']
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return 'Username already exists!', 400
        else:
            new_user = User(username=username, password=password, name=name)
            db.session.add(new_user)
            db.session.commit()
            session['username'] = username
            session['user_id'] = new_user.id
            return redirect('/home')
