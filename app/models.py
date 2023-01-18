from datetime import datetime

from app import db


class BlogPost(db.Model):
    __tablename__ = 'blog_posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    caption = db.Column(db.String(200), nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('author_of_post', lazy=True))


followers = db.Table('followers',
                     db.Column('follower_id', db.Integer, db.ForeignKey('users.id')),
                     db.Column('followed_id', db.Integer, db.ForeignKey('users.id'))
                     )
followers_table = followers


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70))
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('BlogPost', backref='author_of_post', lazy=True)
    following = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')

    def is_following(self, user):
        return self.following.filter(followers.c.followed_id == user.id).count() > 0
