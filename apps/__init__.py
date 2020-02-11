from flask import Flask,render_template
from apps.views import config_blueprint
from apps.extensions import config_extensions
from apps.config import config
#创建实例
#封装一个函数 专门用来创建app  这就是 工厂模式
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name]) #告诉我找哪个配置文件
    config[config_name].init_app(app) #让环境生效
    config_blueprint(app) #配置蓝本 跟实例绑定
    config_extensions(app) #配置扩展 跟实例绑定
    config_errorhandler(app) #错误信息跟app完成绑定
    return app

def config_errorhandler(app):
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html')



