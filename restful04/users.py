from flask import Blueprint,render_template,make_response
from flask_restful import Resource,Api,marshal_with,fields
from models import Article
user_bp = Blueprint('user',__name__,url_prefix='/users')
api =Api(user_bp)

@api.representation('text/html') #告诉浏览器这是一个页面
def output_html(data,code,headers):
    resp = make_response(data)
    return resp



class UserView(Resource):
    def get(self):
        return render_template('user.html') #直接返回返回的是一个字符串
    #浏览器不解析   想让它解析 就得告诉浏览器这是个html页面
    def post(self):
        return '情人节快乐,放开双手勇敢的干'

api.add_resource(UserView,'/')

