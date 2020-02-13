from flask import Flask,jsonify,render_template
from flask_script import Manager
import qiniu
app = Flask(__name__)

manager = Manager(app)

@app.route('/')
def hello_world():
    return render_template('index.html')


#获取七牛云的token
@app.route('/gettoken/')
def gettoken():
    # 需要填写你的 Access Key 和 Secret Key
    access_key = 'p_p2-jutlTI1mlPCSfMEO8DyZnkQaiFrd9IOlvpz'
    secret_key = 'rN0YQux570vbhL5d8QvShrV-SnjzTdqhlfWstWri'
    # 构建鉴权对象
    q = qiniu.Auth(access_key, secret_key)
    # 要上传的空间
    bucket_name = 'beimei1904'
    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name)

    return jsonify({'uptoken':token}) #这个键值叫做 uptoken

if __name__ == '__main__':
    manager.run()
