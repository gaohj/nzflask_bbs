from flask import Flask
from flask_script import Manager
from flask_restful import Api,Resource,reqparse,inputs
#reqparse 类似于 wtforms  验证数据的合法性
app = Flask(__name__)
manager = Manager(app)
api = Api(app)
@app.route('/')
def hello_world():
    return 'Hello World!'

class RegisterView(Resource):
    def post(self):
        from datetime import date #因为我们验证的要求是
        #2020-02-02
        parser = reqparse.RequestParser()
        parser.add_argument('username',required=True,type=str,help='请输入正确用户名')
        parser.add_argument('password',required=True,type=str,help='密码验证错误')
        parser.add_argument('age',type=int,help='年龄验证错误')
        parser.add_argument('gender',type=str,choices=['male','female','secret'],trim=True)
        parser.add_argument('homepage',type=inputs.url,help='个人中心链接验证错误')
        parser.add_argument('telephone',type=inputs.regex(r'1[3456789]\d{9}'),help='请输入正确的手机号')
        parser.add_argument('birth',type=inputs.date,help='生日字段验证错误')
        args = parser.parse_args()
        print(args)
        return {'username':'kangbazi'}

api.add_resource(RegisterView,'/signup/')



if __name__ == '__main__':
    manager.run()
