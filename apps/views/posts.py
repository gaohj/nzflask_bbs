from flask import Blueprint

#实例化蓝本对象
posts = Blueprint('posts',__name__)

@posts.route('/',methods=['GET','POST'])
def index():
    return '我是收藏的首页'