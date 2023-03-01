from flask import request, render_template, make_response, redirect, session
from flask_restful import Resource

from src import db
from models import User, BlogPost


class UpdateUser(Resource):
    def get(self, user_id):
        if 'username' not in session:
            return make_response(redirect('/'))
        else:
            if session["user_id"] == user_id:
                user = User.query.filter_by(id=user_id).first()
                return make_response(render_template('updateuser.html', user=user), 200)
            else:
                return "Not Allowed to update other user profile", 401

    def post(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        name = request.form['name']
        password = request.form['password']
        user.name = name
        user.password = password
        db.session.commit()
        number_of_blogs = BlogPost.query.filter_by(user_id=user.id).count()
        number_of_followers = user.followers.count()
        number_of_followed = user.following.count()
        posts = BlogPost.query.filter_by(user_id=user.id).all()
        return make_response(render_template('profile.html', user=user, number_of_blogs=number_of_blogs,
                                             number_of_followers=number_of_followers,
                                             number_of_followed=number_of_followed,
                                             posts=posts), 200)
