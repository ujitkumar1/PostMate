import os

from flask import session, request, render_template, make_response, redirect
from flask_restful import Resource
from werkzeug.utils import secure_filename

from src import db, app
from models import BlogPost


class UpdatePost(Resource):
    def get(self, post_id):
        if 'username' not in session:
            return make_response(redirect('/'), 403)
        post = BlogPost.query.filter_by(id=post_id, user_id=session['user_id']).first()
        return make_response(render_template('updatepost.html', post=post), 200)

    def post(self, post_id):
        post = BlogPost.query.filter_by(id=post_id, user_id=session['user_id']).first()
        title = request.form['title']
        caption = request.form['caption']
        try:
            file = request.files['file']
            if file and self.allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                image_url = filename
                post.title = title
                post.caption = caption
                post.image_url = image_url
                db.session.commit()
                return make_response(render_template('viewpost.html', post=post, user=session['username']), 200)
            else:
                return {"message": "Invalid file format. Allowed formats are jpg, jpeg, png, gif"}, 400
        except Exception as e:
            return {"message": str(e)}, 500

    def allowed_file(self, filename):
        ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
