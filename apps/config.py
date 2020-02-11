import os
base_dir = os.path.abspath(os.path.dirname(__file__))
#返回目录的绝对路径
#我们想将sqlite数据库的文件存入到 apps目录下


class Config:
    SECRET_KEY = 'AFAFAFsdfaddsf122345'
    #数据库配置


    #邮件配置
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_USERNAME = '2287228249@qq.com'
    MAIL_PASSWORD = 'vhsbflvpqkbsdjbc'
    #这里的password 不是 邮箱密码 而是激活码
    #使用本地的bootstrap.css
    BOOTSTRAP_SERVE_LOCAL = True

    # 文件上传配置
    # 上传文件的大小

    ALLOWED_EXTENSIONS = set(['jpg','jpeg','gif','png'])
    UPLOADED_PHOTOS_DEST = os.path.join(base_dir, 'static/uploadeds')
    MAX_CONTENT_LENGTH = 8 * 1024 * 1024
    #静态方法 完成特定环境的初始化

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DB_USERNAME = 'root'
    DB_PASSWORD = '123456'
    DB_PORT = '3306'
    DB_NAME = 'memeda'
    DB_HOST = '127.0.0.1'

    DB_URI = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' % (DB_USERNAME,DB_PASSWORD,DB_HOST,DB_PORT,DB_NAME)
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir,'nz1904-dev.sqlite')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'nz1904-product.sqlite')


#为了方便指定当前是什么环境 用字典映射 方便 导出

config = {
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig,
    'default':DevelopmentConfig
}
