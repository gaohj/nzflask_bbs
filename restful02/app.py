from flask import Flask
from flask_script import  Manager
from flask_restful import Api,Resource,reqparse

#接口继承于 flask_restful.Resource类
app = Flask(__name__)
manager = Manager(app)
api = Api(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

class LoginView(Resource):
    def get(self):
        return {'username':'kunge是传说'}

    def post(self):
        return {'username': '你是post过来想添加数据是么'}

    def put(self):
        return {'username': '你是put过来想添加修改数据是么记住要提交所有的字段'}

    def patch(self):
        return {'username': '你是patch过来 请提交想修改的字段'}

    def delete(self):
        return {'username': '删除数据一定要慎重'}


class RegisterView(Resource):
    def post(self):
        parser = reqparse.RequestParser() #对输入的字段进行验证
        parser.add_argument('username',required=True,type=float,help='用户名验证错误')
        parser.add_argument('password',type=str,help='密码验证错误')
        parser.add_argument('age',type=int,help='年龄验证错误')
        parser.add_argument('gender',type=str,choices=['male','female','secret'])
        args = parser.parse_args()
        return {'result':'添加成功'}

api.add_resource(LoginView,'/signin/')
api.add_resource(RegisterView,'/signup/')



if __name__ == '__main__':
    manager.run()
