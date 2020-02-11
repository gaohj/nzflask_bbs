from apps.extensions import db,login_manager
from flask import current_app,flash #current_app代表当前的实例
from werkzeug.security import generate_password_hash,check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_login import  UserMixin
class User(UserMixin,db.Model):
    __tablename__ = 'users' #指定数据表的名称
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(32),unique=True) #用户名唯一性
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(64),unique=True)
    confirmed = db.Column(db.Boolean,default=False)
    icon = db.Column(db.String(64),default='qfnz.jpg')

    posts = db.relationship('Posts',backref='user',lazy='dynamic')

    #实现密码 加密
    #对内 password_hash  对外  password
    @property  #把方法当作属性来对待
    def password(self):
        raise AttributeError('密码不可读')

    @password.setter
    def password(self,password): #参数是用户提交过来的密码
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    #afasfdsafdsafadsfq3eqw2323w3434
    #adfadfds23233rdsfaewer33wewwere
    #生成token 需要通过邮件发送给用户
    def gernerate_active_token(self,expires_in=3600):
        s = Serializer(current_app.config['SECRET_KEY'],expires_in=expires_in)
        return s.dumps({'id':self.id})

    #解密token
    @staticmethod
    def check_active_token(token):
        #token是用户带过来的
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False

        u = User.query.get(data.get('id'))
        if not u:
            flash('用户不存在')
            return False
        if not u.confirmed:
            u.confirmed = True
            db.session.add(u)
            db.session.commit()
        return True
#http://10.211.55.3:5000/users/activate/eyJhbGciOiJIUzUxMiIsImlhdCI6MTU4MTMyODc4NiwiZXhwIjoxNTgxMzMyMzg2fQ.eyJpZCI6MTN9.ICBdqzb963SWIbgsgfEC3KR0Ck75tZw2s19nHg2PlUITQnkkgq91ZT-dvv3CZBBTiYpUe1fxfwnPbwYRNOh00A/

#登录成功之后的回调函数
#你登陆成功了 拿到你的详细信息  然后在页面上显示  你好玉玉

@login_manager.user_loader
def load_user(uid):
    return User.query.get(int(uid))