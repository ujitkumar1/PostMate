from flask import session, redirect
from flask_restful import Resource

from src import db
from models import User


class UnFollowUser(Resource):
    def get(self, username):
        current_user = User.query.filter_by(username=session['username']).first()
        user_to_unfollow = User.query.filter_by(username=username).first()
        current_user.following.remove(user_to_unfollow)
        db.session.commit()
        return redirect('/search')
