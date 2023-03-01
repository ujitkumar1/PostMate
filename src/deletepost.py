from flask import session, redirect, url_for, flash
from flask_restful import Resource

from src import db
from models import BlogPost


class DeletePost(Resource):
    def get(self, post_id):
        if 'username' not in session:
            return redirect(url_for('login'))
        post = BlogPost.query.filter_by(id=post_id, user_id=session['user_id']).first()
        if post:
            db.session.delete(post)
            db.session.commit()
            flash("Post deleted successfully")
            return redirect('/viewposts')

        else:
            flash("Access Denied: You are not authorized to delete this post")
            return redirect('/viewposts')
