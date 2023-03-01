from flask import session, render_template, redirect, make_response
from flask_restful import Resource

from models import BlogPost, User


class ViewPosts(Resource):
    def get(self):
        if 'username' not in session:
            return make_response(redirect('/'))
        posts = BlogPost.query.filter_by(user_id=session['user_id']).all()
        return make_response(render_template('viewposts.html', posts=posts, user=User.query.get(session['user_id'])),200)
