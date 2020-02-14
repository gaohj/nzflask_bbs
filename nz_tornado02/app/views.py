import tornado.web
from .models import create_db,drop_db,Students
from utils.db import session
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('hello tornado')

class TindexHandler(tornado.web.RequestHandler):
    def get(self):
        item = ['苍老师','波老师','龙老师','吉老师']
        item2 = ['程老师','和老师','陈老师','全老师']
        self.render('index.html',item=item,item2=item2)

class DbHandler(tornado.web.RequestHandler):
    def get(self):
        create_db()
        self.write('创建表成功')
class DropHandler(tornado.web.RequestHandler):
    def get(self):
        drop_db()
        self.write('删除表成功')
class AddHandler(tornado.web.RequestHandler):
    def post(self):
        stus = []
        for i in range(100):
            stu = Students()
            stu.s_name = 'nz1904_%s' % i
            stus.append(stu)
        session.add_all(stus)
        session.commit()
        self.write('添加数据成功')

class SelectHandler(tornado.web.RequestHandler):
    def get(self):
        # stu = session.query(Students).all()
        #stu = session.query(Students).filter(Students.s_name=='nz1904_66').all()
        stu = session.query(Students).filter_by(s_name='nz1904_66').all()
        print(stu)
        self.write('查询成功')