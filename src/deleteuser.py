from flask import redirect, session
from flask_restful import Resource

from src import db
from models import User, followers


class DeleteUser(Resource):
    def get(self, username):
        if 'username' not in session:
            return redirect('/')
        user = User.query.filter_by(username=username).first()
        if session["username"] == username:
            if user:
                for post in user.posts:
                    db.session.delete(post)
                db.session.query(followers).filter(
                    (followers.c.follower_id == user.id) | (followers.c.followed_id == user.id)
                ).delete(synchronize_session='fetch')
                db.session.query(followers).filter(
                    (followers.c.follower_id == user.id) | (followers.c.followed_id == user.id)
                ).delete(synchronize_session='fetch')
                db.session.delete(user)
                db.session.commit()
                return redirect('/')
            else:
                return redirect('/')
        else:
            return "Not allowed to delete"
