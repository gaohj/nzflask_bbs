#encoding:utf-8
from extensions import db
#用户
#文章
#标签


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(50))

article_tag_table = db.Table('article_tag',
    db.Column('article_id',db.Integer,db.ForeignKey('article.id'),primary_key=True),
    db.Column('tag_id',db.Integer,db.ForeignKey('tags.id'),primary_key=True),
)

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    author = db.relationship('User',backref='articles')

    tags = db.relationship('Tag',secondary=article_tag_table,backref='tag')

class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))
