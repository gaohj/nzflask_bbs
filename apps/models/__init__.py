from .users import User
from .posts import Posts
from apps.extensions import db

collections = db.Table('collections',
    db.Column('user_id',db.Integer,db.ForeignKey('users.id')),
    db.Column('posts_id',db.Integer,db.ForeignKey('posts.id'))
)

