from flask import Flask,render_template
from flask_script import Manager
from ueditor import bp #导入蓝本
import config
app = Flask(__name__)
manager = Manager(app)
app.config.from_object(config) #让配置文件生效
app.register_blueprint(bp)

@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    manager.run()
