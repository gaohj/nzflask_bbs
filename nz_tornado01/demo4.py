from datetime import datetime,timedelta
import os
import tornado.ioloop
import tornado.web
from tornado.options import define,parse_command_line,options
define('port',default=8081,type=int) #定义默认的启动端口号为8081
class MainHandler(tornado.web.RequestHandler): #请求处理的类视图
    #继承于RequestHandler类
    def get(self):
        # name = self.get_argument('name',default='kangbazi',strip=True)
        #name = self.get_query_argument('name',default='kangbazi',strip=True)
        # name = self.get_arguments('name',strip=True)
        name = self.get_query_arguments('name',strip=True)
        self.write('helloadadf99999 %s' % name) #以字符串为参数写入到http的响应中
    def post(self):
        #name= self.get_body_argument('username',default='haha',strip=True)
        #http://127.0.0.1:8004  结果 hello haha
        #name= self.get_body_argument('username',default='haha',strip=True)
        name= self.get_body_arguments('username',strip=True)
        password= self.get_body_arguments('password',strip=True)

        self.write('hello %s:%s' % (name,password))
class ResHandler(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        self.write('<h1>情人节带动一条龙的消费</h1>')
        # self.set_status(500)
        self.set_cookie('token','123321666',expires_days=1)
        # out_time = datetime.now()+timedelta(hours=2)
        # self.set_cookie('token','123321666',expires=out_time)
        #self.clear_cookie('token') #删除指定的cookie
        # self.clear_all_cookies() #清空所有的cookie
        # self.write(self.get_cookie('token'))
        self.set_header('kangbazi','666')
class RoutesHandler(tornado.web.RequestHandler):
    def get(self,year,month,day):
        self.write('日期:%s年%s月%s日'%(day,year,month))

class Routes1Handler(tornado.web.RequestHandler):
    def get(self,year,month,day):
        self.write('日期:%s年%s月%s日'%(day,year,month))

import pymysql

class EntryHandler(tornado.web.RequestHandler):

    def initialize(self):
        #在这里你要完成一些初始化的操作
        self.conn = pymysql.Connect(host='127.0.0.1',user='root',password='123456',database='nz_restful',port=3306)
        self.cursor = self.conn.cursor()
        self.write('我在这里初始化一些东西 类似于魔术方法__init__')
    def prepare(self):
        self.write('我在get之前进行操作')
    def get(self):
        self.write('从数据库中查询数据')
        sql = "select * from user"
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        print(data)
    def on_finish(self):
        self.conn.close()

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')
def make_app():
    return tornado.web.Application(
        handlers=[
            (r'/',MainHandler),
            (r'/index',IndexHandler),
            (r'/res',ResHandler),
            (r'/entry',EntryHandler),
            (r'/routes/(\d{4})/(\d{2})/(\d{2})/',RoutesHandler),
            (r'/routes1/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/',Routes1Handler),
        ],autoreload=True,debug=True,template_path=os.path.join(os.path.dirname(__file__),'templates'),static_path=os.path.join(os.path.dirname(__file__),'static')
    )

if __name__ == "__main__":
    #你想添加启动选项 那么我就监听你的选项是什么
    parse_command_line() #监听启动命令 获取选项
    #启动实例
    app = make_app()
    #监听端口
    app.listen(options.port) #获取你设置的端口号
    #接收客户端的请求
    tornado.ioloop.IOLoop.current().start()
