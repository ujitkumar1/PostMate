import os

from flask import session, redirect, request, render_template, make_response
from flask_restful import Resource
from werkzeug.utils import secure_filename

from src import db, app
from models import BlogPost


class CreatePost(Resource):
    def post(self):
        if session:
            title = request.form['title']
            caption = request.form['caption']
            try:
                file = request.files['file']
                if file and self.allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    image_url = filename
                    blog_post = BlogPost(title=title, caption=caption, image_url=image_url, user_id=session["user_id"])
                    db.session.add(blog_post)
                    db.session.commit()
                    return redirect('/viewposts')
                else:
                    return {"message": "Invalid file format. Allowed formats are jpg, jpeg, png, gif"}, 400
            except Exception as e:
                return {"message": str(e)}, 500

    def get(self):
        if 'username' not in session:
            return redirect('/')
        return make_response(render_template('createpost.html', username=session['username']), 200)

    def allowed_file(self, filename):
        ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
