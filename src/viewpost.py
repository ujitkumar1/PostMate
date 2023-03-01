from flask import session, render_template, redirect, url_for, make_response
from flask_restful import Resource

from models import BlogPost, User


class ViewPost(Resource):
    def get(self, post_id):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        post = BlogPost.query.filter_by(id=post_id, user_id=session['user_id']).first()
        if post:
            return make_response(render_template('viewpost.html', post=post, user=User.query.get(session['user_id'])),
                                 200)
        else:
            return 'Access Denied! The post does not belong to the current user.', 404
