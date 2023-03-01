from flask import session, url_for, redirect
from flask_restful import Resource

from src import db
from models import User


class FollowUser(Resource):
    def get(self, username):
        if 'username' not in session:
            return redirect(url_for('login'), 403)
        user_to_follow = User.query.filter_by(username=username).first()
        current_user = User.query.filter_by(username=session['username']).first()
        current_user.following.append(user_to_follow)
        db.session.commit()
        return redirect('/search')
