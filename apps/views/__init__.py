from .main import main
from .users import users
from .posts import posts

#配置蓝本
#(蓝本,前缀)
DEFAULT_BLUEPRINT = (
    (main,''),
    (users,'/users'),
    (posts,'/posts')
)
#我们需要将蓝本统一注册完成以后 再注册
#因为后边可能扩展多个蓝本


#封装一个方法 批量完成蓝本注册
def config_blueprint(app):
    for blueprint,url_prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint,url_prefix=url_prefix)


