from flask import make_response, render_template, session, request, redirect
from flask_restful import Resource

from models import User


class Search(Resource):
    def get(self):
        if 'username' not in session:
            return redirect('/')
        return make_response(render_template('search.html', username=session['username']), 200)

    def post(self):
        search_term = request.form['search_term']
        if search_term:
            users = User.query.filter(User.username.like('%' + search_term + '%')).all()
            current_user = User.query.filter_by(username=session['username']).first()
            for user in users:
                user.is_following_status = current_user.is_following(user)
            return make_response(render_template('search.html', users=users, username=session['username']), 200)
        else:
            return redirect("/search")
