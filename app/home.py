from flask import make_response, render_template, session, redirect
from flask_restful import Resource

from models import User, followers, BlogPost


class Home(Resource):
    def get(self):
        if session:
            current_user = User.query.filter_by(username=session['username']).first()
            followed_posts = BlogPost.query.join(
                followers, (followers.c.followed_id == BlogPost.user_id)).filter(
                followers.c.follower_id == current_user.id).order_by(
                BlogPost.timestamp.desc()).all()
            return make_response(
                render_template('home.html', username=session['username'], followed_posts=followed_posts), 200)
        else:
            return redirect("/")
