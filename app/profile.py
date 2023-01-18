from flask import make_response, render_template, session, redirect
from flask_restful import Resource

from models import User, BlogPost


class Profile(Resource):
    def get(self, username):
        if 'username' not in session:
            return make_response(redirect('/'), 403)
        user = User.query.filter_by(username=username).first()
        if user is None:
            return "User not found", 404
        number_of_blogs = BlogPost.query.filter_by(user_id=user.id).count()
        number_of_followers = user.followers.count()
        number_of_followed = user.following.count()
        posts = BlogPost.query.filter_by(user_id=user.id).all()
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('profile.html', user=user, number_of_blogs=number_of_blogs,
                                             number_of_followers=number_of_followers,
                                             number_of_followed=number_of_followed,
                                             posts=posts), 200)
