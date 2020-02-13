from flask import Flask,jsonify,abort,request
from flask_script import Manager
app = Flask(__name__)
manager = Manager(app)
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth() #创建一个认证对象

#进行认证
@auth.verify_password
def verify_password(username,password):
    if username=='nikun' and password == 'kangbazi':
        return True
    return False

#定制认证的错误类型
@auth.error_handler
def unauthorized():
    return jsonify({'error':'没有登录禁止访问'}),403



#请求方法不是

data = [
    {
        'id':1,
        'title':'人生苦短我用python',
        'content':'好多人都说python语法简单,但是问题偏偏都出在语法上'
    },
    {
        'id': 2,
        'title': 'java从入门到放弃',
        'content': '爬虫经常改变反爬规则,python需要5行,java可能需要20行'
    }
]

@app.route('/')
def hello_world():
    return 'Hello World!'

#查找所有的资源
@app.route('/datas/',methods=['GET'])
@auth.login_required
def get_datas_list():
    return jsonify({'datas':data})

#获取指定的资源
@app.route('/data/<int:did>/',methods=['GET'])
def get_data(did):
    p = list(filter(lambda d:d['id'] == did,data))
    if len(p) == 0:
        abort(404)
    return jsonify({'data':p[0]})

#添加资源
@app.route('/data/',methods=['POST'])
def create_data():
    if not request.json or 'title' not in request.json or 'content' not in request.json:
        abort(400)
    p = {
        'id':data[-1]['id']+1, #id累加
        'title':request.json['title'], #接收前端提交过来的json数据
        'content':request.json['content'],
    }
    data.append(p)  #保存资源
    return jsonify({'datas':p}),201  #返回状态码

#修改资源
@app.route('/data/<int:did>/',methods=['PUT'])
def update_data(did):
    p = list(filter(lambda d: d['id'] == did, data))
    if len(p) == 0:
        abort(404)
    if 'title' in request.json:
        p[0]['title'] = request.json['title']
    if 'content' in request.json:
        p[0]['content'] = request.json['content']

    return jsonify({'data':p[0]}),201

#删除资源
@app.route('/data/<int:did>/',methods=['DELETE'])
def delete_data(did):
    p = list(filter(lambda d: d['id'] == did, data))
    if len(p) == 0:
        abort(404)
    data.remove(p[0])  #移除资源
    return jsonify({'result':'数据已经删除'}) #返回结果

#自定义错误类型
@app.errorhandler(404)
def bad_request(e):
    return jsonify({'error':'请求方法找不到'}),404
#自定义错误类型
@app.errorhandler(405)
def bad_request(e):
    return jsonify({'error':'请求方法有错误'}),405


if __name__ == '__main__':
    manager.run()
