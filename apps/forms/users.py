from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,EqualTo,Email,ValidationError
from flask_wtf.file import FileField,FileRequired,FileAllowed
from apps.models import User
# from apps.extensions import photos

#用户注册表单
class RegisterForm(FlaskForm):
    username = StringField('用户名',validators=[DataRequired(),Length(4,30,message="用户名必须在4到30位之间")])
    password = PasswordField('密码',validators=[DataRequired(),Length(6,30,message="密码必须在4到30位之间")]) #密码
    confirm = PasswordField('确认密码',validators=[EqualTo('password',message="两次密码输入不一致")])    #确认密码
    email = StringField('邮箱',validators=[Email(message="邮箱格式不正确")])
    submit = SubmitField('立即注册')

    #validate_username
    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('该用户已经注册了,请选择其它用户名')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('该邮箱已经注册了,请选择其它邮箱')
#用户登录表单
class LoginForm(FlaskForm):
    username = StringField('用户名',validators=[DataRequired(),Length(4,30,message="用户名必须在4到30位之间")])
    password = PasswordField('密码',validators=[DataRequired(),Length(6,30,message="密码必须在4到30位之间")]) #密码
    remember = BooleanField('记住我')
    submit = SubmitField('立即登录')
#头像上传表单

# class UploadedForm(FlaskForm):
#     icon = FileField('头像',validators=[FileRequired('请选择头像'),FileAllowed(photos,message='只能上传图片')])
#     submit = SubmitField('立即上传')
