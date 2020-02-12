from .users import User
from .posts import Posts
from apps.extensions import db


# 添加用户与帖子的收藏中间关联表  表名.字段
collections = db.Table('collections',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('posts_id', db.Integer, db.ForeignKey('posts.id'))
)

#一个用户可以收藏多个帖子

#一个帖子可以被多个用户收藏

#多对多我们是通过 中间表来实现



