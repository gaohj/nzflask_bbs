from flask_script import Manager
from apps import create_app
from flask_migrate import MigrateCommand

#python manage.py db init
#实例化对象并跟app完成绑定
app = create_app('default') #指定此刻我们是什么环境
#详情查看 config 文件
manager = Manager(app)
manager.add_command('db',MigrateCommand)

if __name__ == "__main__":
    manager.run()



