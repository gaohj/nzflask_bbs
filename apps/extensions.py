#导入扩展
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_login import LoginManager
#创建扩展的对象
bootstrap = Bootstrap()
db = SQLAlchemy()
migrate = Migrate(db=db)
mail = Mail()
login_manager = LoginManager()
#设置只能上传图片
# photos = UploadSet('photos',IMAGES) #创建文件上传对象
#批量将扩展跟app完成绑定
def config_extensions(app):
    bootstrap.init_app(app)
    db.init_app(app) #init_app 传入实例 完成绑定
    migrate.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app) #登录管理的初始化
    #指定登录的url地址是什么
    login_manager.login_view = 'users.login'
    #登录的提示信息   如果用户没有登录如何去提示他
    login_manager.login_message = '请先登录才可以访问'
    #设置session的级别
    #None是没有  basic 是最基本的  strong 是最严格的
    login_manager.session_protection = 'strong'

    # configure_uploads(app,photos)
    # patch_request_class(app,size=None)



