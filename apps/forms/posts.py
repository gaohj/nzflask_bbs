from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField
from wtforms.validators import Length

class PostsForm(FlaskForm):
    content = TextAreaField('',render_kw={'placeholder':'这一刻你想说点什么...'},validators=[Length(10,140,message='说话注意分寸(10~140)')])
    submit = SubmitField('发表')
