from flask import Blueprint,render_template

#实例化蓝本对象
main = Blueprint('main',__name__)

@main.route('/',methods=['GET','POST'])
def index():
    return render_template('main/index.html')

