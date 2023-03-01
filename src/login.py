from flask import render_template, make_response, request, session, redirect
from flask_restful import Resource

from models import User


class Login(Resource):
    def get(self):
        return make_response(render_template('login.html'), 200)

    def post(self):
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            session['username'] = username
            session['user_id'] = user.id
            return redirect('/home')
        else:
            return 'Invalid username/password combination', 400
