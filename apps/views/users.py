import os
from flask import (
    Blueprint,
    views,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    current_app,
    send_from_directory
)
from apps.models import User
from apps.forms import RegisterForm,LoginForm
from apps.extensions import db
from apps.email import send_mail
from flask_login import login_user,logout_user,login_required,current_user
#pip install pillow
from PIL import Image
#实例化蓝本对象
users = Blueprint('users',__name__)


class RegisterView(views.MethodView):
    #get请求 我们用来 展示页面
    def get(self,message=None):
        form = RegisterForm()
        return render_template('users/register.html',form=form,message=message)
    #post请求用来 实现 用户提交数据到服务器
    def post(self):
        form = RegisterForm(request.form) #实例化表单对象
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            email = form.email.data
            u = User(username=username,password=password,email=email)
            db.session.add(u)
            db.session.commit()
            #如果注册成功 生成token    该token会通过邮件发送给 用户注册时填的邮箱
            token = u.gernerate_active_token()
            # print(token)
            #发送邮件
            send_mail(u.email,'账户激活','mail/activate',username=u.username,token=token)
            #弹出小时提示用户
            flash("用户已经注册,请点击链接完成激活")
            return redirect(url_for('main.index'))
        else:
            return self.get(message="您的输入不符合要求")
users.add_url_rule('/register/',view_func=RegisterView.as_view('register'))

#http://127.0.0.1:5000/activate/你的token
@users.route('/activate/<token>/')
def activate(token):
    if User.check_active_token(token):
        flash('账户已经激活')
        return redirect(url_for('users.login'))
    else:
        flash('激活失败')
        return redirect(url_for('main.index'))


class LoginView(views.MethodView):
    #get请求 我们用来 展示页面
    def get(self,message=None):
        form = LoginForm()
        return render_template('users/login.html',form=form,message=message)
    #post请求用来 实现 用户提交数据到服务器
    def post(self):
        form = LoginForm(request.form) #实例化表单对象
        if form.validate_on_submit():
            #根据用户输入的 用户名 去数据库中查询
            u = User.query.filter_by(username=form.username.data).first()
            if not u:
                flash('该用户不存在')
            elif not u.confirmed:
                flash('请先移步邮箱激活该用户')
            elif u.verify_password(form.password.data):
                # 1.将 用户id 或者用户名写入session
                #2.如果点击了 记住我 那么让过期时间延长
                login_user(u,remember=form.remember.data)
                #duration = timedelta(seconds=100)  设置过期时间的写法
                # login_user(u, remember=form.remember.data,duration=duration)
                flash('登录成功')
                #http://10.211.55.3:5000/users/login/?next=%2Fusers%2Fprofile%2F
                return redirect(request.args.get('next') or url_for('main.index'))
        else:
            return self.get(message="您的输入不符合要求")

users.add_url_rule('/login/',view_func=LoginView.as_view('login'))

@users.route('/logout/')
def logout():
    logout_user()
    flash("注销成功")
    return redirect(url_for('main.index'))

@users.route('/profile/')
@login_required #必须先登录才可以查看个人中心
def profile():
    return '个人中心'

@users.route('/change_icon/',methods=['GET','POST'])
@login_required
def change_icon():
    # form = UploadedForm()  nikun.jpg
    img_url = None
    if request.method == "POST":
        file = request.files.get("icon")
        if file and allowed_file(file.filename):
            # file.filename 上传文件名
            suffix = os.path.splitext(file.filename)[1]
            filename = random_string() + suffix
            file.save(os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'], filename))

            pathname = os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'], filename)
            #打开图片
            img = Image.open(pathname)

            #重设尺寸
            img.thumbnail((128,128))
            #保存修改
            img.save(pathname)

            #文件上传成功以后
            # gaogao123   qfnz.jpg  qf.png  python.gif
            if current_user.icon != 'qfnz.jpg':
                os.remove(os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'], current_user.icon))

            current_user.icon = filename
            db.session.add(current_user)
            db.session.commit()
            flash('头像已经保存')
            return redirect(url_for('users.change_icon'))
    img_url = url_for('users.uploaded',filename=current_user.icon)
    return render_template('users/change_icon.html',img_url=img_url)

#判断后缀名是否合法
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1] in current_app.config['ALLOWED_EXTENSIONS']




#生成随机字符串
def random_string(length=16):
    import random
    base_dir = 'qwertyuiopasdfghjklzxcvbnm0123456789'
    return ''.join(random.choice(base_dir) for i in range(length))

#获取上传的文件

#http://127.0.0.1:5005/uploaded/123.jpg
@users.route('/uploaded/<filename>/')
def uploaded(filename):
    return send_from_directory(current_app.config['UPLOADED_PHOTOS_DEST'],filename)
