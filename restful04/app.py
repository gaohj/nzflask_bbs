from flask import Flask
import config
from extensions import db
from article_view import bp
from users import user_bp
from models import User,Article,Tag
app = Flask(__name__)
app.config.from_object(config)
app.register_blueprint(bp)
app.register_blueprint(user_bp)
db.init_app(app)


@app.route('/')
def hello_world():
    user = User(username='尼克何杨',email='yang@163.com')
    article = Article(title='他强任他强',content='老子何杨杨')
    article.author = user
    tag1 = Tag(name='篮球界代码写的最好')
    tag2 = Tag(name='代码界篮球打的最好')
    article.tags.append(tag1)
    article.tags.append(tag2)
    db.session.add(article)
    db.session.commit()
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
