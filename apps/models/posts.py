from apps.extensions import db
from datetime import datetime
#  id    rid
#   1     0
#   2     0
#   3     0
#   4     1
#   5     3


class Posts(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    rid = db.Column(db.Integer, index=True, default=0)
    content = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    # 添加关联外键: '表名.字段'
    uid = db.Column(db.Integer, db.ForeignKey('users.id'))
