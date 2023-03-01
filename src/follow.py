from flask import session, redirect
from flask_restful import Resource

from src import db
from models import User


class Follow(Resource):
    def get(self, username):
        user = User.query.filter_by(username=username).first()
        current_user = User.query.filter_by(username=session['username']).first()
        current_user.follow(user)
        db.session.commit()
        return redirect('/profile/' + username)
