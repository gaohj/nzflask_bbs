from flask_script import Manager
from apps import create_app
from flask_migrate import MigrateCommand
from apps.models.users import User
from apps.models.posts import Posts
from apps.extensions import db

#python manage.py db init
#实例化对象并跟app完成绑定
app = create_app('default') #指定此刻我们是什么环境
#详情查看 config 文件
manager = Manager(app)
manager.add_command('db',MigrateCommand)


@manager.command
def create_test_posts():
    for x in range(2,201):
        content = '内容:%s' % x
        author = User.query.first()
        post = Posts(content=content,user=author)
        db.session.add(post)
        db.session.commit()
    print('帖子添加成功')


if __name__ == "__main__":
    manager.run()



